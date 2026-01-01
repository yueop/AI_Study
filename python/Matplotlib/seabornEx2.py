import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

iris_data = pd.read_csv('iris.csv')
sns.scatterplot(x='petal_length', y='petal_width', hue='species', data=iris_data)
plt.title('Scatter Plot by seaborn', fontsize=20)
plt.show()