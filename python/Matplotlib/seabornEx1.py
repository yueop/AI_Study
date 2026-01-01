import seaborn as sns
import pandas as pd

# 1. Seaborn에서 기본 제공하는 iris 데이터 로드
iris = sns.load_dataset('iris')

# 2. csv 파일로 저장
iris.to_csv('iris.csv', index=False)

print("iris.csv 파일이 생성되었습니다!")