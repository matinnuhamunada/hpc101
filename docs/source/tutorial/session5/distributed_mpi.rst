
Distributed Parallelism
----------------------------------------------------


.. admonition:: Overview
   :class: Overview

    * **Tutorial:** 30 min

    #. Learn how to use MPI for distributed parallelism.
    #. Understand the relationship between distributed parallelism and MPI.


We will use the GPU programming in Numba to accelerate our code.

Distributed parallelism is a model of parallel computing where the workload is split across multiple 
independent computing units (often across different machines), each with its own memory and processor. 
These units communicate and coordinate via a network.

``MPI`` (Message Passing Interface) is the primary programming model and standard used to implement 
distributed parallelism.  MPI is a standardized and portable message-passing system designed to allow processes to communicate 
with each other in a distributed computing environment. It provides a set of functions that enable 
data exchange, synchronization, and coordination among processes running on different nodes in a 
cluster or across multiple machines. 

.. list-table:: Relationship Between Distributed Parallelism and MPI
   :widths: 30 70
   :header-rows: 1

   * - Distributed Parallelism Concept
     - How MPI Supports It
   * - **Multiple Processes**
     - MPI programs run as multiple processes, each with its own ID (``rank``).
   * - **Independent Memory**
     - Each MPI process has its own address space (no shared memory).
   * - **Communication Between Nodes**
     - MPI provides functions like ``Send``, ``Recv``, ``Scatter``, ``Gather``, and ``Broadcast``.
   * - **Synchronization**
     - MPI allows synchronization (e.g., ``Barrier``) to coordinate steps.
   * - **Scalability**
     - MPI programs scale to thousands of processes on large clusters.

.. admonition:: Explanation
   :class: attention

        MPI uses message passing to coordinate and communicate between independent processes. These processes:
        * Run independently (separate memory and execution).
        * Communicate by sending and receiving messages.
        * Are typically started together via a launcher like ``mpirun``.


Overview Diagram
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This program demonstrates how to use ``mpi4py`` to perform **parallel array addition**. It splits two 
arrays among processes, computes the addition in parallel, and gathers the result.

.. code-block:: text

               +---------+         +---------+         +---------+
               | Rank 0  |         | Rank 1  |   ...   | Rank N  |
               +---------+         +---------+         +---------+
                    ↓                   ↓                   ↓
             [A0, A1, A2,...]     [An, An+1,...]     [Am,..., A99]
             [B0, B1, B2,...]     [Bn, Bn+1,...]     [Bm,..., B99]
                    ↓                   ↓                   ↓
             [C0, C1, C2,...]     [Cn, Cn+1,...]     [Cm,..., C99]
                    ↓                   ↓                   ↓
                         → GATHERED TO RANK 0 →
                  [C0, C1, C2, ..., C99] (Final Result)

Step-by-Step Code Explanation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Initialize MPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from mpi4py import MPI
    import numpy as np

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

- `comm`: Communicator for all processes.
- `rank`: ID of this process (e.g., 0, 1, 2, ...).
- `size`: Total number of MPI processes.

Define Problem Size
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    N = 100
    chunk_size = N // size

Each process works on `chunk_size` elements.

Create Arrays on Root Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    if rank == 0:
        A = np.arange(N, dtype="float64")
        B = np.ones(N, dtype="float64")
    else:
        A = None
        B = None

- Rank 0 initializes full arrays.
- Other ranks set their arrays to `None`.

Allocate Buffers for Chunks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    A_chunk = np.empty(chunk_size, dtype="float64")
    B_chunk = np.empty(chunk_size, dtype="float64")
    C_chunk = np.empty(chunk_size, dtype="float64")

Each process creates local buffers to hold a portion of `A`, `B`, and the result `C`.

Distribute the Work (Scatter)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    comm.Scatter(A, A_chunk, root=0)
    comm.Scatter(B, B_chunk, root=0)

- Each process receives a chunk from `A` and `B`.

Example:

+------+------------------+------------------+
| Rank | Receives A_chunk | Receives B_chunk |
+======+==================+==================+
| 0    | A[0:25]          | B[0:25]          |
| 1    | A[25:50]         | B[25:50]         |
| ...  | ...              | ...              |
| 3    | A[75:100]        | B[75:100]        |
+------+------------------+------------------+

Perform Computation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    C_chunk = A_chunk + B_chunk

Each process performs element-wise addition of its own chunks.

Gather Results to Root
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    C = None
    if rank == 0:
        C = np.empty(N, dtype="float64")

    comm.Gather(C_chunk, C, root=0)

All partial results are gathered into `C` on the root process.

Print Final Result
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    if rank == 0:
        print("Result of A + B =", C)

Only the root process displays the full result.

Summary Table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Step
     - What Happens
     - MPI Function Used
   * - Init
     - Processes get rank and size
     - `COMM_WORLD`
   * - Setup
     - Root allocates full arrays
     - —
   * - Scatter
     - Arrays split to chunks
     - `Scatter`
   * - Compute
     - Local chunk computation
     - —
   * - Gather
     - Chunks reassembled on root
     - `Gather`
