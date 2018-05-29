from distutils.core import setup
from setuptools.extension import Extension
import numpy as np
from Cython.Build import cythonize

sources = []

sources.append("sparse_blas/functions.pyx")


# take out the path to the compiled library against numpy

print np.__config__.show()

np_config = np.__config__.blas_opt_info
include_dirs= np_config["include_dirs"]
libraries= np_config["libraries"]
library_dirs = np_config["library_dirs"]

# extension name of mkl
#https://software.intel.com/en-us/articles/a-new-linking-model-single-dynamic-library-mkl_rt-since-intel-mkl-103
ext = Extension("sparse_blas.functions",
                sources = sources,
                libraries = libraries,
                library_dirs = library_dirs)


# https://stackove(rflow.com/questions/43521852/cython-dynamic-library-linking
# https://stackoverflow.com/questions/45650917/dynamically-linked-dll-with-cython
setup(name = "sparse_blas",
      ext_modules = cythonize([ext]),
        include_dirs=[np.get_include()] + include_dirs
      )
