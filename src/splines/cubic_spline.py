import math
import numpy as np
import matplotlib.pyplot as plt

x_i = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

y_i = []

for i in x_i:
    y_i.append(math.cos(2*i))

print("\n-------\n")

n = len(x_i)
h = x_i[1] - x_i[0]
A = [[0] * (n) for _ in range(n)]
F = [0] * (n)

A[0][0] = 1
A[-1][-1] = 1
F[0] = 0
F[-1] = 0

for i in range(1, n - 1):
        A[i][i-1] = h
        A[i][i] = 2*(h+h)
        A[i][i+1] = h

for i in range(1, n - 1):
    F[i] = 3*((y_i[i+1]-y_i[i])/h - (y_i[i]-y_i[i-1])/h)
            

matrix = [[0] * 4 for _ in range(n)]

for i in range(n):
    if i == 0:
        matrix[i][1] = A[i][i]
        matrix[i][2] = A[i][i+1]
        matrix[i][3] = F[i]
    elif i in range(1, n-1):
        matrix[i][0] = A[i][i-1]
        matrix[i][1] = A[i][i]
        matrix[i][2] = A[i][i+1]
        matrix[i][3] = F[i]
    else:
        matrix[i][0] = A[i][i-1]
        matrix[i][1] = A[i][i]
        matrix[i][3] = F[i]


for i in range(n):
    print(matrix[i])

print("\n-------\n")

alpha = [0] * n
gamma = [0] * n


for i in range(1, n):
    if i == 1:
        alpha[i] = -matrix[i - 1][2] / matrix[i - 1][1]
        gamma[i] = matrix[i - 1][3] / matrix[i - 1][1]
    elif i < n - 1:
        alpha[i] = -matrix[i - 1][2] / (matrix[i - 1][1] + matrix[i - 1][0] * alpha[i - 1])
        gamma[i] = (matrix[i - 1][3] - matrix[i - 1][0] * gamma[i - 1]) / (matrix[i - 1][1] + matrix[i - 1][0] * alpha[i - 1])
    else:
        alpha[i] = 0
        gamma[i] = (matrix[i - 1][3] - matrix[i - 1][0] * gamma[i - 1]) / (matrix[i - 1][1] + matrix[i - 1][0] * alpha[i - 1])

c_i = [0] * n
c_i[-1] = 0

for i in range(n-2, -1, -1):
    c_i[i] = alpha[i+1] * c_i[i+1] + gamma[i+1]

print(f"i |   alpha     |   gamma ")
print("--|-----------|----------")
for i in range(1, n):
    print(f"{i} | {round(alpha[i], 4):^9} | {round(gamma[i], 4):^9}")

print("\n")
print(f"i  |   c_i   ")
print("---|----------")
for i in range(n):
    print(f"{i}  |  {round(c_i[i], 4)}   ")

print("\n-------\n")

a_i = []
for i in range(n-1):
    a_i.append(y_i[i])

b_i = [0] * (n-1)
for i in range(n-1):
    b_i[i] = ((y_i[i+1]-y_i[i])/h - h/3*(c_i[i+1]+2*c_i[i]))

d_i = []
for i in range(n-1):
    d_i.append((c_i[i+1] - c_i[i]) / (3*h))

def function(a, b, c, d, x, x_i):
    return a + b * (x - x_i) + c * (x - x_i)**2 + d * (x - x_i)**3


plt.figure(figsize=(8, 5))
x_real = np.linspace(x_i[0], x_i[-1], 1000)
y_real = []
for i in x_real:
    y_real.append(math.cos(2*i))

plt.plot(x_real, y_real, color='black', label="f(x)")

my_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown', 'gray', 'pink', 'cyan', 'magenta',
             'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown', 'gray', 'pink', 'cyan', 'magenta']

for i in range(n - 1):
    x = np.linspace(x_i[i], x_i[i + 1], 100)
    y = []
    for j in x:
        y.append(function(a_i[i], b_i[i], c_i[i], d_i[i], j, x_i[i]))
    plt.plot(x, y, color=my_colors[i], label=f"Spline {i+1}", linestyle='--')

plt.scatter(x_i, y_i, color='red', zorder=5)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()