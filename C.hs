module C where
import Prelude ()
import Common

data Type = Type String
          | Void
          | Const Type
          | Volatile Type
          | Pointer Type
          | Array (Maybe Integer) Type
          | Function [(Type, String)] Type
          deriving (Eq, Read, Show)

data FunctionDecl = FunctionDecl String [(Type, String)] Type
                  deriving (Eq, Read, Show)

-- ^ Parenthesize the string if the boolean argument is true.
parensIf b s = if b then "(" <> s <> ")" else s

-- here, `p` is precedence: `*` has 1 while `[]` and `()` have 2
prettyType'      = prettyType 9
prettyType p t r = case t of
  Type     s   -> s <> if null r then "" else " " <> r
  Void         -> prettyType p (Type "void") r
  Const    t   -> prettyType 1 t $    "const " <> parensIf (p < 1) r
  Volatile t   -> prettyType 1 t $ "volatile " <> parensIf (p < 1) r
  Pointer  t   -> prettyType 1 t $         "*" <> parensIf (p < 1) r
  Array    n t -> prettyType 2 t $ parensIf (p < 2) r <> "[" <> n' <> "]"
    where  n'   = fromMaybe "" $ show <$> n
  Function a t -> prettyType 2 t $ parensIf (p < 2) r <> "(" <> a' <> ")"
    where  a'   = intercalate ", " $ uncurry prettyType' <$> a

prettyFunctionDecl (FunctionDecl name args ret) =
  prettyType' (Function args ret) name
