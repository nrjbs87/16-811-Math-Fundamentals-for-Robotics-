import numpy as np
import matplotlib as plt
import math


# implementing Euler's

np.set_printoptions(formatter={'float': lambda x: "{0:0.5f}".format(x)})

h = 0.05
n = 10
x0, y0 = 2, 1

table = np.zeros((n, 5))
table[0][1] = x0
table[0][2] = y0
table[0][3] = y0
for i in range(1, n):
    table[i][0] = i 
    table[i][1] = table[i-1][1] - h

for i in range(1, n):
    term  = math.pow((table[i-1][2]), 2)
    table[i][2] = table[i-1][2] - h * (1/ (3 * term))
    x = table[i][1]
    table[i][3] = math.pow(x-1, 1/3)
    table[i][4] = table[i][3] - table[i][2] 


print(table)