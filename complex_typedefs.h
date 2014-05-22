#ifndef  HAVE_COMPLEX_TYPEDEFS
# define HAVE_COMPLEX_TYPEDEFS
/*
  If these typedefs are already defined, then define `HAVE_COMPLEX_TYPEDEFS`
  to skip this header.  Otherwise:

    - in C++, `complex_T` shall alias to `std::complex<T>`;

    - in C, `complex_T` shall alias to either the built-in complex types (C99
      or newer) or structs with the same representations.
 */
# ifdef __cplusplus
#  include <complex>
   typedef std::complex<float>  complex_float;
   typedef std::complex<double> complex_double;
# else
#  if __STDC_VERSION__ >= 199901L && !defined(__STDC_NO_COMPLEX__)
    typedef float  _Complex complex_float;
    typedef double _Complex complex_double;
#  else
    typedef struct complex_float {
        float  real, imag;
    } complex_float;
    typedef struct complex_double {
        double real, imag;
    } complex_double;
#  endif
# endif
#endif
