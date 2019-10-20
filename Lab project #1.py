#THIS IS NOT WORKING YET
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import load_svmlight_file


#Provide the data
#No. of data: 252, #of features: 14
x_data, y_data= load_svmlight_file("bodyfat.txt")

x = x_data[:20]
y = y_data[:20]

#test data
x_test = x_data[20:30]

#Model creation and fitting
model =  LinearRegression()
model.fit (x,y)

#Results
r_sq = model.score (x,y)
print ("coefficient of determination: ", r_sq)
print ("intercept: ", model.intercept_) #when the value is 0
print ("slope: ", model.coef_)

#predictions
y_pred = model.predict(x_test)
print (y_pred)