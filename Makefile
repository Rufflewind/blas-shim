# linker flag for BLAS
LBLAS=-lblas

# extension of executable file (set this to `.exe` if on Windows)
#EXE=

# flags for C compiler
#CC=cc
CFLAGS=-O3 -fPIC -std=c90 -Wall -pedantic -Idist/include

# flags for archiver
#AR=ar
ARFLAGS=-cru

# flags for creating shared library
SOFLAGS=-shared -Wl,-soname,lib$(LIBNAME).so.$(VERSION)

# ----------------------------------------------------------------------------

NAME=blas-shim
LIBNAME=blasshim
VERSION=0.1.0

all: wrapper lib

clean:
	rm -fr dist

doc:
	cabal haddock --executables
	doxygen

lib: dist/lib/lib$(LIBNAME).a dist/lib/lib$(LIBNAME).so.$(VERSION)

dist/lib/lib$(LIBNAME).a: dist/src/blas.o
	mkdir -p dist/lib
	$(AR) $(ARFLAGS) $@ $<

dist/lib/lib$(LIBNAME).so.$(VERSION): dist/src/blas.o
	mkdir -p dist/lib
	$(CC) $(SOFLAGS) -o $@ $< $(LBLAS)

dist/src/blas.o: \
    dist/src/blas.c \
    dist/include/blas.h \
    dist/include/complex_typedefs.h
	$(CC) $(CFLAGS) -o $@ -c $<

dist/src/blas.c dist/include/blas.h: dist/build/$(NAME)/$(NAME)$(EXE)
	mkdir -p dist/include dist/src
	$<

dist/include/complex_typedefs.h: complex_typedefs.h
	mkdir -p dist/include
	cp $< $@

wrapper: dist/build/$(NAME)/$(NAME)$(EXE)

Common.hs: Common.py
	./$<

dist/setup-config: $(NAME).cabal
	cabal configure

dist/build/$(NAME)/$(NAME)$(EXE): \
    dist/setup-config \
    Blas.hs \
    C.hs \
    Common.hs \
    Fortran.hs \
    Main.hs
	cabal build

test: dist/build/test/test
	LD_LIBRARY_PATH=dist/lib dist/build/test/test

dist/build/test/test: \
    dist/build/test/test-tmp/test.o \
    dist/lib/libblasshim.so.$(VERSION)
	$(CC) $(CFLAGS) -o $@ $< dist/lib/libblasshim.so.$(VERSION)

dist/build/test/test-tmp/test.o: \
    test.c \
    dist/include/blas.h \
    dist/include/complex_typedefs.h
	mkdir -p dist/build/test/test-tmp
	$(CC) $(CFLAGS) -o $@ -c $<
