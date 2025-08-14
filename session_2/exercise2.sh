module purge

# Check if there is a module named python3/3.12.1 available on Gadi.
module avail python3/3.12.1

# If available, load the module python3/3.12.1.
module load python3/3.12.1

# What happend when you try to load intel-mkl/2019.3.199 after loading python3/3.12.1
module load intel-mkl/2019.3.199
# conflict in dependencies