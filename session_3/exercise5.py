# I have a program which has 30% parallelism and 70% serialism. What is speedup I can expect if I run it on
# - 4 cores
# - 8 cores
# Use Amdahl’s Law to calculate the speedup.

def amdahl(P, N):
    """
    Calculate Amdahl's Law
    """
    S = 1 / ((1-P) + (P/N))
    return f"Sa = {S:.2f}, P = {P:.0%}, N = {N}"

def gustafson(P, N):
    """
    Calculate Gustafson's Law
    """
    S = N - ((1-P) * (N-1))
    return f"Sg = {S:.2f}, P = {P:.0%}, N = {N}"


print(amdahl(0.3, 4))
print(amdahl(0.3, 8))

print(gustafson(0.3, 4))
print(gustafson(0.3, 8))