cdef extern from "cblas_sparse_headers.h":
    void cblas_daxpyi(const int nz, const double a, const double *x,
                       const int *indx, double *y)

    double cblas_ddoti(const int nz, const double *x,
                            const int *indx, const double *y)

    void cblas_dgthr(const int nz, double *y,
                        double *x, const int *indx)