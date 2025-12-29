import pandas as pd

df = pd.DataFrame({
    'Column1': [1, 2, 3, 4],
    'Column2': [5, 6, 7, 8]
})

#값 3을 300으로 변경
df.replace(3, 300, inplace=True)
print(df)