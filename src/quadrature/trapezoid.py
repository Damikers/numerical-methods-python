import numpy as np

n = 19000

a = 0.23
b = 0.42

h = (b-a)/n

integral = 0

for i in range(n+1):
    if i == 0:
        integral += np.cosh(a-2/a)/2
    elif i == n:
        integral += np.cosh(b-2/b)/2
    else:
        integral += np.cosh(a+(i)*h-2/(a+(i)*h))
integral *= h

print("I =", integral)