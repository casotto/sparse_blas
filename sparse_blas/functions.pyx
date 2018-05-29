import numpy as np
cimport numpy as np
from libc cimport stdlib


# Sparse Level 1 routines for BLAS
# https://software.intel.com/en-us/mkl-developer-reference-c-blas-level-1-routines-and-functions


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


def sparse_ddoti(double[:] x_values, int[:] x_ind, double[:] y_dense):
    # res = x[0]*y[indx[0]] + x[1]*y[indx[1]] +...+ x[nz-1]*y[indx[nz-1]]
    # (nz, x_values, x_ind) represents a sparse vector
    # y is a vector of full storage form


    assert x_values.shape[0] == x_ind.shape[0]
    cdef int nz = <int> x_values.shape[0]
    # take out values from
    cdef double* x = &x_values[0]
    cdef int* indx = &x_ind[0]
    cdef double *y = &y_dense[0]
    cdef double dot

    dot = cblas_ddoti(nz,x,indx, y)

    return dot

def sparse_dgthr(double[:] y_dense, int[:] x_ind):
    assert y_dense.shape[0] >= x_ind.shape[0]
    cdef int nz = <int> x_ind.shape[0]
    cdef double[:] x_sub = np.zeros(nz)

    # take out values from
    cdef double* x = &x_sub[0]
    cdef int* indx = &x_ind[0]
    cdef double *y = &y_dense[0]

    cblas_dgthr(nz, y, x, indx)

    return np.asarray(x_sub)
