Graphical Processing Units (GPUs)
---------------------------------

GPUs are specialized hardware designed to handle parallel processing tasks efficiently. They consist of 
thousands of smaller cores that can perform many calculations simultaneously, making them ideal for tasks 
like graphics rendering and scientific computing. 

GPUs are particularly effective for data-parallel tasks, where the same operation is applied to many data
elements independently. This allows for significant speedups in applications such as machine learning,
image processing, and numerical simulations.

GPU vs CPU Memory
^^^^^^^^^^^^^^^^^^^^

GPUs have their own dedicated memory, known as **device memory** or **VRAM** (Video RAM), which is separate
from the system's main memory (RAM). This memory is optimized for high bandwidth and low latency, allowing
GPUs to access and process large datasets quickly. 

Data Transfer Between CPU and GPU
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Transferring data between the CPU and GPU is a crucial aspect of GPU programming. The CPU typically holds
the main application logic, while the GPU handles the computationally intensive tasks.

To utilize the GPU effectively, data must be transferred from the CPU's main memory to the GPU's device memory.
Typical data transfer flow:

1. Allocate memory on the GPU..
2. Copy data from CPU (host) to GPU (device).
3. Execute the GPU kernel.
4. Copy results back from GPU to CPU, if needed.

This transfer can be done using libraries like Numba, which provide functions to allocate memory on the GPU and
copy data between the CPU and GPU.