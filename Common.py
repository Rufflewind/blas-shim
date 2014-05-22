#!/usr/bin/env python
from __future__ import unicode_literals
s = '''

# GHC Boot:
#
# array
# base
# binary
# bytestring
# Cabal
# containers
# deepseq
# directory
# filepath
# ghc-prim
# haskeline
# haskell98
# haskell2010
# hoopl
# hpc
# integer-gmp
# integer-simple
# old-locale
# old-time
# pretty
# process
# template-haskell
# terminfo
# time
# transformers
# unix
# Win32
# xhtml

# don't import `const`; use `pure` instead
name: Common
imports:
  Prelude: |
    Bool:
      False
      True
    (&&)
    (||)
    not
    otherwise
    Either:
      Left
      Right
    either
    Ordering:
      LT
      EQ
      GT
    String
    Eq
      (==)
      (/=)
    Ord
      compare
      (<)
      (>=)
      (>)
      (<=)
      max
      min
    Enum
      succ
      pred
      toEnum
      fromEnum
      enumFrom
      enumFromThen
      enumFromTo
      enumFromThenTo
    Bounded
      minBound
      maxBound
    Int
    Integer
    Float
    Double
    Rational
    Num:
      (+)
      (*)
      (-)
      negate
      abs
      signum
      fromInteger
    Real
      toRational
    Integral
      quot
      rem
      div
      mod
      quotRem
      divMod
      toInteger
    Fractional
      (/)
      recip
      fromRational
    Floating
      pi
      exp
      sqrt
      log
      (**)
      logBase
      sin
      tan
      cos
      asin
      atan
      acos
      sinh
      tanh
      cosh
      asinh
      atanh
      acosh
    RealFrac
      properFraction
      truncate
      round
      ceiling
      floor
    RealFloat
      floatRadix
      floatDigits
      floatRange
      decodeFloat
      encodeFloat
      exponent
      significand
      scaleFloat
      isNaN
      isInfinite
      isDenormalized
      isNegativeZero
      isIEEE
      atan2
    subtract
    even
    odd
    gcd
    lcm
    (^)
    (^^)
    fromIntegral
    realToFrac
    id
    (.)
    flip
    ($)
    until
    asTypeOf
    error
    undefined
    seq
    ($!)
    (++)
    (!!)
    ShowS
    Show(show)
    shows
    showChar
    showString
    showParen
    ReadS
    Read
      readsPrec
      readList
    reads
    readParen
    read
    lex

  Control.Applicative: |
    Applicative
      pure
      (<*>)
      (*>)
      (<*)
    Alternative
      empty
      (<|>)
      some
      many
    (<$>)
    (<**>)
    liftA
    liftA2
    liftA3
    optional

  Control.Arrow: |
    Arrow
      arr
      first
      second
      (***)
      (&&&)
    returnA
    (^>>)
    (>>^)
    (>>>)
    (<<<)
    (<<^)
    (^<<)
    ArrowZero
      zeroArrow
    ArrowChoice
      left
      right
      (+++)
      (|||)
    ArrowApply
      app
    ArrowLoop
      loop

  Control.Monad: |
    Monad
      (>>=)
      (>>)
      return
      fail
    MonadPlus
      mzero
      mplus
    (=<<)
    (<=<)
    (>=>)
    ap
    filterM
    foldM
    forever
    guard
    join
    liftM
    liftM2
    liftM3
    liftM4
    liftM5
    mapAndUnzipM
    mfilter
    replicateM
    replicateM_
    unless
    void
    when
    zipWithM
    zipWithM_

  Control.Monad.Fix: |
    MonadFix
      mfix

  Data.Char: |
    Char
    isControl
    isSpace
    isLower
    isUpper
    isAlpha
    isAlphaNum
    isPrint
    isDigit
    isOctDigit
    isHexDigit
    isLetter
    isMark
    isNumber
    isPunctuation
    isSymbol
    isSeparator
    isAscii
    isLatin1
    isAsciiUpper
    isAsciiLower
    GeneralCategory:
      UppercaseLetter
      LowercaseLetter
      TitlecaseLetter
      ModifierLetter
      OtherLetter
      NonSpacingMark
      SpacingCombiningMark
      EnclosingMark
      DecimalNumber
      LetterNumber
      OtherNumber
      ConnectorPunctuation
      DashPunctuation
      OpenPunctuation
      ClosePunctuation
      InitialQuote
      FinalQuote
      OtherPunctuation
      MathSymbol
      CurrencySymbol
      ModifierSymbol
      OtherSymbol
      Space
      LineSeparator
      ParagraphSeparator
      Control
      Format
      Surrogate
      PrivateUse
      NotAssigned
    generalCategory
    toUpper
    toLower
    toTitle
    digitToInt
    intToDigit
    ord
    chr
    showLitChar
    lexLitChar
    readLitChar

  Data.Complex: |
    Complex:
      :+
    cis
    conjugate
    imagPart
    magnitude
    mkPolar
    polar
    phase
    realPart

  Data.Foldable: |
    Foldable
      fold
      foldMap
      foldr
      foldr'
      foldl
      foldl'
      foldr1
      foldl1
    all
    and
    any
    asum
    concat
    concatMap
    elem
    find
    foldlM
    foldrM
    forM_
    for_
    mapM_
    maximum
    maximumBy
    minimum
    minimumBy
    msum
    notElem
    or
    product
    sequenceA_
    sequence_
    sum
    traverse_

  Data.Functor: |
    Functor
      fmap
      (<$)

  Data.Function: |
    fix
    on

  Data.List: | # (incomplete)
    intercalate
    permutations

  Data.Maybe: |
    Maybe:
      Nothing
      Just
    catMaybes
    fromJust
    fromMaybe
    isJust
    isNothing
    listToMaybe
    mapMaybe
    maybe
    maybeToList

  Data.Monoid: | # (intentionally incomplete)
    Monoid
      mempty
      mappend
      mconcat
    (<>)

  Data.Ratio: |
    Ratio
    (%)
    numerator
    denominator
    approxRational

  Data.Traversable: |
    Traversable
      traverse
      sequenceA
      mapM
      sequence
    for
    forM
    mapAccumL
    mapAccumR
    fmapDefault
    foldMapDefault

  Data.Word: |
    Word
    Word8
    Word16
    Word32
    Word64

  Debug.Trace: |
    trace
    traceIO
    traceShow
    traceStack

  Data.Tuple: |
    fst
    snd
    curry
    uncurry
    swap

  # TODO move this into a separate wrapper library
  Data.ListLike: |
    zip
    zipWith
    unzip
    ListLikeIO
      hGetLine
      hGetContents
      hGet
      hGetNonBlocking
      hPutStr
      hPutStrLn
      getLine
      getContents
      putStr
      putStrLn
      interact
      readFile
      writeFile
      appendFile
    ListLike
      singleton
      cons
      snoc
      append
      head
      last
      tail
      init
      null
      length
      rigidMap
      reverse
      intersperse
      rigidConcatMap
      replicate
      take
      drop
      splitAt
      takeWhile
      dropWhile
      span
      break
      group
      inits
      tails
      isPrefixOf
      isSuffixOf
      isInfixOf
      filter
      partition
      index
      elemIndex
      elemIndices
      findIndex
      findIndices
      rigidMapM
      nub
      delete
      deleteFirsts
      union
      intersect
      sort
      insert
      toList
      fromList
      fromListLike
      nubBy
      deleteBy
      deleteFirstsBy
      unionBy
      intersectBy
      groupBy
      sortBy
      insertBy
      genericLength
      genericTake
      genericDrop
      genericSplitAt
      genericReplicate
    StringLike
      toString
      fromString
      lines
      words
    InfiniteListLike
      iterate
      repeat
      cycle

  System.Environment: |
    getArgs
    getProgName
    getEnv
    withArgs
    withProgName
    getEnvironment

  System.Exit: |
    ExitCode:
      ExitSuccess
      ExitFailure
    exitWith
    exitFailure
    exitSuccess

  System.IO: |
    IO
    FilePath
    Handle
    stdin
    stdout
    stderr
    withFile
    openFile
    IOMode:
      ReadMode
      WriteMode
      AppendMode
      ReadWriteMode
    hClose
    hFileSize
    hSetFileSize
    hIsEOF
    isEOF
    BufferMode:
      NoBuffering
      LineBuffering
      BlockBuffering
    hGetBuffering
    hSetBuffering
    hFlush
    hGetPosn
    hSetPosn
    HandlePosn
    hSeek
    SeekMode:
      AbsoluteSeek
      RelativeSeek
      SeekFromEnd
    hTell
    hIsOpen
    hIsClosed
    hIsReadable
    hIsWritable
    hIsSeekable
    hIsTerminalDevice
    hSetEcho
    hGetEcho
    hShow
    hWaitForInput
    hReady
    hGetChar
    hLookAhead
    hPrint
    putChar
    print
    getChar
    readIO
    readLn
    withBinaryFile
    openBinaryFile
    hSetBinaryMode
    hPutBuf
    hGetBuf
    hGetBufSome
    hPutBufNonBlocking
    hGetBufNonBlocking
    openTempFile
    openBinaryTempFile
    openTempFileWithDefaultPermissions
    openBinaryTempFileWithDefaultPermissions
    hSetEncoding
    hGetEncoding
    TextEncoding
    latin1
    utf8
    utf8_bom
    utf16
    utf16le
    utf16be
    utf32
    utf32le
    utf32be
    localeEncoding
    char8
    mkTextEncoding
    hSetNewlineMode
    Newline:
      LF
      CRLF
    nativeNewline
    NewlineMode:
      NewlineMode
    inputNL
    outputNL
    noNewlineTranslation
    universalNewlineMode
    nativeNewlineMode

  System.IO.Error: |
    IOError
    mkIOError
    annotateIOError
    isAlreadyExistsError
    isDoesNotExistError
    isAlreadyInUseError
    isFullError
    isEOFError
    isIllegalOperation
    isPermissionError
    isUserError
    ioeGetErrorType
    ioeGetLocation
    ioeGetErrorString
    ioeGetHandle
    ioeGetFileName
    ioeSetErrorType
    ioeSetErrorString
    ioeSetLocation
    ioeSetHandle
    ioeSetFileName
    IOErrorType
    alreadyExistsErrorType
    doesNotExistErrorType
    alreadyInUseErrorType
    fullErrorType
    eofErrorType
    illegalOperationErrorType
    permissionErrorType
    userErrorType
    isAlreadyExistsErrorType
    isDoesNotExistErrorType
    isAlreadyInUseErrorType
    isFullErrorType
    isEOFErrorType
    isIllegalOperationErrorType
    isPermissionErrorType
    isUserErrorType
    ioError
    catchIOError
    tryIOError
    modifyIOError

  Text.Printf: |
    printf
    hPrintf
    PrintfType
    HPrintfType
    PrintfArg
    IsChar

'''
import sys, unicodedata

# import YAML library with Unicode support
import yaml
def construct_yaml_str(self, node):
    return self.construct_scalar(node)
yaml.Loader.add_constructor("tag:yaml.org,2002:str", construct_yaml_str)
yaml.SafeLoader.add_constructor("tag:yaml.org,2002:str", construct_yaml_str)

if __name__ != "__main__":
    raise Exception("This script is not meant to be imported.")

data = yaml.safe_load(s)
name = data["name"]
imports = data["imports"]
out_filename = name + ".hs"
out_imports = []
append = out_imports.append
all_symbols = []

for module, symbols in sorted(imports.items()):
    out_imports.append("import " + module)
    if symbols:                         # export specific symbols
        symbols_ = []
        in_group = False
        for symbol in symbols.split("\n"):
            # remove whitespace and calculate indent
            symbol = symbol.rstrip()
            indent = len(symbol)
            symbol = symbol.lstrip()
            indent -= len(symbol)
            # ignore blank lines
            if not symbol:
                continue
            # add brackets if needed
            head = symbol[0]
            head_type = unicodedata.category(head)[0]
            last = symbol[-1]
            if head != "(" and last != ")" and head_type in "PS":
                symbol = "(" + symbol + ")"
            # deal with groups
            if in_group:
                if indent:
                    # continue group
                    subsymbols.append(symbol)
                    continue
                # end group
                in_group = False
                symbols_[-1] += ", ".join(subsymbols) + ")"
            if last == ":" and head_type not in "PS":
                # begin group
                in_group = True
                subsymbols = []
                symbols_.append(symbol[:-1] + "(")
                continue
            symbols_.append(symbol)
        if in_group:                    # end group
            in_group = False
            symbols_[-1] += ", ".join(subsymbols) + ")"
        all_symbols.extend(symbols_)
        out_imports.append(" (")
        out_imports.append(", ".join(symbols_))
        out_imports.append(")")
    else:                               # export entire module
        all_symbols.append("module " + module)
    out_imports.append("\n")

out_str = "".join([
    "-- autogenerated from ", sys.argv[0], "\n",
    "module ", name, " (", ", ".join(all_symbols), ") where\n"
] + out_imports)
with open(out_filename, "w") as f:
    f.write(out_str)
