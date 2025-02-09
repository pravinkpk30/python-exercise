import pandas as pd

df = pd.read_json('./assests/data.json')

print(df.to_string()) 