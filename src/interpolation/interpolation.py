import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from scipy.interpolate import KroghInterpolator as newton


x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

y = [0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    y[i] = (np.log10(3*x[i] - 2))

c = [0,0,0,0,0,0,0,0,0,0]
c[0] = 1 / ((x[0] - x[2]) * (x[0] - x[4]) * (x[0] - x[6]) * (x[0] - x[8]))
c[2] = 1 / ((x[2] - x[0]) * (x[2] - x[4]) * (x[2] - x[6]) * (x[2] - x[8]))
c[4] = 1 / ((x[4] - x[0]) * (x[4] - x[2]) * (x[4] - x[6]) * (x[4] - x[8]))
c[6] = 1 / ((x[6] - x[0]) * (x[6] - x[2]) * (x[6] - x[4]) * (x[6] - x[8]))
c[8] = 1 / ((x[8] - x[0]) * (x[8] - x[2]) * (x[8] - x[4]) * (x[8] - x[6]))


yc = [0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    yc[i] = c[i] * y[i]

l0 = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    l0[i] = yc[0] * (x[i] - x[2]) * (x[i] - x[4]) * (x[i] - x[6]) * (x[i] - x[8])

l1 = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    l1[i] = yc[2] * (x[i] - x[0]) * (x[i] - x[4]) * (x[i] - x[6]) * (x[i] - x[8])

l2 = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    l2[i] = yc[4] * (x[i] - x[0]) * (x[i] - x[2]) * (x[i] - x[6]) * (x[i] - x[8])

l3 = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    l3[i] = yc[6] * (x[i] - x[0]) * (x[i] - x[2]) * (x[i] - x[4]) * (x[i] - x[8])

l4 = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    l4[i] = yc[8] * (x[i] - x[0]) * (x[i] - x[2]) * (x[i] - x[4]) * (x[i] - x[6])

l = [0,0,0,0,0,0,0,0,0,0]

for i in range(10): 
    l[i] = l0[i] + l1[i] + l2[i] + l3[i] + l4[i]
    print(f"{x[i]:^4}| {y[i].round(3):^7}| {l[i].round(4)}")


h = 20

a = [10, 30, 50, 70, 90]

b = [0,0,0,0,0]

for i in range(5):
    b[i] = np.log10(3*a[i] - 2)

d_1 = [0,0,0,0]

for i in range(4):
    d_1[i] = b[i+1] - b[i]

d_2 = [0,0,0]

for i in range(3):
    d_2[i] = d_1[i+1] - d_1[i]

d_3 = [0,0]

for i in range(2):
    d_3[i] = d_2[i+1] - d_2[i]

d_4 = [0]

d_4[0] = d_3[1] - d_3[0]

a_set = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
b_set = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    b_set[i] = np.log10(3*a_set[i] - 2)

t = [0,0,0,0,0,0,0,0,0,0]

a_0 = 10

b_0 = np.log10(3*a_0 - 2)

for i in range(10):
    t[i] = (a_set[i] - a_0) / h

n_0 = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    n_0[i] = b_0

n_1 = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    n_1[i] = t[i] * d_1[0]

n_2 = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    n_2[i] = t[i] * (t[i] - 1) * d_2[0] / 2

n_3 = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    n_3[i] = t[i] * (t[i] - 1) * (t[i] - 2) * d_3[0] / 6

n_4 = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    n_4[i] = t[i] * (t[i] - 1) * (t[i] - 2) * (t[i] - 3) * d_4[0] / 24

n_n = [0,0,0,0,0,0,0,0,0,0]
for i in range(10): 
    n_n[i] = n_0[i] + n_1[i] + n_2[i] + n_3[i] + n_4[i]

print("------")
for i in range(10):
    print(f"{a_set[i]:^4} | {b_set[i].round(3):^7} | {l[i].round(4):^8} | {n_n[i].round(4):^8}")

print("------")

Lg = lagrange(a, b)
print("L = ", Lg)

Nt = newton(a, b)
coeffs_n = np.polyfit(a, b, len(a)-1)
Nt_poly = np.poly1d(coeffs_n)

print("------")

print("N = ")
print(Nt_poly)

print("------")
point_1 = 74
point_2 = 3

print(f"{point_1:^4}| {np.log10(3*point_1 - 2).round(4):^7} | {Lg(point_1).round(4):^7} | {Nt(point_1).round(4):^7}")
print(f"{point_2:^4}| {np.log10(3*point_2 - 2).round(4):^7} | {Lg(point_2).round(4):^7} | {Nt(point_2).round(4):^7}")

print("------")

plt.plot(x, y, color = 'red')
plt.plot(a_set, n_n, color = 'blue')
plt.plot(a_set, l, color = 'green')
plt.plot(a, b, color = 'none', marker = 'o', markerfacecolor = 'black')
plt.legend(['f(x)', 'N(x)', 'L(x)'])
plt.show()

a_set_s = np.linspace(10, 100, 1000)

b_set_s = []

for i in range(1000):
    b_set_s.append(np.log10(3*a_set_s[i] - 2))

lg_s = []
nt_s = []

for i in range(1000):
    lg_s.append(Lg(a_set_s[i]))
    nt_s.append(Nt(a_set_s[i]))


plt.plot(a_set_s, b_set_s, color = 'red')
plt.plot(a_set_s, lg_s, color = 'blue', linestyle = '--')
plt.plot(a_set_s, nt_s, color = 'green', linestyle = ':', linewidth = 3)
plt.plot(a, b, color = 'none', marker = 'o', markerfacecolor = 'black')
plt.legend(['f(x)', 'L(x)', 'N(x)'])
plt.show()

big_set = np.linspace(1, 200, 1000)

big_set_s = []

for i in range(1000):
    big_set_s.append(np.log10(3*big_set[i] - 2))

big_lg = []
big_nt = []

for i in range(1000):
    big_lg.append(Lg(big_set[i]))
    big_nt.append(Nt(big_set[i]))

fig, ax = plt.subplots()
ax.axhline(y = 0, color = 'black', linewidth = 3)
ax.axvline(x = 0, color = 'black', linewidth = 3)
plt.plot(big_set, big_set_s, color = 'red')
plt.plot(big_set, big_lg, color = 'blue', linestyle = '--')
plt.plot(big_set, big_nt, color = 'green', linestyle = ':', linewidth = 3)
plt.plot(a, b, color = 'none', marker = 'o', markerfacecolor = 'black')
plt.legend(['f(x)', 'L(x)', 'N(x)'])
plt.show()


# Different Lagrange: use reproducible, distinct nodes so the interpolation
# denominators cannot vanish because of duplicate random samples.
rng = np.random.default_rng(10)
x_d = np.sort(rng.choice(np.arange(10, 100), size=10, replace=False))
y_d = [0,0,0,0,0,0,0,0,0,0]

a_d = [x_d[0], x_d[2], x_d[4], x_d[6], x_d[8]]
b_d = [0,0,0,0,0]

for i in range(10):
    y_d[i] = np.log10(3*x_d[i] - 2)

for i in range(5):
    b_d[i] = np.log10(3*a_d[i] - 2)

c_d = [0,0,0,0,0,0,0,0,0,0]
c_d[0] = 1 / ((x_d[0] - x_d[2]) * (x_d[0] - x_d[4]) * (x_d[0] - x_d[6]) * (x_d[0] - x_d[8]))
c_d[2] = 1 / ((x_d[2] - x_d[0]) * (x_d[2] - x_d[4]) * (x_d[2] - x_d[6]) * (x_d[2] - x_d[8]))
c_d[4] = 1 / ((x_d[4] - x_d[0]) * (x_d[4] - x_d[2]) * (x_d[4] - x_d[6]) * (x_d[4] - x_d[8]))
c_d[6] = 1 / ((x_d[6] - x_d[0]) * (x_d[6] - x_d[2]) * (x_d[6] - x_d[4]) * (x_d[6] - x_d[8]))
c_d[8] = 1 / ((x_d[8] - x_d[0]) * (x_d[8] - x_d[2]) * (x_d[8] - x_d[4]) * (x_d[8] - x_d[6]))


yc_d = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    yc_d[i] = c_d[i] * y_d[i]


l0_d = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    l0_d[i] = yc_d[0] * (x_d[i] - x_d[2]) * (x_d[i] - x_d[4]) * (x_d[i] - x_d[6]) * (x_d[i] - x_d[8])


l1_d = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    l1_d[i] = yc_d[2] * (x_d[i] - x_d[0]) * (x_d[i] - x_d[4]) * (x_d[i] - x_d[6]) * (x_d[i] - x_d[8])

l2_d = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    l2_d[i] = yc_d[4] * (x_d[i] - x_d[0]) * (x_d[i] - x_d[2]) * (x_d[i] - x_d[6]) * (x_d[i] - x_d[8])


l3_d = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    l3_d[i] = yc_d[6] * (x_d[i] - x_d[0]) * (x_d[i] - x_d[2]) * (x_d[i] - x_d[4]) * (x_d[i] - x_d[8])

l4_d = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    l4_d[i] = yc_d[8] * (x_d[i] - x_d[0]) * (x_d[i] - x_d[2]) * (x_d[i] - x_d[4]) * (x_d[i] - x_d[6])

l_d = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    l_d[i] = l0_d[i] + l1_d[i] + l2_d[i] + l3_d[i] + l4_d[i]

Lg_d = lagrange(a_d, b_d)
print(x_d)
print("------")
print(Lg_d)

plt.plot(x, y, color = 'red')
plt.plot(a_set, n_n, color = 'blue')
plt.plot(a_set, l_d, color = 'green')
plt.plot(a, b, color = 'none', marker = 'o', markerfacecolor = 'black')
plt.legend(["f(x)", "N(x)", "L(x)"])
plt.show()

diff_l = []

for i in range(1000):
    diff_l.append(Lg_d(big_set[i]))

fig, ax = plt.subplots()
ax.axhline(y = 0, color = 'black', linewidth = 3)
ax.axvline(x = 0, color = 'black', linewidth = 3)
plt.plot(big_set, big_set_s, color = 'red')
plt.plot(big_set, big_lg, color = 'blue', linestyle = '--')
plt.plot(big_set, big_nt, color = 'green', linestyle = ':', linewidth = 3)
plt.plot(big_set, diff_l, color = 'purple', linestyle = '-.', linewidth = 2)
plt.plot(a, b, color = 'none', marker = 'o', markerfacecolor = 'black')
plt.legend(["f(x)", "L(x)_1", "N(x)", "L(x)_2"])
plt.show()
