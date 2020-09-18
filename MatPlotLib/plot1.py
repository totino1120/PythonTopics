import matplotlib.pyplot as plt
import numpy as np

# uses seed to generate random numbers
np.random.seed(444)

rng = np.arange(50)
rnd = np.random.randint(0, 10, (3, rng.size))  # 3 arrays of rng.size (49) # y axis
yrs = 1950 + rng  # x axis

# print(rng)
# print(rnd)
print(rng+rnd)

#
fig, ax = plt.subplots(figsize=(5, 3))  # fig size on screen
ax.stackplot(yrs, rng+rnd, labels =['Eastasia', 'Eurasia', 'Oceania'])  #uses 1d array for x-axis values, 2d array to plot along y axis
ax.set_title('Combined debt growth over time')
ax.legend(loc='upper left')
ax.set_ylabel('Total debt')

ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])

fig.tight_layout()
plt.show()

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)  # nrows, ncols determine how many axes belong to the figure.