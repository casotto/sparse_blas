import numpy as np
from sparse_blas.functions import sparse_axpyi


def test_sparse_dot(n = 100, verbose = True):
    nz = np.random.choice(n)
    y = np.random.rand(n)
    y_tmp = y.copy()
    a = 3.
    x_values = np.random.rand(nz)
    x_ind = np.random.choice(n,nz,replace=False).astype(np.int)

    x = np.zeros(n)
    x[x_ind] = x_values
    if verbose:
        print "a, {0}".format(a)
        print "x, {0}".format(x)
        print "y, {0}".format(y)
        print "a *x +y"

    res_sparse = sparse_axpyi(x_values, x_ind, y_tmp, a)
    res_real = a * x + y
    np.testing.assert_allclose(res_sparse, res_real)