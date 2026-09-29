import matplotlib.pyplot as plt

ab = [0, 2]
h = 0.2
n = int((ab[1] - ab[0]) / h)
x = []
y = []

x_0 = ab[0]
x.append(x_0)
y_0 = 1
y.append(y_0)

def f_xy(x, y):
    return 0.4 * x ** 3 - 2 / y ** 2

for i in range(1, n + 1):
    x.append(ab[0] + i * h)
    y.append(y[i-1] + h * f_xy(x[i-1], y[i-1]))

#---------

k1 = []
k2 = []
k3 = []
k4 = []

y_k = [1]

for i in range(0, n):
    k1.append(h * f_xy(x[i], y_k[i]))
    k2.append(h * f_xy(x[i] + h / 2, y_k[i] + k1[i] / 2))
    k3.append(h * f_xy(x[i] + h / 2, y_k[i] + k2[i] / 2))
    k4.append(h * f_xy(x[i] + h, y_k[i] + k3[i]))
    y_k.append(y_k[i] + (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) / 6)


print("i  |   x   |     y     |   y_k  ")
print("---|-------|-----------|-----------")
for i in range(len(x)):
    print(f"{i:^2} | {round(x[i], 2):^5} |  {round(y[i], 4):^8} |  {round(y_k[i], 4):^5}")


plt.plot(x, y, label = "y(x), Euler", marker = 'o')
plt.plot(x, y_k, label = "y(x), Runge-Kutta(4)", marker = 'o')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid(linewidth = 0.2)
plt.hlines(0, ab[0], ab[1], color = 'gray')

plt.show()