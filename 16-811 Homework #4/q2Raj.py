import numpy as np
import matplotlib.pyplot as plt
import math

def dxx(x, n):
    y = np.zeros((1, n))
    for i in range(0, n):
        X = x[i]
        y[0][i] = 3 * math.pow(X, 2) - (4 * X)
        
    return y

def dyy(x, n):
    y = np.zeros((1, n))
    for i in range(0, n):
        X = x[i]
        y[0][i] = 3 * math.pow(X, 2) + (6 * X)
        
    return y

n = 100

x1 = np.linspace(-3, 3, 100)
fx = x1.reshape(1, 100)
fx = dxx(x1, n)
plt.title("Partial f_x")

x2 = np.linspace(-3, 3, 100)
fy = x2.reshape(1,100)
fy = dyy(x2, n)
plt.title("Partial f_y")

plt.plot(x2, fy[0],color='b')
plt.show()

    