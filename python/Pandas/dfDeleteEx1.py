import pandas as pd

df = pd.DataFrame({
    'Column1': [1, 2, 3, 4],
    'Column2': [5, 6, 7, 8]
})

df.drop(index=1, axis=0,inplace=True)  # 인덱스 1에 해당하는 행 삭제
print(df)