import pandas as pd
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(cur_dir, 'data.xlsx')
df = pd.read_excel(file_path)

print(df.head(3))
print(df.tail(3))

print(df.info)