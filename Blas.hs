module Blas where
import Prelude ()
import Common
import qualified Fortran as F

data BFun = BFun { bfRange   :: [F.Type]
                 , bfFuncMap :: F.Type -> F.FunctionDecl
                 }

s = [ F.Real ]
d = [ F.DoublePrecision ]
c = [ F.Complex ]
z = [ F.DoubleComplex ]
sd = s <> d
cz = c <> z
sdcz = sd <> cz

prefix F.Real            = "s"
prefix F.DoublePrecision = "d"
prefix F.Complex         = "c"
prefix F.DoubleComplex   = "z"

realPrefix F.Real            = "s"
realPrefix F.DoublePrecision = "d"
realPrefix F.Complex         = "sc"
realPrefix F.DoubleComplex   = "dz"

realType F.Complex       = F.Real
realType F.DoubleComplex = F.DoublePrecision
realType t               = t

param         n t = ((F.declType t) { F.dIntent = F.In }, n)
paramArray    n t = ((F.declType t) { F.dIntent = F.In,  F.dArray = True }, n)
paramMutArray n t = ((F.declType t) { F.dIntent = F.Out, F.dArray = True }, n)

-- | Blas function signatures.
blasFuns =

  [ BFun sdcz $ \ t ->
    F.FunctionDecl (realPrefix t <> "asum")
    [ param      "n"    F.Integer
    , paramArray "x"    t
    , param      "incx" F.Integer
    ] $ Just $ realType t

  , BFun sdcz $ \ t ->
    F.FunctionDecl (prefix t <> "gemm")
    [ param         "transa" F.Character
    , param         "transb" F.Character
    , param         "m"      F.Integer
    , param         "n"      F.Integer
    , param         "k"      F.Integer
    , param         "alpha"  t
    , paramArray    "a"      t
    , param         "lda"    F.Integer
    , paramArray    "b"      t
    , param         "ldb"    F.Integer
    , param         "beta"   t
    , paramMutArray "c"      t
    , param         "ldc"    F.Integer
    ] Nothing

  ]
