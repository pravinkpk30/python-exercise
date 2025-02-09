import matplotlib.pyplot as plt
import numpy as np

# You can combine a colormap with different sizes of the dots. This is best visualized if the dots are transparent

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100)) # color of the dots
sizes = 10 * np.random.randint(100, size=(100)) # size of the dots

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral') # scatter plot

plt.colorbar() # Add a colorbar to the plot

plt.show()