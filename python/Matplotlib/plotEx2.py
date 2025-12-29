import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data1.xlsx')

plt.plot(df['kor'], 'k--', marker='o')
plt.show()