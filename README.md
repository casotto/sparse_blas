## Sparse Blas

In your journey to [optimize your python code](https://www.youtube.com/watch?v=zQeYx87mfyw), at some point you can touch a level where, no matter you ported all your code to **cython**, the bottleneck is given by linear algebra operations.

 At this stage, the most efficient way to optimize your code is to use the [BLAS](http://www.netlib.org/blas/blast-forum/) routines for linear algebra. Luckily, the BLAS dense routines are exposed to cython through [scipy](https://docs.scipy.org/doc/scipy/reference/linalg.blas.html), so, in order to use them is to add the `from scipy.linalg.blas cimport c_name_of_routine` in your code and you're pretty to go.

However, the **Sparse BLAS** routines are not accessible through scipy, and hence there is no easy way to profit from processor based optimization for sparse operations.

This repo sums up a **working experiment** (in Windows and Linux) to call the Sparse BLAS routines from the MKL library provided by default in the Anaconda distribution, that can be easily installed by typing `conda install mkl` 


## Installation

Package is based on a Anaconda installation on python . Ohter distributions are not supported.
`conda install mkl` (be sure that your distribution is linked against the mkl, reinstalls numpy if necessary)

`python setup.py install`

`pytest tests`


## Use the routines in a package

In order to call the routines for your own package, you need to modify your `setup.py` by 

* `add libraries and library_dirs keywords on the Extension class`
* `add include_dirs argument in the setup function`

Take a look at `setup.py` to see what the instructions above mean.


### Contribute

Sparse blas package contains headers for some Sparse functions, to include other functions just take a look at [the c headers](https://github.com/casotto/sparse_blas/blob/master/sparse_blas/cblas_sparse_headers.h) for instructions.