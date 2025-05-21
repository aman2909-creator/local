# Create a 3x3 NumPy array with values from 1 to 9.
# Reshape it into a 1D array.
# Then reverse the array using slicing.



import numpy as np
a = np.arange(1,10).reshape(3,3)
print(a)
b = a.reshape(-1)
print(b)
c =  b[::-1]
print(c)