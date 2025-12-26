import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': ['a', 'b', 'c', 'd', 'e']
})

column_a1 = df.A
column_a2 = df['A']

print(column_a1)
print(column_a2)

columns_ab = df[['A', 'B']]

print(columns_ab)