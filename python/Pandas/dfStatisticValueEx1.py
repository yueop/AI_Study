import pandas as pd

data = {
    'A': [1, 2, 3, 4, 5],
    'B': [6, 7, 8, 9, 10]
}

df = pd.DataFrame(data)

sum_A = df['A'].sum()   #칼럼 'A'의 합계 계산
print(f'sum of column A: {sum_A}')