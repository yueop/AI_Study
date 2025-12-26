import pandas as pd
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(cur_dir, 'data.csv')

df = pd.read_csv(file_path, index_col=0)
print(df)