import numpy as np

n = 16
m = n/2
e = 10**(-5)

a = 0.23
b = 0.42

h = abs(b-a)/n

while True:
    s1 = 0
    for i in range(1, n, 2):
        s1 += np.cosh(a+(i)*h-2/(a+(i)*h))
    s2 = 0
    for i in range(2, n, 2):
        s2 += np.cosh(a+(i)*h-2/(a+(i)*h))
    i_h = (b-a)/(6*m)*(np.cosh(a-2/a) + 4*s1 + 2*s2 + np.cosh(b-2/b))

    n_new = n*2
    m_new = n_new/2
    h_new = abs(b-a)/n_new

    s1_new = 0
    for i in range(1, n_new, 2):
        s1_new += np.cosh(a+(i)*h_new-2/(a+(i)*h_new))
    s2_new = 0
    for i in range(2, n_new, 2):
        s2_new += np.cosh(a+(i)*h_new-2/(a+(i)*h_new))
    i_h_new = (b-a)/(6*m_new)*(np.cosh(a-2/a) + 4*s1_new + 2*s2_new + np.cosh(b-2/b))

    diff = abs(i_h - i_h_new)/(2**4 - 1)
    if diff < e:
        print("I =", i_h_new)
        print("h =", h_new)
        print("n =", n_new)
        break
    else:
        n = n_new
        m = m_new
        h = h_new