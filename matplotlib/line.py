import matplotlib.pyplot as plt
import numpy as np

# If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.
# Draw a line in a diagram from position (1, 3) to position (8, 10):

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()