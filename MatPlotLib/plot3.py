import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import tarfile
from urllib.request import urlopen


url = 'https://ndownloader.figshare.com/files/5976036'
b = BytesIO(urlopen(url).read())  # open URL as a sequence of bytes
fpath = 'CaliforniaHousing/cal_housing.data'  # path within the extracted directory

with tarfile.open(mode='r', fileobj=b) as archive:
    housing = np.loadtxt(archive.extractfile(fpath), delimiter=',')  # turn into ndarray

    value = housing[:, -1]  # get the last element in the line
    pop, age = housing[:, [4, 7]].T  # get element 4 and 7 and transpose

    value2, pop2, age2 = housing[:, [-1, 4, 7]].T  # get element 4 and 7 and transpose

    # print(f'value: {value}')
    # # print(f'housing: {housing[:, [4, 7]]}')
    # print(f'pop: {pop}')


def add_innerbox(ax, text):  # will create label inside box vs title area
    ax.text(.55, .8, text,
            horizontalalignment='center',
            transform=ax.transAxes,  # MAKES COORDINATES (TEXT?) RELATIVE TO BOUNDS OF AXES
            bbox=dict(facecolor='white', alpha=0.6),  # OPACITY (ALPHA CHANNEL)
            fontsize=12.5)


# GOING TO USE A 3X2 GRID AND USE TOP (1,1;1,2;2,1;2,2), (3,1), (3,2)
gridsize = (3, 2)
fig = plt.figure(figsize=(12, 8))  # create figure 4x grid size
ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=2, rowspan=2)
ax2 = plt.subplot2grid(gridsize, (2, 0))
ax3 = plt.subplot2grid(gridsize, (2, 1))

ax1.set_title('Home value as a function of home age (x) & area population (y)', fontsize=14)
sctr = ax1.scatter(x=age2, y=pop2, c=value2, cmap='RdYlGn')  # returns a collection that we can use to set the colorbar
plt.colorbar(sctr, ax=ax1, format='$%d')  # $integer
ax1.set_yscale('log')

ax2.hist(age, bins='auto')
ax3.hist(pop, bins='auto', log=True)

add_innerbox(ax2, 'Histogram: home age')
add_innerbox(ax3, 'Histogram: area population (log scl.)')

plt.show()


