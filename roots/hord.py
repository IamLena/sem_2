import matplotlib.pyplot as plt
import numpy as np
from math import *

eps = float(input("eps = "))
a = float(input("a = "))
b = float(input("b = "))
step = float(input("step = "))
print("метод половинного деления")
print("отрезок [", a, ";", b,"] с точностью ", eps, "с шагом ", eps)
print("-----------------------------")

#вершины и концы отрезков

def f(x):
    return x * x - 3
def find_root(a, b, eps):
    if f(a) == 0:
        x = a
    elif f(b) == 0:
        x = b
    else:
        lb = a
        rb = b
        x = x = lb - (rb - lb)*f(lb)/(f(rb) - f(lb))

        while (abs(lb - x) > eps and abs(rb - x) > eps):
            x = lb - (rb - lb)*f(lb)/(f(rb) - f(lb))
            if f(x) * f(lb) <= 0:
                rb = x
            else:
                lb = x
    return x

def solve(a, b, eps, step):
    while (a < b):
        if f(a) * f(a + step) <= 0:
            print(a, a+step, "интервал ", end = '')
            x = find_root (a, a + step, eps)
            print("корень - {:.4f} ".format(x), end = '')
            print("значение функции - {:.1e}".format(f(x)))
        a += step
    if a != b:
        find_root (a, b, eps)

solve(a, b, eps, step)

def zero(x):
    return 0

X = np.linspace(a, b)
Y = f(X)
plt.plot(X, Y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('f(x)')
plt.grid()
plt.show()