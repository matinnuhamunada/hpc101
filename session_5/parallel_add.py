from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Length of the full array
N = 100

# Each process handles a chunk of the array
chunk_size = N // size

# Create arrays only on root
if rank == 0:
    A = np.arange(N, dtype="float64")
    B = np.ones(N, dtype="float64")
else:
    A = None
    B = None

# Create buffers for each chunk
A_chunk = np.empty(chunk_size, dtype="float64")
B_chunk = np.empty(chunk_size, dtype="float64")
C_chunk = np.empty(chunk_size, dtype="float64")

# Scatter the arrays to all processes
comm.Scatter(A, A_chunk, root=0)
comm.Scatter(B, B_chunk, root=0)

# Each process performs addition on its chunk
C_chunk = A_chunk + B_chunk

# Gather the result back to the root
C = None
if rank == 0:
    C = np.empty(N, dtype="float64")

comm.Gather(C_chunk, C, root=0)

# Print result on root
if rank == 0:
    print("Result of A + B =", C)
