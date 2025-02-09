import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./assests/new-data.csv')

df.plot() # Pandas uses the plot() method to create diagrams.

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories') # scatter plot with good coorelation

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse') # scatter plot with bad coorelation

df["Duration"].plot(kind = 'hist') # Histogram: It is used to represent the frequency of data distribution in the graphical format.

plt.show()