#importing libraries
import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt

#importing dataset
data = pd.read_csv("linear_data.csv")

#converting columns to list
x = list(data['INCOME'].values)
y = list(data['PAYMENT'].values)

#x -> income & y -> payment

#calculating Mean
x_mean = st.mean(x)
y_mean = st.mean(y)
#print(income_mean, payment_mean)

#calculating X = x - x_mean & Y = y - y_mean
X = []
Y = []
for i in range(len(x)):
	X.append(x[i] - x_mean)
	Y.append(y[i] - y_mean)

#calculating (x - x_mean) * (y - y_mean) OR X * Y & (x - x_mean)^2 OR X_square
XY = []
X_square = []
for i in range(len(x)):
	XY.append(X[i] * Y[i])
	X_square.append(X[i] ** 2)

#calculating total XY and X_square
XY_sum = sum(XY)
X_square_sum = sum(X_square)

#printing data
print("\t x\t\t  y \t\t (x - x_mean)\t\t(y - y_mean)\t(x - x_mean)*(y - y_mean)\t(x - x_mean)^2")
print("_______________"*9)
for i in range(len(x)):
	print("\t{}\t\t {} \t\t{} \t\t{} \t\t{} \t\t {}".format(x[i], y[i], X[i], Y[i], XY[i], X_square[i]))

print()
print("X_mean =", x_mean)
print("Y_mean =", y_mean)
print("Sum of (x - x_mean)*(y - y_mean) = ", XY_sum)
print("Sum of (x - x_mean)^2 = ", X_square_sum)
print()

#calculating b1 and b0
b1 = XY_sum / X_square_sum
b0 = y_mean - (b1 * x_mean)

#calculating y_pred
y_pred = []
y_temp = 0
for i in range(len(x)):
	y_temp = (round(b1,2) * x[i]) + (round(b0,2))
	y_pred.append(y_temp)

#printing the linear regression
print("Linear Regression For The Given Data-Set Is Like This:\n")
print("\ty = ({} * x) + ({})".format(round(b1,2),round(b0,2)))

#printing y for a given x
x_inp = int(input("Enter a x value: "))
y_out = (b1 * x_inp) + (b0)
print("The Corresponding y value is = {}".format(round(y_out,2)))

# Visualizing the Results
plt.scatter(x, y, color = 'red')
plt.plot(x, y_pred, color = 'blue')
plt.title('INCOME VS PAYMENT')
plt.xlabel('INCOME')
plt.ylabel('PAYMENT')
plt.show()