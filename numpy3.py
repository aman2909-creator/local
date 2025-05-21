# Given an array of integers from 1 to 20, filter out all even numbers greater than 10.

import numpy as np
a = np.arange(1,21)
b = a[(a%2==0) & (a>10)]
print(b)
