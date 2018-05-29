import numpy as np
from sparse_blas.functions import sparse_axpyi, sparse_ddoti, sparse_dgthr


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



def test_sparse_ddoti(n = 100, verbose = False):
    nz = np.random.choice(n)
    y = np.random.rand(n)
    y_tmp = y.copy()
    x_values = np.random.rand(nz)
    x_ind = np.random.choice(n,nz,replace=False).astype(np.int)

    x = np.zeros(n)
    x[x_ind] = x_values
    if verbose:
        print "x, {0}".format(x)
        print "y, {0}".format(y)
        print "<x,y>"

    res_sparse = sparse_ddoti(x_values, x_ind, y_tmp)
    res_real = np.dot(x, y)

    print res_sparse, res_real
    np.testing.assert_allclose(res_sparse, res_real)


def test_sparse_dgthr(n = 100):
    nz = np.random.choice(n)
    y = np.random.rand(n)
    y_tmp = y.copy()
    x_values = np.random.rand(nz)
    x_ind = np.random.choice(n,nz,replace=False).astype(np.int)

    x_sub = sparse_dgthr(y,x_ind)


    np.testing.assert_allclose(x_sub,
                               y_tmp[x_ind])