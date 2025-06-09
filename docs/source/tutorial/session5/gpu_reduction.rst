Reduction in GPU
--------------------

.. admonition:: Overview
   :class: Overview

    * **Tutorial:** 5 min

       
    #. Learn how to perform reduction operations on GPUs.
    #. Understand how to use the `@reduce` decorator in Numba.


Numba offers a `@reduce` decorator that transforms a simple binary operation into a reduction kernel.


.. code-block:: text

    Initial Array:
        [2]   [4]  [6]  [8] [1]  [3]  [5]   [7]

          \   /     \   /     \   /     \   /
           6         14        4         12

              \       /         \       /
                  20               16

                      \       /
                          36

..  code-block:: python
    :linenos:

    import numpy
    from numba import cuda

    @cuda.reduce
    def sum_reduce(a, b):
        return a + b

    A = (numpy.arange(1234, dtype=numpy.float64)) + 1
    normal_sum = A.sum()      # NumPy sum reduction
    gpu_sum = sum_reduce(A)   # cuda sum reduction
    assert normal_sum == gpu_sum



.. admonition:: Key Points
   :class: hint

    #. ``@reduce`` can convert a simple binary operation into a reduction kernel.
    #. Numba's reduction operations can be performed on GPUs, providing efficient parallel computation.