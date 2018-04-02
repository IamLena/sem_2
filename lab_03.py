# lab_03

from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (x - 2)**2 - 2
    #return x ** 3 - 8
    #return 3 * x - 3
    #return (x)**2-16

#f1 - производная f(x)
def f1(x):
    return 2 *(x-2)
    #return 3* x **2
    #return 3
    #return 2*(x)

a = b = 0
R = []

def graf():
##    global a
##    global b
##    global R
    X = np.linspace(a, b)
    Y = f(X)

    plt.plot(X, Y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('f(x)')
    plt.grid()
    plt.show()
    
def clear():
    M = []
    R = []
    A.delete(0, END)
    B.delete(0, END)
    h.delete(0, END)
    eps.delete(0, END)
    m.delete(0, END)

    num_1.delete(0, END)
    interval_1.delete(0, END)
    root_1.delete(0, END)
    f_1.delete(0, END)
    n_1.delete(0, END)
    error_1.delete(0, END)



def correct(a):
    if a == '':
        print("Некорректный ввод")
        return False
    else:
        x = a
        if x[0] == '-':
            x = x[1:]
        d = x.find('.')
        if d != -1:
            x = x[:d] + x[d+1:]
        if x.isdigit():
            print(a)
            return a
        else:
            print("Некорректный ввод")
            return False
        
def solve():
    global a
    global b
    a = A.get()
    if not correct(a):
        return
    else:
        a = float(a)
    
    b = B.get()
    if not correct(b):
        return
    else:
        b = float(b)
    
    step = h.get()
    if step == '':
        print("Некорректный ввод")
        return
    else:
        if correct(step) and float(step) > 0:
            step = float(step)
            print(step)
        else:
            print("Некорректный ввод")
            return
        
    e = eps.get()
    if e == '':
        print("Некорректный ввод")
        return
    else:
        d = e.find('.')
        if d!= -1:
            x = e[:d]+e[d+1:]
        if x.isdigit():
            e = float(e)
            if 0 < e < 1:
                print(e)
            else:
                print("Некрректный ввод")
                return
        else:
            print("Некрректный ввод")
            return

    N = m.get()
    if N == '':
        print("Некорректный ввод")
        return
    else:
        if N.isdigit():
            N = int(N)
            print(N)
        else:
            print("Некорректный ввод")
            return
        
    newtons_method(a , b, step, e, N)

def newtons_method(a , b, step, e, N):
    R = []
    M = []
    lb = a
    while lb < b and lb + step <= b:
        print("промежуток", lb, lb + step)
        n = 0
        x0 = lb
        if f(lb) * f(lb + step) <= 0:
            if f(lb) != 0:
                M.append("1")
                number = len(M)
                interval_1.insert(END,  "({:.3f}, {:.3f})".format(lb, lb + step))
                interval_1.insert(END, "-----------------")
                while (n < N):
                    n += 1
                    if f1(x0) == 0:
                        print("производная ноль")
                        num_1.insert(END, "{:d}".format(number) )
                        num_1.insert(END, "-----------------")
                        root_1.insert(END, "???")
                        root_1.insert(END, "-----------------")
                        f_1.insert(END, "???")
                        f_1.insert(END, "-----------------")
                        n_1.insert(END, "{:d}".format(n))
                        n_1.insert(END, "----------------" )
                        error_1.insert(END, "3")
                        error_1.insert(END, "----------------")

                        break
                    else:
                        x1 = x0 - (f(x0) / f1(x0))
                        print(x1)
                        if abs(x1 - x0) < e:
                            R.append(x1)
                            print(R)
                            print("Точность достигнута за {:d} итераций.".format(n))
                            print("корень - ", x1)

                            num_1.insert(END, "{:d}".format(number) )
                            num_1.insert(END, "-----------------")
                            root_1.insert(END, "{:.3f}".format(x1))
                            root_1.insert(END, "-----------------")
                            f_1.insert(END, "{:.4f}".format((f(x1))))
                            f_1.insert(END, "-----------------")
                            n_1.insert(END, "{:d}".format(n))
                            n_1.insert(END, "----------------" )
                            error_1.insert(END, "0")
                            error_1.insert(END, "----------------")
                            break
                    x0 = x1
                else:
                    print(" не сошелся ")
                    num_1.insert(END, "{:d}".format(number) )
                    num_1.insert(END, "-----------------")
                    root_1.insert(END, "???")
                    root_1.insert(END, "-----------------")
                    f_1.insert(END, "???")
                    f_1.insert(END, "-----------------")
                    n_1.insert(END, "{:d}".format(n))
                    n_1.insert(END, "----------------" )
                    error_1.insert(END, "1")
                    error_1.insert(END, "----------------")
        else:
            print("нет корней на этом промежутке")
        lb += step
        
    if lb != b and ((f(lb) * f(b)) <= 0):
        n = 0
        x0 = lb
        M.append("1")
        number = len(M)
        interval_1.insert(END,  "({:.3f}, {:.3f})".format(lb, b))
        interval_1.insert(END, "-----------------")
        while (n < N):
            n += 1
            if f1(x0) == 0:
                print("производная ноль")
                num_1.insert(END, "{:d}".format(number) )
                num_1.insert(END, "-----------------")
                root_1.insert(END, "???")
                root_1.insert(END, "-----------------")
                f_1.insert(END, "???")
                f_1.insert(END, "-----------------")
                n_1.insert(END, "{:d}".format(n))
                n_1.insert(END, "----------------" )
                error_1.insert(END, "2, 3")
                error_1.insert(END, "----------------")

                break
            else:
                x1 = x0 - (f(x0) / f1(x0))
                print(x1)
                if abs(x1 - x0) < e:
                    print("Точность достигнута за {:d} итераций.".format(n))
                    print("корень - ", x1)

                    num_1.insert(END, "{:d}".format(number) )
                    num_1.insert(END, "-----------------")
                    root_1.insert(END, "{:.3f}".format(x1))
                    root_1.insert(END, "-----------------")
                    f_1.insert(END, "{:.4f}".format((f(x1))))
                    f_1.insert(END, "-----------------")
                    n_1.insert(END, "{:d}".format(n))
                    n_1.insert(END, "----------------" )
                    error_1.insert(END, "2")
                    error_1.insert(END, "----------------")
                    break
                x0 = x1
        else:
            print(" не сошелся ")
            num_1.insert(END, "{:d}".format(number) )
            num_1.insert(END, "-----------------")
            root_1.insert(END, "???")
            root_1.insert(END, "-----------------")
            f_1.insert(END, "???")
            f_1.insert(END, "-----------------")
            n_1.insert(END, "{:d}".format(n))
            n_1.insert(END, "----------------" )
            error_1.insert(END, "2, 1")
            error_1.insert(END, "----------------")

#interface
root = Tk()
root.minsize(600, 330)

#vidgets
lab_1 = Label (root, text = "Нахождение приближенных корней функции", font = 12)
lab_2 = Label(root, text = "на отрезке от a")
lab_3 = Label( root, text = "до b")
lab_4 = Label(root,text = "с шагом")
lab_5 = Label(root, text = "с точностью")
lab_6 = Label(root, text = "Максимальное количество итераций n")

A = Entry(root, width = 10)
B = Entry(root, width = 10)
h = Entry(root, width = 10)
eps = Entry(root, width = 10)
m = Entry(root, width = 10)
grafic = Button(root, width = 20, text = "график", command = graf, bg = "lightblue")
solvebut = Button(root, width = 20, text = "решить", command = solve, bg = "lightblue")
clearbut = Button(root, width = 20, text = "очистить", command = clear, bg = "lightblue")

#table
frame2 = Frame(root, width = 580, height = 140, bg = "lightgrey")

lab_7 = Label(root, text = '№', width = 8, bg = "lightgrey")
lab_8 = Label(root, text = "интервал", width = 8, bg = "lightgrey")
lab_9 = Label(root, text = "корень", width = 8, bg = "lightgrey")
lab_10 = Label(root, text = "f(x)", width = 8, bg = "lightgrey")
lab_11 = Label(root, text = "n", width = 8, bg = "lightgrey")
lab_12 = Label(root, text = "ошибка", width = 8, bg = "lightgrey")

num_1 = Listbox(root, width = 14, height = 6)
interval_1 = Listbox(root, width = 14, height = 6)
root_1 = Listbox(root, width = 14, height = 6)
f_1 = Listbox(root, width = 14, height = 6)
n_1 = Listbox(root, width = 14, height = 6)
error_1 = Listbox(root, width = 14, height = 6)

frame = Frame(root, width = 250, height = 83, bg = "lightgreen")
lab_0 = Label(root, text = "код ошибки\n0 - ошибки нет\n1 - точность не достигнута за n итераций\n2 - шаг вышел за заданный отрезок\n3 - производная равна нулю", justify = LEFT, bg = "lightgreen")

# packer
lab_1.place(x = 80, y = 8)
lab_2.place(x = 10, y = 45)
A.place(x = 110, y = 45)
lab_3.place(x = 185, y = 45)
B.place(x = 240, y = 45)
lab_4.place(x = 10, y = 75)
h.place(x = 75, y = 75)
lab_5.place(x = 155, y = 75)
eps.place(x = 240, y = 75)
lab_6.place(x = 10, y = 105)
m.place(x = 240, y = 105)

frame. place( x = 330, y = 45)
lab_0.place( x = 335, y = 45)

grafic.place(x = 40, y = 140)
solvebut.place(x = 223, y = 140)
clearbut.place(x = 400, y = 140)

frame2.place(x = 10, y = 175)

lab_7.place(x = 40, y = 180)
lab_8.place(x = 130, y = 180)
lab_9.place(x = 220, y = 180)
lab_10.place(x = 310, y = 180)
lab_11.place(x = 400, y = 180)
lab_12.place(x = 490, y = 180)

num_1.place(x = 25, y = 200)
interval_1.place(x = 115, y = 200)
root_1.place(x = 205, y = 200)
f_1.place(x = 295, y = 200)
n_1.place(x = 385, y = 200)
error_1.place(x = 475, y = 200)

root.mainloop()
