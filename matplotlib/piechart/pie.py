import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

# As you can see the pie chart draws one piece (called a wedge) for each value in the array (in this case [35, 25, 25, 15]).
# By default the plotting of the first wedge starts from the x-axis and moves counterclockwise:

# Note: The size of each wedge is determined by comparing the value with all the other values, by using this formula:
# The value divided by the sum of all values: x/sum(x)

mylabels = ["Apples", "Bananas", "Cherries", "Dates"] # Add labels to the pie chart with the label parameter

#plt.pie(y) # pie chart

# plt.pie(y, labels = mylabels) # Add labels to the pie chart with the label parameter

# The startangle parameter is defined with an angle in degrees, default angle is 0
# 0 degrees = x-axis
# 90 degrees = y-axis
# 180 degrees = -x-axis
# 270 degrees = -y-axis
# As mentioned the default start angle is at the x-axis, but you can change the start angle by specifying a startangle parameter.

# plt.pie(y, labels = mylabels, startangle = 90) # Start the first wedge at 90 degrees (straight upwards)

myexplode = [0.2, 0, 0, 0] # Explode the pie chart to emphasize a value
# plt.pie(y, labels = mylabels, explode = myexplode) # Explode the pie chart to emphasize a value

# plt.pie(y, labels = mylabels, explode = myexplode, shadow = True) # Add a shadow to the pie chart

mycolors = ["black", "hotpink", "b", "#4CAF50"]
plt.pie(y, labels = mylabels, colors = mycolors) # Change the color of each wedge
plt.legend() # Add a legend
plt.legend(title = "Four Fruits:") # Add a title to the legend

plt.show() 