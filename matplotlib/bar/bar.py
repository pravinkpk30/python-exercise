import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

# The categories and their values represented by the first and second argument as arrays
# plt.bar(x,y) # Draw a bar chart. The bar() function takes arguments that describes the layout of the bars

# plt.barh(x, y) # Draw a horizontal bar chart. The barh() function takes arguments that describes the layout of the bars

plt.bar(x, y, color = "red") # Set the bar color to red

plt.bar(x, y, color = "hotpink") # Set the bar color to hotpink

plt.bar(x, y, color = "#4CAF50") # Set the bar color to green

plt.bar(x, y, width = 0.1) # Set the width of the bars to 0.1 (10%) The default width value is 0.8

# Note: For horizontal bars, use height instead of width.

plt.barh(x, y, color = "red", height=0.1) # Set the bar color to red and the height to 0.1 (10%) The default height value is 0.8

plt.show()