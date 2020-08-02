import numpy as np
import matplotlib as plt
import math

np.set_printoptions(formatter={'float': lambda x: "{0:0.5f}".format(x)})

def f(x):
    return math.pow((x-1), (1/3))

def f_deriv(y):
    a = 3 * math.pow(y, 2)
    return (1 / a)

h = -0.05
x, y = 2, 1
n = 10

table = np.zeros((n+4, 5))

table[0][0], table[1][0], table[2][0], table[3][0] = 0, 1, 2, 3
table[0][1], table[1][1], table[2][1], table[3][1] = 2.15, 2.10, 2.05, 2
table[0][2], table[1][2], table[2][2], table[3][2] = 1.04768955317165, 1.03228011545637, 1.01639635681485, 1
table[0][3], table[1][3], table[2][3], table[3][3] = f(table[0][1]), f(table[1][1]), f(table[2][1]), f(table[3][1])
table[0][4], table[1][4], table[2][4], table[3][4] = table[0][3] - table[0][2], table[1][3] - table[1][2], table[2][3] - table[2][2], table[3][3] - table[3][2]


for i in range(4, n+4):
    x += h
    table[i][0] = i-4
    table[i][1] = x
    table[i][3] = f(x)

    y = table[i-1][2]

    # again you made the same mistake. THIS EQUATION DOES NOT CARE ABOUT X
    # this is why we're only plugging in the y-components back into the eqn
    fn0 = f_deriv(table[i-1][2])
    fn1 = f_deriv(table[i-2][2])
    fn2 = f_deriv(table[i-3][2])
    fn3 = f_deriv(table[i-4][2])

    if i == 4: print(fn0, fn1, fn2, fn3, y)

    table[i][2] = y + (h/24) * (55*fn0 - 59*fn1 + 37*fn2 - 9*fn3)

    table[i][4] = table[i][3] - table[i][2]

 

  


    



print(table)

