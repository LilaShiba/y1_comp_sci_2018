# supervised learning with decision tree
from sklearn import tree
# training set 
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
# correct output
labels = [0,0,1,1]
# classifer as function to produce code for correct output
# train classifier via decision tree aka box of rules
clf = tree.DecisionTreeClassifier()
# train 
clf = clf.fit(features, labels)
# print predictions
print(clf.predict([[150, 0]]))