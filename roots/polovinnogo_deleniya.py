import matplotlib as plt
from math import *

eps = float(input("eps = "))
a = float(input("a = "))
b = float(input("b = "))
step = float(input("step = "))
print("метод половинного деления")
print("отрезок [", a, ";", b,"] с точностью ", eps, "с шагом ", eps)
print("-----------------------------")

def f(x):
    return x * x - 2

def find_root(a, b, eps):
    while abs(a - b) > 2*eps:
        if f(a) == 0:
            x = a
        elif f(b) == 0:
            x = b
        else:
            x = (a + b) / 2
            if f(x) * f(a) <= 0:
                b = x
            else:
                a = x
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