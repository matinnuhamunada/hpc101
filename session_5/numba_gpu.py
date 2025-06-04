import numpy as np
from numba import cuda
import math


# Device function
@cuda.jit(device=True)
def polar_to_cartesian(rho, theta):
    x = rho * math.cos(theta)
    y = rho * math.sin(theta)
    return x, y


# Kernel
@cuda.jit
def convert_kernel(rho, theta, x, y):
    idx = cuda.grid(1)
    if idx < rho.size:
        x[idx], y[idx] = polar_to_cartesian(rho[idx], theta[idx])


# Data size
n = 1024

# Host input data
rho_host = np.random.rand(n).astype(np.float32)
theta_host = np.random.rand(n).astype(np.float32)

# Copy to Data in the Host memory to GPU memory
rho_device = cuda.to_device(rho_host)
theta_device = cuda.to_device(theta_host)

# Create output arrays on GPU memory
x_device = cuda.device_array(n, dtype=np.float32)
y_device = cuda.device_array(n, dtype=np.float32)

# Run kernel
threads_per_block = 256
blocks_per_grid = (n + (threads_per_block - 1)) // threads_per_block
convert_kernel[blocks_per_grid, threads_per_block](
    rho_device, theta_device, x_device, y_device
)

# Copy back to host
x_host = x_device.copy_to_host()
y_host = y_device.copy_to_host()

# (Optional) print a few results
print("x:", x_host[:5])
print("y:", y_host[:5])
