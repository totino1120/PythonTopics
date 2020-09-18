import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(low=1, high=11, size=50)
y = x + np.random.randint(1, 5, size=x.size)
data = np.column_stack((x,y))

# print(data)

fig, (ax1, ax2) =  plt.subplots(nrows=1, ncols=2, figsize=(8,4))

ax1.scatter(x=x, y=y, marker='o', c='r', edgecolors='b' )  #marker = style of dot, c=color, edgecolor
ax1.set_title('Scatter: $x$ versus $y$')  # laytec
ax1.set_xlabel('$x$')
ax1.set_xlabel('$y$')
ax1.set_axisbelow(True)  # tells axes to diplay ticks and grids behind the points
ax1.grid(linestyle='--')  # enables grid with linestyle '--'  *see documentation

#----------------
ax2.hist(data, bins=np.arange(data.min(), data.max()), label=('x', 'y'))
ax2.legend(loc=(0))  # Renders lengend to avoid overlapping with bars on screen.
                     # can cause delays in rendering figure with large data.
ax2.set_title('Frequencies: $x$ versus $y$')
ax2.yaxis.tick_right()  # puts ticks on the right
ax2.set_axisbelow(True)
ax2.grid(linestyle='--')  # enables grid with linestyle '--'  *see documentation


plt.show()