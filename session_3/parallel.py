import numba
from numba import jit, int32, prange, vectorize, float64, cuda
import numpy as np

import time


@jit(nopython=True)
def reduction_without_parallel(n):
    shp = (13, 17)
    result1 = 2 * np.ones(shp, np.int_)
    tmp = 2 * np.ones_like(result1)

    for i in prange(n):
        result1 *= tmp

    return result1


@jit(nopython=True, parallel=True)
def reduction_with_parallel(n):
    shp = (13, 17)
    result1 = 2 * np.ones(shp, np.int_)
    tmp = 2 * np.ones_like(result1)

    for i in prange(n):
        result1 *= tmp

    return result1


start = time.time()
reduction_without_parallel(10000000)
end = time.time()
print("Time without parallel:", end - start)

start = time.time()
reduction_with_parallel(10000000)
end = time.time()
print("Time with parallel:", end - start)
