import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model


coefs = []
# 30 observations
ols = linear_model.LinearRegression()


for i in range(100):
    # create nested array
    x = np.random.rand(30,2)
    y = x[:, 0] + 2*x[:,1] + np.random.rand(30)
    # train model
    ols.fit(x,y)
    coefs.append(ols.coef_)


data = np.random.rand(100,2)
# predictor
x = data[:, 1]
# response
# Y=x1+2*x2+μ
y = data[:, 0] + 2*data[:, 1] + np.random.rand(100)
x = x.reshape(-1,1)
ols.fit(x,y)
# how much of a change in y is explained by x
print("r2: %.3f" %ols.score(x,y))
# when x changes y changes this much
print("coef %.3f" %ols.coef_)
plt.scatter(x,y)
plt.plot(x, ols.predict(x.reshape(-1,1)), color='r')
plt.show()
