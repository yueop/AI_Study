import pandas as pd
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(cur_dir, 'data.xlsx')
df = pd.read_excel(file_path)

df2 = df.dropna(subset=['응시여부']) #데이터프레임의 '응시여부' 칼럼에서 결측치가 있는 행 제거
print(df2)

df3 = df.dropna()
print(df3) #데이터프레임의 모든 칼럼에서 결측치가 있는 행 제거