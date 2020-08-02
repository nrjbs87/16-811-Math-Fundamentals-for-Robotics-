import numpy as np
import matplotlib as plt
import math

np.set_printoptions(formatter={'float': lambda x: "{0:0.5f}".format(x)})

# implementing Runge Kutta to the fourth degree
# remember in this specific equation, there is no x term
# so we only need to pass our function the y term


def f(x):
    return math.pow((x-1), (1/3))

def f_deriv(y):
    a = 3 * math.pow(y, 2)
    return (1 / a)

h = -0.05
x, y = 2, 1
n = 20

table = np.zeros((n, 5))
table[0][0] = 0
table[0][1] = x
table[0][2] = y
table[0][3] = y
table[0][4] = 0

for i in range(1, n):
    k1 = h * f_deriv(y)
    k2 = h * f_deriv(y + (k1/2))
    k3 = h * f_deriv(y + (k2/2))
    k4 = h * f_deriv(y + k3)
    y = y + (k1 + 2*k2 + 2*k3 + k4)/6
    x = round(x + h, 2)
    table[i][0] = i
    table[i][1] = x
    table[i][2] = y
    table[i][3] = f(x)
    table[i][4] = table[i][3] - table[i][2]
    

print(table)

    
    
