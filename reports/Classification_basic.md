# 분류

## 분류 모델을 생성하는 절차

- 문제 정의하기: 붓꽃의 종류는 어떤 특성에 따라 구분할 수 있습니까?,

                                  붓꽃의 종류를 예측할 수 있는 모델을 개발할 수 있습니까?

- 데이터 불러오기: 사이킷런(sklearn)의 iris 데이터셋 불러오기
- 데이터 처리하기: 데이터셋을 살펴보고, 학습에 적합한 형태로 변형, 가공
- 모델 학습하기: 데이터의 특징을 파악하여 알맞은 머신러닝 알고리즘 선택 및 학습
- 모델 테스트 및 평가: 테스트 데이터로 평가하기

## 문제 정의

- 붓꽃 품종을 분류할 수 있을까?
- 아이리스 품종
    - 꽃은 꽃잎(Petal)과 꽂받침(Sepal)으로 이루어져 있고, 품종에 따라 꽃잎과 꽃받침의 길이, 폭이 다르다.
    - 예를 들어, 붓꽃 데이터 세트에서 붓꽃을 세 가지 품종(Setosa, Versicolor, Virginicca)으로 분류하는 것이 있다.

## 데이터 불러오기

- Iris 데이터 불러오기

```python
#아이리스 데이터
from sklearn.datasets import load_iris
iris = load_iris()
```

- 필요한 라이브러리 불러오기

```python
from sklearn.model_selection import train_test_split    #데이터를 훈련 및 테스트 세트로 분할
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score #분류 모델의 정확도 평가
```

- 데이터 확인

```python
iris.keys() #iris 데이터의 key 확인해보기
iris.data #iris 데이터의 Feature(입력변수)
iris.target #iris 데이터의 Label(출력데이터)
iris.feature_names  #feature_names(입력변수 각 이름) 확인하기
iris.target_names   #target_names(예측하려는 값(class)을 가진 문자열 배열) 확인하기
print(iris.DESCR)   #데이터셋의 설명
```

- 데이터프레임에 아이리스 데이터 담기

```python
import pandas as pd
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df.head()
```

- 꽃잎 길이, 꽃잎 너비만 추출하여 iris_petal에 저장

```python
iris_petal = iris.data[:, [2,3]]
print(iris_petal)
```

## 데이터 처리하기

- 데이터 크기 확인

iris_df.shape

- 데이터프레임에 label 칼럼 추가하기

```python
iris_df["label"] = iris.target
iris_df.head()
```

- train_test_split 함수를 사용하여 데이터 셋을 훈련(train) 셋과 테스틑(test)셋으로 분할

```python
X_train, X_test, Y_train, Y_test = train_test_split(iris.data, #input data(feature)
                                                    iris.target, #output data(label or target)
                                                    test_size = 0.2,
                                                    random_state= 7)
print('X_train 개수: ', len(X_train), 'X_test 개수: ', len(X_test))
```

-test_size=0.2: 테스트 셋 20% 훈련 셋 80%로 지정하는 매개변수

-random_state=7: 데이터 셋을 섞을 때 int값이 고정된 시드값으로 나오도록하여 데이터 셋이 계속해서 변경되는 것을 방지(실행할 때마다 동일한 결과를 얻음).

### 시각화

- 특성 간에 상관 관계를 확인하기 위해 산점도로 시각화

```python
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10, 10))
sns.pairplot(iris_df, hue='label', palette='bright') #모든 변수 쌍에 대한 산점도 그리기
plt.show()
```

## 모델 생성 및 학습하기

- 결정트리(Decision Tree) 알고리즘 모델 생성

```python
#결정트리 알고리즘 모델 생성
dt_model = DecisionTreeClassifier(random_state=32)
dt_model.fit(X_train, Y_train)  #학습하기
```

-fit: 학습 명령

## 예측 및 정확도 계산

- 테스트 세트를 이용한 예측하기

```python
y_pred = dt_model.predict(X_test)
print(y_pred)
print(Y_test)   #정답 비교
```

-모델 별 성능 평가 지표

```python
from sklearn.metrics import classification_report
print(classification_report(Y_test, y_pred))
```

- 정확도 계산하기

print("정확도: ", accuracy_score(Y_test, y_pred))

$$
정확도 = \frac{예측한 전체 데이터의 개수}{예측결과가 정답인 데이터의 개수}
$$

-precision: 정밀도

-recall: 재현율

-f1-score: 정밀도와 재현율의 조화평균

-support: 각 클래스 별로 분류(각 클래스 별로 데이터가 몇개 씩 있었는지 출력)
