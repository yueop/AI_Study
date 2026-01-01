import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data1.xlsx')
plt.rc('font', family='Gulim')
plt.plot(df['name'], df['kor'], 'g--', marker='o', label='국어점수')
plt.plot(df['name'], df['math'], 'r', marker='v', label='수학점수')
plt.title('성적 그래프')
plt.xlabel('이름')
plt.ylabel('점수')
plt.legend()
plt.show()