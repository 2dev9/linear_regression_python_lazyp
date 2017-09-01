import numpy as np
import matplotlib.pyplot as plt

#load data
X = []
Y = []
for line in open('data_1d.csv'):
	x, y = line.split(',')
	X.append(float(x))
	Y.append(float(x))

#convert lists into numpy arrays
X = np.array(X)
Y = np.array(Y)

#plot the data
plt.scatter(X,Y)
plt.show()

#apply the equations to calculate a and b
#the denominator and numerator were mutliplied by n

#equivalent to denominator = np.mean(X**2) - np.mean(X) **2
denominator = X.dot(X) - X.mean() * X.sum()


a =  (X.dot(Y) - Y.mean()  * X.sum())/ denominator
b = (Y.mean() * X.dot(X) - X.mean() * X.dot(Y))/denominator

#calculate predicted y
Yhat = a*X + b

#plot it all
plt.scatter(X,Y)
plt.plot(X,Yhat)
plt.show()
