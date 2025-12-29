import pandas as pd
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(cur_dir, 'data.xlsx')
df = pd.read_excel(file_path)

df2 = df.fillna({'확인여부':'완료'})    #데이터프레임(df)의 '확인여부' 컬럼의 결측치를 '완료'로 채움
print(df2)

df3 = df2.fillna(0)   #데이터프레임(df2)의 전체 칼럼에서 결측치를 0으로 채움
print(df3)