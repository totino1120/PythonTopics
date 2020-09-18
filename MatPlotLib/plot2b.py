import matplotlib.pyplot as plt
import numpy as np
#
# fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(7, 7))
# print(type(ax))
# # <class 'numpy.ndarray'>
#
# print(ax)  # 2 x 2 array
# # [[<AxesSubplot:> <AxesSubplot:>]
# #  [<AxesSubplot:> <AxesSubplot:>]]
#
# #
# print(ax[0][1])
#
# # shape of array
# print(ax.shape)
#
# ax1, ax2, ax3, ax4 = ax.flatten()  # store each array in a sepa rate variable
#
fig1, ax1 = plt.subplots()  # figsize 640x480 default
print(f'fig1 id: {id(fig1)}')
print(f'gcf() id: {id(plt.gcf())}')  #gcf - get current figure returns fig1

fig2, ax2 = plt.subplots()  # figsize 640x480 default
print(f'fig2 == gcf: {id(fig2) == id(plt.gcf())}')  #gcf is now fig2, most recent fig.

# Note: Both figures are still existing
print(f'fignums: {plt.get_fignums()}')


def get_all_figures():
    return [plt.figure(i) for i in plt.get_fignums()]


print(f'figs before close:\n {get_all_figures()}')
plt.close('all')

print(f'figs after close:\n {get_all_figures()}')
