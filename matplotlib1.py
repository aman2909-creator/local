import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# fig , ax = plt.subplots()
# ax.plot([1,2,3,4],[1,4,2,3])
# plt.show()

np.random.seed(12345)
data = {'a': np.arange(50),'c': np.random.randint(0, 50, 50),'d': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')
plt.show()