import matplotlib.pyplot as plt
import numpy as np

# You can use the keyword argument marker to emphasize each point with a specified marker

ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = 'o') # circle marker

# plt.plot(ypoints, marker = '*') # star marker

# marker|line|color

# plt.plot(ypoints, marker = 'D') # diamond marker

# plt.plot(ypoints, 'o:r') # circle marker with red color

# plt.plot(ypoints, 'o--m') # circle marker with magenta color and dashed line

# plt.plot(ypoints, marker = 'o', ms = 20) # circle marker with size 20

# You can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers:
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r') # circle marker with size 20 and red color (Markeredgecolor)

# You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers
# plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r') # circle marker with size 20 and red color (Markerfacecolor)

# Use both the mec and mfc arguments to color the entire marker:
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'g') # circle marker with size 20, red edge color and yellow face color

# plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50') # circle marker with size 20, hex color edge and face color

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink') # circle marker with size 20, named color edge and face color

plt.show()