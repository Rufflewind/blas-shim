BLAS Shim
=========

This is a small library that wraps an existing Fortran interface of BLAS.

Note: This is an *incomplete work*, as most of the BLAS functions are still
missing.  However, it is trivial to add additional BLAS functions as the
infrastructure for automatic generation is quite complete: one can simply add
more functions to the `blasFuns` variable in `Blas.hs`.

Building
--------

The makefile will automate pretty much everything and generate the wrapper
libraries (both static and shared).  Be sure to set the correct linker flags
for your BLAS implementation by overriding the `LBLAS` variable in the makefile.

The wrapper generator is written in Haskell and, when executed, creates two
files:

- `blas.h`: This header file is to be included and supplies the declarations
  of the normalized interface.

- `blas.c`: This is the implementation of the wrapper.

There is an additional supplementary header, `complex_typedefs.h`, which
provides type aliases for the complex number type.  It uses the standard
complex number types if possible, falling back to a simple struct if it's not
supported (e.g. in C90).

Dependencies
------------

  - [Haskell][3] environment
  - [ListLike][4]
  - C compiler and associated build tools
  - BLAS implementation

Motivation
----------

BLAS implementations generally provide two kinds of interfaces: one for C and
one for Fortran.  The C interface is much more portable than the Fortran
interface due to lack of a standard Fortran calling convention, but the C
interface is not nearly as ubiquitous.  There are a few ways to overcome this:

- One can build the official [CBLAS][1] interface wrapper ([download][2]).
  This is the most straightforward approach but the interfaces .

- Alternatively, one can call the Fortran functions directly.  One must then
  account for the differences in the Fortran calling convention, which can
  vary depending on the Fortran compiler.  The goal of this library is to
  *automatically generate* a wrapper so as to normalize these differences.

Interface
---------

The function signatures in the normalized interface are exactly what one'd
expect if each type was translated literally.  The parameters are no longer
passed as pointers (which is very awkward to use) as they would be if the
Fortran interface was used directly.  Of course, the array arguments are still
passed as pointers for obvious reasons.

To avoid conflicts with existing BLAS implementations, the normalized
functions are named with a prefix `bls_`.

[1]: http://netlib.org/blas/blast-forum/cinterface.pdf
[2]: http://netlib.org/blas/blast-forum/cblas.tgz
[3]: http://haskell.org
[4]: https://hackage.haskell.org/package/ListLike
