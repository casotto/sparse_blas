#ifndef CBLAS_H
#define CBLAS_H

/*
 * ===========================================================================
 * Prototypes for level 1 BLAS functions (complex are recast as routines)
 * ===========================================================================
 * In order to obtain the headers, all we did was to go to
 * https://software.intel.com/en-us/mkl-developer-reference-c-sparse-blas-level-1-routines
 * select the function of interest
 * copy and paste the function declaration from the Syntax paragraph in the page
 * and then change the macro MKL_INT to int (if someone knows how to explicitely
 * import the Macro in order to make it just a matter fo copy and paste, he is more than
 * welcome! :)
 */

void cblas_daxpyi (const int nz, const double a, const double *x,
                   const int *indx, double *y);

double cblas_ddoti(const int nz, const double *x,
                        const int *indx, const double *y);

void cblas_dgthr(const int nz, double *y,
                        double *x, const int *indx);

#endif
