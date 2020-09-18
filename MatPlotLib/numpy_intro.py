import matplotlib.pyplot as plt
import numpy as np

# uses seed to generate random numbers
np.random.seed(20200914)

# creates a evenly spaced 1D array 0 (inclusive) to 6 (exclusive)
a = np.arange(6)  # similar to range (0, 6, 1)
print(f'arange(6):\n {a}')

b = np.arange(6, 10, 1)  # arange(start, stop, end)
print(f'arange(6, 10, 1):\n {b}')

c = np.random.randint(1, 10, (2, 4))  # create array shape (2 arrays or  4 each) with rand between 1 - 10  -
print(f'randint (1, 10, (2, 4)):\n {c}')

shape = c.shape  # attribute
print(f'shape:\n {shape}')  # shape of array 1,9

size = c.size  # attribute
print(f'size:\n {size}')  # No.Arrays * Size of Array  2*4

# reshapes an ndarray
d = c.reshape(4, 2)
print(f'reshape(4, 2):\n {d}')  #reshape to 4 arrays of size 2
print(f'reshape(1, 8):\n {c.reshape(1, 8)}')  #reshape to 1 arrays of size 8
print(f'reshape(8, 1):\n {c.reshape(8, 1)}')  #reshape to 4 arrays of size 2

# transpose an ndarray
e = d.T
print(f'transpose:\n {e}')  # shape(4,2) -> shape(2,4)

f = np.diag([1, 2, 3])
print(f'diag {f}')


# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.show()

# Object Hierarchy
# 1) Figure  # outermost window, can be resized.
# 1.1) Axes  # 1 or more Axes  # represents a single graphic (ie. histogram, scatterplot)
# 1.1.1) Axis  # 1 or more Axis  # x, y, title, points, tickmark, label.
# tickmark, label (belongs to) x or y axis (belongs to) Axes (belongs to) Figure

x = np.arange(0, 1, .1)
y = np.arange(10)
plt.title("pyplot demo")
plt.plot(x, y)
plt.show()

# pyplot is stateful

