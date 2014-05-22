module Fortran where
import Prelude ()
import Common hiding (Integer, Complex)
import qualified C

data LetterCase = LowerCase
                | UpperCase
                deriving (Eq, Read, Show)

toCase LowerCase = toLower
toCase UpperCase = toUpper

data NameSuffix = NameSuffix String -- ^ fixed suffix
                | Underscore'       -- ^ double underscore if name already
                                    --   contains underscore; otherwise single
                                    --   underscore
                deriving (Eq, Read, Show)

addSuffix (NameSuffix s) name = name <> s
addSuffix Underscore'    name = name <> if '_' `elem` name then "__" else "_"

-- ^ Performs name-mangling on a Fortran name.
mangle :: Config -> String -> String
mangle Config { nameCase = nameCase, nameSuffix = nameSuffix } name =
  addSuffix nameSuffix (toCase nameCase <$> name)

data Type = Character
          | Integer
          | Real
          | DoublePrecision
          | Complex
          | DoubleComplex
          deriving (Eq, Read, Show)

defaultTypeMap t = C.Type $ case t of
    Character       -> "char"
    Integer         -> "int"
    Real            -> "float"
    DoublePrecision -> "double"
    Complex         -> "complex_float"
    DoubleComplex   -> "complex_double"

data Intent = In
            | Out
            | InOut
            deriving (Eq, Read, Show)

data DeclType = DeclType
                { dType   :: Type
                , dArray  :: Bool
                , dIntent :: Intent
                } deriving (Eq, Read, Show)

declType t = DeclType
             { dType   = t
             , dArray  = False
             , dIntent = InOut
             }

data FunctionDecl = FunctionDecl String [(DeclType, String)] (Maybe Type)
                  deriving (Eq, Read, Show)

data ParamConvention = ByValue
                     | ByPointer
                     deriving (Eq, Read, Show)

applyParamConvention ByValue   t = t
applyParamConvention ByPointer t = C.Pointer t

defaultParamConventionMap _ = ByPointer

data ReturnConvention = ReturnValue
                      | FirstParamByPointer
                      deriving (Eq, Read, Show)

applyReturnConvention c name params ret = case c of
  ReturnValue -> C.FunctionDecl name params ret
  FirstParamByPointer -> C.FunctionDecl name
                         ([(C.Pointer $ ret, "ret")] <> params)
                         C.Void

defaultReturnConventionMap Complex       = FirstParamByPointer
defaultReturnConventionMap DoubleComplex = FirstParamByPointer
defaultReturnConventionMap _             = ReturnValue

data Config = Config
  { nameCase            :: LetterCase
  , nameSuffix          :: NameSuffix
  , typeMap             :: Type -> C.Type
  , paramConventionMap  :: Type -> ParamConvention
  , returnConventionMap :: Type -> ReturnConvention
  }

defaultConfig = Config
  { nameCase            = LowerCase
  , nameSuffix          = NameSuffix "_"
  , typeMap             = defaultTypeMap
  , paramConventionMap  = defaultParamConventionMap
  , returnConventionMap = defaultReturnConventionMap
  }

-- default configurations for specific compilers (and platforms)

gfortranConfig     = defaultConfig

ifortConfig        = defaultConfig

ifortWindowsConfig = defaultConfig
  { nameCase   = UpperCase
  , nameSuffix = NameSuffix ""
  }
