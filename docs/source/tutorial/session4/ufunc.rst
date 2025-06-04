Universal Functions
--------------------------

.. admonition:: Overview
   :class: Overview

    * **Time:** 10 min

        
    #. Learn how to implement ufunc in Python.
    #. Understand how to use the vectorize decorator in Numba.


A universal function (ufunc) performs element-by-element operations on NumPy arrays. While creating 
traditional ufuncs in NumPy requires writing C code, Numba simplifies this process. With the 
``vectorize()`` decorator, Numba can compile a pure Python function into a ufunc that operates on 
NumPy arrays with performance comparable to ufuncs written in C.

..  code-block:: python
    :emphasize-lines: 1
    :linenos:

    @vectorize([float64(float64, float64)]) 
    def sinacosb_vect(a, b):
        return math.sin(a) * math.cos(b)



.. admonition:: Key Points
   :class: hint

    #. Numba can simplify ufunc in Python.
    #. The ``vectorize`` decorator compiles a Python function into a ufunc.