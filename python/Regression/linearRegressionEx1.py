import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([[2.1], [10], [3], [1], [3.5], [5], [8]], dtype=float)    #재배 면적
y = np.array([64.9, 292.6, 85.9, 30.92, 110.5, 163.4, 230.1], dtype=float)  #수확량

LR_model = LinearRegression()
LR_model.fit(x, y)

prd = LR_model.predict([[7], [12]])
print(prd)

plt.scatter(x, y, label='Train Data')
plt.scatter([7, 12], prd, marker='v', label='Predicted Data')
plt.show()