Vectorize
----------

.. admonition:: Overview
   :class: Overview

    * **Time:** 10 min

    
    #. Learn how to use vectorize to implement ufunc.
    #. Understand how to specify multiple signatures for vectorized functions.

Numba's vectorize feature enables Python functions that take scalar inputs to be used as NumPy ufuncs.
By applying the vectorize() decorator, Numba compiles a pure Python function into a ufunc that can 
process NumPy arrays with performance comparable to traditional ufuncs written in C. As with any 
Numba function, you can choose between ``eager`` or ``lazy`` mode for vectorization.

..  code-block:: python
    :emphasize-lines: 1, 3, 4, 5, 6
    :linenos:

    from numba import vectorize, int32, int64, float32, float64

    @vectorize([int32(int32, int32),
                int64(int64, int64),
                float32(float32, float32),
                float64(float64, float64)])
    vec_test(x, y):
        return x + y

When specifying multiple signatures, make sure to list the most specific ones before the more general
ones.

.. admonition:: Key Points
   :class: hint
   
    #. Numba's vectorize feature allows Python functions to be used as NumPy ufuncs.
    #. The vectorize() decorator compiles a Python function into a ufunc.
    #. You can specify multiple signatures for vectorized functions, with more specific ones listed first.