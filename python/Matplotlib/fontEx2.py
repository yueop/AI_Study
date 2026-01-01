import matplotlib.pyplot as plt

plt.rc('font', family='Gulim')
x = [1, 2, 3, 4]
y = [10, 4, 15, 9]
plt.plot(x, y, label='국어')
plt.title('그래프 예제')
plt.xlabel('번호')
plt.ylabel('점수')
plt.legend()
plt.show()