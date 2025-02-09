import pandas as pd

df = pd.read_csv('./assests/new-data.csv')

print(df.corr())

print(df.to_string())