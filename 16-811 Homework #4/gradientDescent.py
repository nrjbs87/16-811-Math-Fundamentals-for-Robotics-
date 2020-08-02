import numpy as np
import matplotlib.pyplot as plt
import math

def fxy(x, y):
    return math.pow(x,3) + math.pow(y,3) - 2*math.pow(x,2) + 3*math.pow(y,2) - 8

def dfdx(x):
    return 3*math.pow(x,2) - (4 * x)

def dfdy(y):
    return 3*math.pow(y,2) + (6 * y)

x0 = 1
y0 = -1

# first iteration 
# find gradient
s1 = dfdx(x0)
s2 = dfdy(y0)

print(s1, s2)

n = 10000
d = np.linspace(-1, 1, n)
d = d.reshape(1, n)

xdd = np.zeros((1, n))
xdd = xdd.reshape(1, n)

ydd = np.zeros((1, n))
ydd = ydd.reshape(1, n)

fd = np.zeros((1, n))
fd = fd.reshape(1, n)

for i in range(n):
    xdd[0][i] = x0 + (d[0][i] * s1)
    ydd[0][i] = y0 + (d[0][i] * s2)
    fd[0][i] = fxy(xdd[0][i], ydd[0][i])

# for some reason we only pick minimum points that are greater than zero
# not really sure why...

mini = 100000
for i in range(n):
    if fd[0][i] < mini and fd[0][i] >= 0:
        mini = fd[0][i]
print(mini)


plt.plot(d[0], fd[0])
plt.xlabel('d')
plt.ylabel('f(d)')
plt.show()


