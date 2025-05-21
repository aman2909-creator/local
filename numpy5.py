# Generate a 1000-element array of random numbers from a normal distribution (mean=0, std=1).
# Then:
# Find the mean and standard deviation of the array
# Count how many values fall between -1 and 1
import numpy as np
rng = np.random.default_rng()
a = rng.normal(size=1000)
print(a)
print(np.mean(a))
print(np.std(a))
b = np.sum((a>=-1)&(a<=1))
print(b)

