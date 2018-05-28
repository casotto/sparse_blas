import numpy as np
cimport numpy as np
from libc cimport stdlib


# Sparse Level 1 routines for BLAS
# https://software.intel.com/en-us/mkl-developer-reference-c-blas-level-1-routines-and-functions
cdef extern from "cblas_sparse_headers.h":
    void cblas_daxpyi(const int nz, const double a, const double *x,
                       const int *indx, double *y)


def sparse_axpyi(double[:] x_values, int[:] x_ind, double[:] y_dense, double a):
    # y = a*x + y
    # a scalar, x compressed, y full_storage


    assert x_values.shape[0] == x_ind.shape[0]
    cdef int nz = <int> x_values.shape[0]
    # take out values from
    cdef double* x = &x_values[0]
    cdef int* indx = &x_ind[0]
    cdef double *y = &y_dense[0]

    cblas_daxpyi(nz, a, x, indx, y)

    return np.asarray(y_dense)
