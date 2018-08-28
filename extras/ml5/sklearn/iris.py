import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
import pydotplus


iris = load_iris()
print("flower name: %s target name %s and iris data %s"%(iris.feature_names, iris.target_names, iris.data[0]))


# testing data to see how accurate our classifier is
# remove one of each label
test_idx = [0,50,100]

# remove test data from training set
# training set
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

# classifier
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print(test_target)
print(clf.predict(test_data))

# VISUALISE THE TREE

# non-coloured version
# dot_data = tree.export_graphviz(clf, out_file=None)
# graph = pydotplus.graph_from_dot_data(dot_data)
# graph.write_pdf("iris.pdf")

dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=iris.feature_names,
                                class_names=iris.target_names,
                                filled=True, rounded=True,
                                special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf("irisColoured.pdf")
