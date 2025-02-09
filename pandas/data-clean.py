import pandas as pd

df = pd.read_csv('./assests/customers.csv')

# new_df = df.dropna() # Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

df.dropna(inplace = True) # Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.

# print(new_df.to_string())

df.fillna(130, inplace = True) # Note: The fillna() method allows us to replace any NULL values with the value we specify.

df["Calories"].fillna(130, inplace = True) # To only replace empty values for one column, specify the column name for the DataFrame

# Replace Using Mean, Median, or Mode

x = df["Calories"].mean() # Mean = the average value (the sum of all values divided by number of values).

df["Calories"].fillna(x, inplace = True) 

x = df["Calories"].median() # Median = the value in the middle, after you have sorted all values ascending.

df["Calories"].fillna(x, inplace = True)

x = df["Calories"].mode()[0] # Mode = the value that appears most frequently.

df["Calories"].fillna(x, inplace = True)

# Cleaning Data of Wrong Format

df['Date'] = pd.to_datetime(df['Date']) # Pandas will try to guess the format of your dates when converting them, but it is always good to specify the format.

df.dropna(subset=['Date'], inplace = True) # Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.

# Cleaning Wrong data

# Replacing Values

# it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7

df.loc[7, 'Duration'] = 45 # For small data sets you might be able to replace the wrong data one by one

# To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

# Removing Rows

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

print(df.duplicated()) # The duplicated() method returns a Boolean values for each row: True if a row is a duplicate, otherwise False.

# Remember: The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.
df.drop_duplicates(inplace = True) # The drop_duplicates() method removes duplicates.


print(df.to_string())