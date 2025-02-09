import matplotlib.pyplot as plt
import numpy as np

# Plotting with out lines
# To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()