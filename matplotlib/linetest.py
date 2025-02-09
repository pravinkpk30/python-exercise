import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

# You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line

# plt.plot(ypoints, linestyle = 'dotted') # dotted line

# plt.plot(ypoints, linestyle = 'dashed') # dashed line

# The line style can be written in a shorter syntax:
# linestyle can be written as ls.
# dotted can be written as :.
# dashed can be written as --.

# plt.plot(ypoints, ls = ':') # dotted line

# plt.plot(ypoints, color = 'r') # red line

# plt.plot(ypoints, c = '#4CAF50') # hex color

# plt.plot(ypoints, c = 'hotpink') # named color

# plt.plot(ypoints, linewidth = '20.5') # line width

# Multiple lines - You can plot as many lines as you like by simply adding more plt.plot() functions

y1 = np.array([3, 8, 1, 10]) 
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

# another approach - Draw two lines by specifiyng the x- and y-point values for both lines
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2) # x1, y1, x2, y2 are the x- and y-point values for both lines


plt.show()