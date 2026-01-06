#아이리스 데이터
from sklearn.datasets import load_iris
iris = load_iris()

from sklearn.model_selection import train_test_split    #데이터를 훈련 및 테스트 세트로 분할
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score #분류 모델의 정확도 평가

iris.keys() #iris 데이터의 key 확인해보기
iris.data #iris 데이터의 Feature(입력변수)
iris.target #iris 데이터의 Label(출력데이터)
iris.feature_names  #feature_names(입력변수 각 이름) 확인하기
iris.target_names   #target_names(예측하려는 값(class)을 가진 문자열 배열) 확인하기
print(iris.DESCR)   #데이터셋의 설명