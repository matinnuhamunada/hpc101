# I have a program which has 30% parallelism and 70% serialism. What is speedup I can expect if I run it on
# - 4 cores
# - 8 cores
# Use Amdahl’s Law to calculate the speedup.

P = 0.3
N = 4
S = 1 / ((1-P) + (P/N))

print(S, P, N)

N = 8
print(S, P, N)