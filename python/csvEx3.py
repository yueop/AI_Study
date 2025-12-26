import pandas as pd

url = 'https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv'
df = pd.read_csv(url, delimiter='\t')
print(df)