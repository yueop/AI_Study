import pandas as pd
import os

# 현재 파이썬 파일이 있는 폴더의 절대 경로를 계산
current_dir = os.path.dirname(os.path.abspath(__file__))

# 그 폴더 안에 있는 'data.csv'를 연결
file_path = os.path.join(current_dir, 'data.csv')
df = pd.read_csv(file_path, encoding='UTF-8')
print(df)