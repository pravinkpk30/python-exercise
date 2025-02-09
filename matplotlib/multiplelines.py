import matplotlib.pyplot as plt
import numpy as np

# Multiple Lines
# You can plot as many lines as you like by simply adding more plt.plot() functions:
# Draw a line in a diagram from position (1, 3) to (2, 8) and another line from position (6, 1) to (8, 10):

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()