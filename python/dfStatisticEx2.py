import pandas as pd
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(cur_dir, 'data.xlsx')
df = pd.read_excel(file_path)

grouped_sum = df.groupby('반')['국어'].sum()
print(grouped_sum)

grouped_mean = df.groupby('반')['국어'].mean()
print(grouped_mean)

grouped_std = df.groupby('반')['국어'].std()
print(grouped_std)