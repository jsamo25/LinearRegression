#THIS IS NOT WORKING YET
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import load_svmlight_file

#Provide the data
#No. of data: 252, #of features: 14
X, Y= load_svmlight_file("abalone.txt") #bodyfat, abalone, cadata
reg = LinearRegression()

print(X)

# i = 0
# N = 30
#
# while i < len(Y):
#     x_train = X[i:(N+i)]
#     y_train = Y[i:(N+i)]
#
#     reg = reg.fit (x_train, y_train)
#     y_pred = reg.predict(x_train)
#     #rmse = np.sqrt(mean_squared_error(y_train, y_pred))
#     rmse = mean_squared_error(y_train, y_pred)
#     plt.scatter (i, rmse)
#     i += N
#
# plt.grid(True)
# plt.xlabel("Number of samples")
# plt.ylabel("Mean Squared error")
# plt.show()
# print (len(Y))
#reg = reg.fit(X,Y)
#Y_pred = reg.predict(X)

#errors
#rmse = np.sqrt(mean_squared_error(Y, Y_pred))
#r2_score = reg.score(X,Y)

