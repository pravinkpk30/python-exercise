import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
# df = pd.DataFrame(data)

df = pd.DataFrame(data, index = ["day1", "day2", "day3"]) # With the index argument, you can name your own indexes.

print(df) 

# print(df.loc[0]) # This example returns a Pandas Series.

print(df.loc["day1"]) # This example returns a Pandas Series.

#use a list of indexes:
# print(df.loc[[0, 1]]) # Note: When using [], the result is a Pandas DataFrame.

print(df.loc[["day1", "day2"]]) # Note: When using [], the result is a Pandas DataFrame.