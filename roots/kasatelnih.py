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

def f1(x):
    return 2 * x

def find_root(a, b, eps):
    if f(a) == 0:
        x = a
    elif f(b) == 0:
        x = b
    else:
        x0 = a
        while abs(x - x0) < eps:
            x = x0 - (f(x0) / f1(x0))
            x0 = x
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

X = np.linspace(a, b)
Y = f(X)
plt.plot(X, Y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('f(x)')
plt.grid()
plt.show()

def newton_method(a , b, step, e, N):
    lb = a
    while lb < b:
        if b - lb <= step:
            rb = b   
        else:
            rb = lb + step
        n = 0
        x0 = lb
        if f(lb) * f(rb) < 0:
            while (n < N):
                n += 1
                if f1(x0) == 0:
                    break
                else:
                    x1 = x0 - (f(x0) / f1(x0))
                    if not (lb < x1 < rb): 
                        break
                if abs(x1 - x0) < e:
                    break
                x0 = x1
            else:
                break
        if f(x0) == 0:
            n += 1
        lb += step