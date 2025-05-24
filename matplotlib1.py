import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# fig , ax = plt.subplots()
# ax.plot([1,2,3,4],[1,4,2,3])
# plt.show()

# np.random.seed(12345)
# data = {'a': np.arange(50),'c': np.random.randint(0, 50, 50),'d': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100

# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# ax.scatter('a', 'b', c='c', s='d', data=data)
# ax.set_xlabel('entry a')
# ax.set_ylabel('entry b')
# plt.show()

# x = np.linspace(0,2,100)
# fig , ax = plt.subplots(figsize=(5,2.7),layout="constrained")
# ax.plot(x,x,label="Linear")
# ax.plot(x,x**2,label="quadratic")
# ax.plot(x,x**3,label="cubic")
# ax.set_xlabel('x_label')
# ax.set_ylabel('y_label')
# ax.set_title("simple plot")
# ax.legend(title="fuctions")
# plt.show()

# plt.figure(figsize=(5,2.7),layout="constrained")
# plt.plot(x,x,label="linear")
# plt.plot(x,x**2,label = "quadratic")
# plt.plot(x,x**3,label="cubic")
# plt.xlabel('x_label')
# plt.ylabel('y_label')
# plt.title("simple plot")
# plt.legend()
# plt.show()

# def my_plotter(ax,data1,data2,param_dict):
#     out = ax.plot(data1,data2,**param_dict)
#     return out

data1,data2,data3,data4 = np.random.randn(4,100)
# fig,(ax1,ax2) = plt.subplots(1,2,figsize=(5,2.7))
# my_plotter(ax1,data1,data2,{'marker':'x'})
# my_plotter(ax2,data3,data4,{'marker':'o'})
# plt.show()

# fig,ax = plt.subplots(figsize=(5,2.7))
# x = np.arange(len(data1))
# ax.plot(x,np.cumsum(data1),color="blue",linewidth=3,linestyle="--")
# l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)
# l.set_linestyle=":"

# fig, ax = plt.subplots(figsize=(5, 2.7))
# ax.scatter(data1, data2, s=50, facecolor='C0', edgecolor='k')
# plt.show()

fig, ax = plt.subplots(figsize=(5, 2.7))
ax.plot(data1, 'o', label='data1')
ax.plot(data2, 'd', label='data2')
ax.plot(data3, 'v', label='data3')
ax.plot(data4, 's', label='data4')
ax.legend()
plt.show()