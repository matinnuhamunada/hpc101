Limits of Paralellism
----------------------

.. admonition:: Overview
   :class: Overview

    * **Time:** 30 min

    #. Understand the limits of parallelism in High-Performance Computing (HPC).
    #. Learn about Amdahl's Law and Gustafson's Law, which describe the limits of parallel processing.

In High-Performance Computing (HPC), while parallelism is a powerful tool for improving performance, it has its 
limits. Understanding these limits is crucial for effectively designing and optimizing parallel applications.
These limits can be broadly categorized into two types: **Amdahl's Law** and **Gustafson's Law**.

Amdahl's Law
^^^^^^^^^^^^^^^^^^^^^^^

Amdahl's Law states that the maximum speedup of a program using parallel processing is limited by the sequential 
portion of the program. It can be expressed mathematically as:

.. math::

    S = \frac{1}{(1 - P) + \frac{P}{N}}

where:

* :math:`S` is the maximum speedup,
* :math:`P` is the parallelizable portion of the program (between 0 and 1),
* :math:`N` is the number of processors.

This means that even with an infinite number of processors, the speedup is limited by the fraction of the 
program that cannot be parallelized. For example, if 90% of a program can be parallelized, the maximum speedup 
is:

.. math::

    S = \frac{1}{(1 - 0.9) + \frac{0.9}{N}} = \frac{1}{0.1 + \frac{0.9}{N}}

As :math:`N` approaches infinity, the speedup approaches 10x, indicating that the sequential portion limits the 
overall performance gain.

Gustafson's Law
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gustafson's Law, on the other hand, argues that as the problem size increases, the parallel portion of the 
program also increases, leading to better scalability. It can be expressed as:

.. math::

    S = N - (1 - P) \cdot (N - 1)

where:

* :math:`S` is the speedup,
* :math:`N` is the number of processors,
* :math:`P` is the parallelizable portion of the program.

This law suggests that as we increase the problem size, we can achieve better speedup with more processors. 
For example, if we have 100 processors and 90% of the program can be parallelized, the speedup is:

.. math::

    S = 100 - (1 - 0.9) \cdot (100 - 1) = 100 - 0.1 \cdot 99 = 100 - 9.9 = 90.1


This indicates that as the problem size grows, the speedup can approach the number of processors, making parallel
computing more effective. Understanding these limits helps in designing efficient parallel algorithms and 
systems. 

While Amdahl's Law highlights the constraints imposed by the sequential parts of a program, 
Gustafson's Law emphasizes the potential for scalability with larger problem sizes.

.. important::

    Scalability refers to a system's ability to handle increased load or growth—such as more users, data, or 
    tasks—without sacrificing performance, reliability, or manageability.  


.. admonition:: Key Points
   :class: hint
   
    1. Amdahl's Law limits speedup based on the sequential portion of a program.
    2. Gustafson's Law emphasizes scalability with larger problem sizes.
    3. Understanding these limits is crucial for designing efficient parallel applications.
   