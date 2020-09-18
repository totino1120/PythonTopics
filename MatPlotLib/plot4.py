import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable

x = np.diag(np.arange(2, 12))[::-1]  # 10x10 matrix flipped vertically
x[np.diag_indices_from(x[::-1])] = np.arange(2, 12)
x2 = np.arange(x.size).reshape(x.shape)

sides = ('left', 'right', 'top', 'bottom')
nolabels = {s: False for s in sides}  #interesting way of filling a dictionary
nolabels.update({'label%s' % s: False for s in sides}) #interesting way of appending and filling a dictionary

with plt.rc_context(rc={'axes.grid': False}):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
    ax1.matshow(x)
    img2 = ax2.matshow(x2, cmap='RdYlGn_r')  # returns an axes image object.
    for ax in (ax1, ax2):
        ax.tick_params(axis='both', which='both', **nolabels)  # **unpack dictionary

    for i, j in zip(*x.nonzero()):
        ax1.text(j, i, x[i, j], color='white', ha='center', va='center')

    divider = make_axes_locatable(ax2)
    cax = divider.append_axes('right', size='5%', pad=0)
    plt.colorbar(img2, cax=cax)
    fig.suptitle('Heatmaps with `Axes.matshow`', fontsize=16)

plt.show()
