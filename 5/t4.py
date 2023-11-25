from sympy import *
import matplotlib.pyplot as plt
import numpy as np

x = symbols('x')
x0=oo
func = (7*(x**2)+7*x-2)/(x**2-2*x+3)
print (limit(func, x, x0))

# Data for plotting
# x = np.arange(-50, 50, 0.01)
# y = (7*(x**2)+7*x-2)/(x**2-2*x+3)

# fig, ax = plt.subplots()
# ax.plot(x,y)

# ax.set(xlabel='x', ylabel='y',
# title='xy Graph')
# ax.grid()

# plt.show()

x = np.arange(50, 500, 0.01)
y = (7*(x**2)+7*x-2)/(x**2-2*x+3)

fig, ax = plt.subplots()
ax.plot(x,y)

ax.set(xlabel='x', ylabel='y',
title='xy Graph')
ax.grid()

plt.show()