import numpy as np
import matplotlib.pyplot as plt
import math

fx = np.loadtxt(fname = 'problem2.txt')
fx = np.reshape(fx, (101,1))
x = np.linspace(0, 1, 101)
np.set_printoptions(formatter={'float': lambda x: "{0:0.6f}".format(x)})

def build_basis(n_lin, n_trig):
    basis = np.zeros((101, n_lin + n_trig))

    for i in range(0, n_lin + 1):
        for j in range(0, 101):
            basis[j][i] = math.pow(x[j], i)

    for i in range(n_lin,basis.shape[1]):
        for j in range(0, 101):
            basis[j][i] = math.sin((i + 1 - n_lin) *math.pi*(x[j])) 

    return basis

def get_coefficients(basis,fx):
    return np.matmul(np.linalg.pinv(basis),fx)

def get_error(basis, coeff, values):
    return np.linalg.norm(np.matmul(basis,coeff) - values)

num_linear_terms = 10
num_trig_terms = 10

min_error = 0.0001
actual_coeff = []

for i in range(1, num_linear_terms):
    for j in range(1, num_trig_terms):
        basis = build_basis(i, j)
        coeff = get_coefficients(basis,fx)
        error = get_error(basis, coeff, fx)
        if error < min_error: 
            min_error = error
            actual_coeff = coeff
            actual_basis = basis

print(actual_coeff)
reconstructed_func = np.matmul(actual_basis, actual_coeff)
plt.plot(x, reconstructed_func)
plt.show()
