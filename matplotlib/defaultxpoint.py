import matplotlib.pyplot as plt
import numpy as np

# Default X-Points
# If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 etc., depending on the length of the y-points.
# So, if we take the same example as multiplelines.py, and leave out the x-points, the diagram will look like this:
# The x-points in the example above are [0, 1, 2, 3, 4, 5]. The y-points are [3, 8, 1, 10, 5, 7].

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()