# Create a 3x3 matrix of all 10s.
# Add a 1D array [1, 2, 3] to each row using broadcasting.

import numpy as np
a = np.ones((3,3))*10
print(a)
b = np.array([1,2,3])

print(a+b)