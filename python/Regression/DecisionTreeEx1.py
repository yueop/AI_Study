from sklearn import tree

parents_height = [[180,165], [175,160], [180,172], [165,160], [171,152]]
child_height = [3,2,2,1,1]

dt = tree.DecisionTreeClassifier()
dt.fit(parents_height, child_height)

prd = dt.predict([[175,153]])
print(prd)