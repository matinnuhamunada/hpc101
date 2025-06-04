No GIL mode
-----------

.. admonition:: Overview
   :class: Overview

    * **Time:** 10 min
    
    #. Learn how to disable GIL in Numba.
    #. Understand the implications of using ``nogil`` mode.


Since Numba optimizes Python code, it's no longer necessary to hold Python's Global Interpreter Lock 
(GIL). 

.. admonition:: Explanation
   :class: attention 
   
    The GIL is a lock that protects access to Python objects, preventing multiple threads from executing
    Python bytecodes at once. This is necessary in CPython, the standard Python implementation, to ensure
    thread safety. However, it can be a bottleneck in multi-threaded applications, as it prevents true
    concurrency in Python code execution.



By passing ``nogil=True```, Numba will release the GIL when entering the compiled function. 
Releasing the GIL can enable concurrent code execution in multi-threaded environments, but it is 
important to consider the implications of race conditions and synchronization issues.



..  code-block:: python
    :emphasize-lines: 1
    :linenos:

    @jit(nopython=True, nogil=True)
    def f(x, y):
        return x + y

.. admonition:: Key Points
   :class: hint

    #. GIL is not necessary in Numba generated code.
    #. Programmers should be careful with ``nogil`` mode in multi-threaded programming.
    #. ``nogil``` mode goes hand-in-hand with ``nopython`` mode