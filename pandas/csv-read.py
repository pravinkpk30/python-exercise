import pandas as pd

print(pd.options.display.max_rows) # The max_rows option is used to limit the number of rows printed on the screen.

pd.options.display.max_rows = 9999 # Set the max_rows option to display all rows.

# If your data sets are stored in a file, Pandas can load them into a DataFrame.
# Load a CSV file into a DataFrame:
df = pd.read_csv('./assests/customers.csv')

# print(df.to_string()) # Tip: use to_string() to print the entire DataFrame.

# print(df.tail(5)) # By default, the head() method returns the top five rows of the DataFrame.

print(df) # By default, the head() method returns the top five rows of the DataFrame.