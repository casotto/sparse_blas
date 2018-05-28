## Sparse Blas

Cython wrapper around the sparse blas library. While scipy exposes bindings
for the dense blas library, there are no headers for the sparse blas library,
that is contained for example, in the Anaconda's mkl distribution.

## Installation

Package is based on a Anaconda installation on python . Ohter distributions are not
supported.

`python setup.py install`
`pytest tests`

## Import from other cython functions

SParse blas package contains headers for some Sparse functions


### Contribute

Add the headers from [MKL documentation](https://software.intel.com/en-us/mkl-developer-reference-c-blas-level-1-routines-and-functions)
