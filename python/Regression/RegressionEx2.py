import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

regr = linear_model.LinearRegression()  #선형 회귀 모델 객체 생성
x = [[164], [179], [162], [170]]    #키 데이터
y = [53, 63, 55, 59]    #몸무게 데이터
regr.fit(x, y)  #모델 학습

plt.scatter(x, y)   #산점도 그리기
y_pred = regr.predict(x)    #예측 수행

plt.plot(x, y_pred, color='blue', linewidth=3)  #회귀선 그리기
plt.show()