# 데이터 전처리

## 목적

- 데이터 전처리는 데이터의 품질을 높이고 모델의 성능을 향상시키는 데 도움

## 작업

1. 데이터의 결측값(누락된 값) 처리
2. 데이터의 이상값 처리
3. 정규화 / 표준화(서로 다른 단위 또는 범위를 가진 데이터는 일정한 범위나 규모로 조정해야한다.)
4. 데이터의 축소
5. 데이터의 분리(데이터 셋의 데이터를 인공지능 모델의 훈련 데이터와 테스트 데이터로 분리하여 사용)

| 데이터 정제 | * 데이터 수집 과정에서 필요없는 데이터 제거
* 손실된 데이터 보정
* 결측값 채우기
* 이상값 제거 |
| --- | --- |
| 결측치
(최빈값, 평균값 등으로 대체하거나 제거해야함) | * 결측값: 비어있거나 누락된 값
* NA(Not Available의 약어, 사용하지 않는 값)
* NaN(Not a Number의 약어, 숫자가 아닌 데이터)
* Null: 아직 정해지지 않는 값으로 빈값 |
| 이상치
(범위를 벗어난, 비정상적으로 높거나 낮은 값) | * 정상값이 아닌 값
* 데이터 입력 오류
* 측정, 실험 오류
* 의도된 이상 |

## 결측치 탐색

- info() 함수 사용

```python
import pandas as pd
df = pd.read_csv('iris.csv')
df.info()

print(df.isnull().sum())
print(df.isna().sum())
```

## 결측치 처리

```python
import pandas as pd
import numpy as np

df = pd.read_excel('data.xlsx')
df.info()

print(df.isnull().sum())
print(df.isna().sum())

df.dropna(how='any')    #결측치가 하나라도 있는 행 삭제
df.fillna(0, inplace=True)  #결측치를 0으로 채우기
df.replace(np.nan, 0)  #결측치를 0으로 대체
```

-df.dropna(how=’any’): 결측치 포함 행 제거

-df.fillna(0, inplace=True): 결측치 채우기

-df.replace(np.nan, 0): 결측치 변경

## 중복값 처리

```python
import pandas as pd

df = pd.read_csv('iris.csv')
print(df[df.duplicated()])

df2 = df.drop_duplicates()
print(df2)
```

## 이상치 탐색

```python
import pandas as pd
import matplotlib.pyplot as plt

iris_data = pd.read_csv('iris.csv')
print(iris_data.describe())    #기초통계량 확인

iris_data.sort_values(by=['petal_length'], ascending=False) #petal_length 기준 내림차순 정렬

plt.scatter(x=iris_data['petal_length'], y=iris_data['petal_width'])    #산점도 그리기
plt.show()
```

-iris_data.describe(): 기초 통계량 사용

-iris_data.sort_values(): 정렬

-plt.scatter(), plt.show(): 산점도 그려 시각화

- 이상치 확인 및 정제 boxplot, IQR공식

```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

wine_load = load_wine()
wine = pd.DataFrame(wine_load.data, columns=wine_load.feature_names)
wine['Class'] = wine_load.target
wine['Class'] = wine['Class'].map({0: 'Class_0', 1: 'Class_1', 2: 'Class_2'})

import matplotlib.pyplot as plt
plt.boxplot(wine['color_intensity'], whis=1.5)
plt.title('color_intensity')
plt.show()
```

-wine[’Class’] = wine_load.target: 와인의 종류(0, 1, 2로 되어있는 정답지)를 DataFrame에 추가

-wine[’Class’] = wine[’Class’].map({0: ‘Class_0’, 1: ‘Class_1’, 2: ‘Class_2’}): .map()을 사용해 0, 1, 2라는 숫자를 Class_0, Class_1, Class_2라는 이름표로 바꿈

-plt.boxplot(wine[’color_intensity’], whis=1.5): 와인 데이터 표에서 ‘색상의 강도’ 열만 지정하여 그래프를 그림

-whis=1.5: 수염(Whiskers)의 길이를 결정하는 옵션. 상자의 위/아래 끝에서 IQR(상자 길이)의 1.5배만큼 떨어진 거리까지만 정상 범위(수염)로 인식 / 이 수염보다 바깥에 있는 점들은 이상치로 간주하여 동그라미로 따로 표시

## 이상치 처리

- 이상치 제거

```python
drop_outliers = wine.drop(index=outliers.index)
print('outliers: ', wine.shape)
print('drop_outliers: ', drop_outliers.shape)
```

- 이상치 대체

```python
wine.loc[outliers.index, 'color_intensity'] =wine['color_intensity'].dropna().mean()
print(wine.loc[outliers.index, 'color_intensity'])
```
