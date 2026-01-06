import numpy as np
from sklearn import linear_model

regr = linear_model.LinearRegression()  #선형 회귀 모델 객체 생성
x = [[164], [179], [162], [170]]    #키 데이터
y = [53, 63, 55, 59]    #몸무게 데이터
regr.fit(x, y)  #모델 학습

score = regr.score(x, y)
print("The score of this line for the data: ", score)

input_data = [[180], [185]] #예측에 사용할 키 데이터
result = regr.predict(input_data)   #예측 수행
print(result)