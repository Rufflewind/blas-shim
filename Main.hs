module Main where
import Prelude ()
import Common
import Blas
import qualified C
import qualified Fortran as F

mapFst f (x, y) = (f x, y)

convRet config (Just t) = (F.typeMap config t, F.returnConventionMap config t)
convRet _      Nothing  = (C.Void, F.ReturnValue)

convIntent F.In = C.Const
convIntent _    = id

convParamF config (F.DeclType t a i) =
  (if a then C.Pointer else applyConvention) .
  convIntent i $ F.typeMap config t
  where applyConvention = F.applyParamConvention $
                          F.paramConventionMap config t

convParamC config (F.DeclType t a i) =
  (if a then C.Pointer . convIntent i else id) $ F.typeMap config t

convArg (F.DeclType _ a _, n) = (if a then "" else "&") <> n

cWrap config (BFun varTypes func) = convert config . func <$> varTypes

convert config (F.FunctionDecl name params ret) =
  (fDecl, wDecl, "{\n" <> wBody <> "}\n\n")
  where fDecl       = F.applyReturnConvention cvn fName fParams wRet
        fName       = F.mangle config name
        fParams     = (mapFst $ convParamF config) <$> params
        args        = intercalate ", " $ convArg <$> params
        call args   = fName <> "(" <> args <> ");\n"
        (wRet, cvn) = convRet config ret
        wDecl       = C.FunctionDecl wName wParams wRet
        wName       = modifyName $ toLower <$> name
        wParams     = (mapFst $ convParamC config) <$> params
        wBody       = case cvn of
          F.ReturnValue -> (<> call args) $
            case wRet of
              C.Void -> "    "
              _      -> "    return "
          F.FirstParamByPointer ->
            "    " <> C.prettyType' wRet "return_value" <> ";\n" <>
            "    " <> call ("&return_value, " <> args) <>
            "    return return_value;\n"

showDecl = (<> ";\n\n") . C.prettyFunctionDecl

modifyName = ("bls_" <>)

main = do
  let wraps  = mconcat $ cWrap F.defaultConfig <$> blasFuns
  let fDecls = (<$> wraps) $ \ (x, _, _) -> x
  let wDecls = (<$> wraps) $ \ (_, x, _) -> x
  let wDefs  = (<$> wraps) $ \ (_, decl, body) ->
               C.prettyFunctionDecl decl <> "\n" <> body

  let fnRoot    = "blas"
  let headerFn  = fnRoot <> ".h"
  let sourceFn  = fnRoot <> ".c"
  let guardName = "SIINKPBGOYKIBQIVESTPJJLLJJRXQXDVBZSDSRYQ"

  -- header
  withFile ("dist/include/" <> headerFn) WriteMode $ \ h -> do
    hPutStrLn h `mapM_`
      [ "#ifndef " <> guardName
      , "#define " <> guardName
      , "#ifndef HAVE_COMPLEX_TYPEDEFS"
      , "#include \"complex_typedefs.h\""
      , "#endif"
      , "#ifdef __cplusplus"
      , "extern \"C\" {"
      , "#endif"
      , ""
      ]
    hPutStr h `mapM_` (showDecl <$> wDecls)
    hPutStrLn h `mapM_`
      [ "#ifdef __cplusplus"
      , "}"
      , "#endif"
      , "#endif"
      ]

  -- source
  withFile ("dist/src/" <> sourceFn) WriteMode $ \ h -> do
    hPutStrLn h `mapM_`
      [ "#include \"" <> headerFn <> "\""
      ]
    hPutStr h `mapM_` (showDecl <$> fDecls)
    hPutStr h `mapM_` wDefs
