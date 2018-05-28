#ifndef CBLAS_H
#define CBLAS_H

/*
 * ===========================================================================
 * Prototypes for level 1 BLAS functions (complex are recast as routines)
 * ===========================================================================
 */

void cblas_daxpyi (const int nz, const double a, const double *x,
                   const int *indx, double *y);

#endif
