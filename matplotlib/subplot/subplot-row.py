import matplotlib.pyplot as plt
import numpy as np

# Display Multiple Plots
# With the subplot() function you can draw multiple plots in one figure

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1) # 1 row, 2 columns, 1st plot
plt.plot(x,y)
plt.title("SALES") # Add a title to the plot

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2) # 1 row, 2 columns, 2nd plot
plt.plot(x,y)
plt.title("INCOME") # Add a title to the plot

plt.suptitle("MY SHOP") # Add a title to the entire figure (Supertitle)
plt.show()