# lab_03
# метод касательных

from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np

a = b = 0
R = []

def f(x):
    return sin(x)

#f1 - производная f(x)
def f1(x):
    return cos(x)

#вторая производная
def f2(x):
    return -sin(x)

# построение графика
def graf():
    
    global a
    global b
    e = 0.1
    N = 10
    step = 0.5

    global R
    R = []
    lb = a

    while lb < b:
        if b - lb <= step:
            rb = b   
        else:
            rb = lb + step
        n = 0
        x0 = lb
        if f(lb) * f(rb) <= 0:
            if f1(lb) != 0:
                while (n < N):
                    if f(x0) == 0:
                        R.append(x0)
                        break
                    
                    n += 1
                    x1 = x0 - (f(x0) / f1(x0))
                    
                    if not (lb < x1 < rb):
                        break

                    if abs(x1 - x0) < e:
                        R.append(x1)
                        break

                    x0 = x1           
        lb += step
        
    X = np.linspace(a, b)
    f2 = np.vectorize(f)
    Y = f2(X)
    F = [f(i) for i in R]
    plt.plot(X, Y)
    plt.scatter(R, F)
    if max_min() != None:
        Imin, Imax, fmin, fmax =  max_min()
        Fmin = [fmin] * len(Imin)
        Fmax = [fmax] * len(Imax)
        plt.scatter(Imin, Fmin)
        plt.scatter(Imax, Fmax)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('f(x)')
    plt.grid()
    plt.show()
        
# очищение полей   
def clear():
    error_message.config(text =  "")
    global R
    M = []
    R = []
    p = []
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
        error_message.config(text =  "Некорректный ввод")
        return False
    else:
        x = a
        if x[0] == '-':
            x = x[1:]
        d = x.find('.')
        if d != -1:
            x = x[:d] + x[d+1:]
        if x.isdigit():
            return a
        else:
            error_message.config(text =  "Некорректный ввод")
            return False
        
def solve():
    error_message.config(text =  "")
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
        error_message.config(text =  "Некорректный ввод")
        return
    else:
        if correct(step) and float(step) > 0:
            step = float(step)
        else:
            error_message.config(text =  "Некорректный ввод")
            return

    global e    
    e = eps.get()
    if e == '':
        error_message.config(text =  "Некорректный ввод")
        return
    else:
        d = e.find('.')
        x = e
        if d!= -1:
            x = e[:d]+e[d+1:]
        if x.isdigit():
            e = float(e)
            if not(0 < e < 1):
                error_message.config(text =  "Некорректный ввод")
                return
        else:
            error_message.config(text =  "Некорректный ввод")
            return

    global N
    N = m.get()
    if N == '':
        error_message.config(text =  "Некорректный ввод")
        return
    else:
        if N.isdigit():
            N = int(N)
        else:
            error_message.config(text =  "Некорректный ввод")
            return

    num_1.delete(0, END)
    interval_1.delete(0, END)
    root_1.delete(0, END)
    f_1.delete(0, END)
    n_1.delete(0, END)
    error_1.delete(0, END)
    
    newtons_method(a , b, step, e, N)

def newtons_method(a , b, step, e, N):
    M = []
    lb = a
    while lb < b:
        if b - lb <= step:
            rb = b   
        else:
            rb = lb + step
        n = 0
        x0 = lb
        if f(lb) * f(rb) <= 0:
            if f(lb) != 0:
                M.append("1")
                number = len(M)
                interval_1.insert(END,  "({:.3f}, {:.3f})".format(lb, rb))
                interval_1.insert(END, "-----------------")
                while (n < N):
                    n += 1
                    if f1(x0) == 0:
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

                    x1 = x0 - (f(x0) / f1(x0))
                    if not (lb < x1 < rb):
                        num_1.insert(END, "{:d}".format(number) )
                        num_1.insert(END, "-----------------")
                        root_1.insert(END, "???")
                        root_1.insert(END, "-----------------")
                        f_1.insert(END, "???")
                        f_1.insert(END, "-----------------")
                        n_1.insert(END, "{:d}".format(n))
                        n_1.insert(END, "----------------" )
                        error_1.insert(END, "2")
                        error_1.insert(END, "----------------")

                        break

                    if abs(x1 - x0) < e:
                        num_1.insert(END, "{:d}".format(number) )
                        num_1.insert(END, "-----------------")
                        root_1.insert(END, "{:.5f}".format(x1))
                        root_1.insert(END, "-----------------")
                        f_1.insert(END, "{:.5f}".format((f(x1))))
                        f_1.insert(END, "-----------------")
                        n_1.insert(END, "{:d}".format(n))
                        n_1.insert(END, "----------------" )
                        error_1.insert(END, "0")
                        error_1.insert(END, "----------------")
                        break

                    x0 = x1
                else:
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
        lb += step

    if len(M) == 0:
        error_message.config(text =  "Нет корней.")
    
        

def max_min():

    global a
    global b
    step = 0.5
    global e
    global N

    P = []
    lb = a
    
    while lb < b:
        if b - lb <= step:
            rb = b   
        else:
            rb = lb + step
            
        n = 0
        x0 = lb
        if f1(lb) * f1(rb) <= 0:
            if f2(lb) != 0:
                while (n < N):
                    n += 1
                    if f1(x0) == 0:
                        break

                    x1 = x0 - (f1(x0) / f2(x0))
                    if not (lb < x1 < rb):
                        break

                    if abs(x1 - x0) < e:
                        P.append(x1)
                        break

                    x0 = x1
        lb += step

    P.append(a)
    P.append(b)
    print(P)
    P2 = []
    fmax = fmin =  f(P[0])
    imin = imax = P[0]
    Imax = []
    Imin = []
    for i in P:
        if f(i) >= fmax:
            if f(i) == f(imax):
                Imax.append(i)
            else:
                Imax = [i]
                imax = i
            fmax = f(i)
            print(imax, fmax)
        if f(i) <= fmin:
            if f(i) == f(imin):
                Imin.append(i)
            else:
                Imin = [i]
                imin = i
            fmin = f(i)
            print(imin, fmin)

    print(Imin, Imax, fmin, fmax)
    if fmin == fmax:
        return
    else:
        return Imin, Imax, fmin, fmax

#interface
root = Tk()
root.minsize(660, 450)

#vidgets
lab_1 = Label (root, text = "Нахождение приближенных корней функции методом касательных", font = 12)
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

error_message = Label(root, text = '', font = 12, fg = "red")

#table
frame2 = Frame(root, width = 580, height = 215, bg = "lightgrey")

lab_7 = Label(root, text = '№', width = 8, bg = "lightgrey")
lab_8 = Label(root, text = "интервал", width = 8, bg = "lightgrey")
lab_9 = Label(root, text = "корень", width = 8, bg = "lightgrey")
lab_10 = Label(root, text = "f(x)", width = 8, bg = "lightgrey")
lab_11 = Label(root, text = "n", width = 8, bg = "lightgrey")
lab_12 = Label(root, text = "ошибка", width = 8, bg = "lightgrey")

num_1 = Listbox(root, width = 14, height = 11)
interval_1 = Listbox(root, width = 14, height = 11)
root_1 = Listbox(root, width = 14, height = 11)
f_1 = Listbox(root, width = 14, height = 11)
n_1 = Listbox(root, width = 14, height = 11)
error_1 = Listbox(root, width = 14, height = 11)

frame = Frame(root, width = 320, height = 90, bg = "lightgreen")
lab_0 = Label(root, text = "код ошибки\n0 - ошибки нет\n1 - точность не достигнута за n итераций\n2 - точка пересечения касательной и оси вне интервала\n3 - производная на конце интервала равна нулю", justify = LEFT, bg = "lightgreen")



# packer
lab_1.place(x = 30, y = 8)
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

frame.place( x = 330, y = 45)
lab_0.place( x = 335, y = 45)

grafic.place(x = 65, y = 140)
solvebut.place(x = 238, y = 140)
clearbut.place(x = 425, y = 140)

frame2.place(x = 30, y = 175)

lab_7.place(x = 65, y = 180)
lab_8.place(x = 155, y = 180)
lab_9.place(x = 245, y = 180)
lab_10.place(x = 335, y = 180)
lab_11.place(x = 425, y = 180)
lab_12.place(x = 515, y = 180)

num_1.place(x = 50, y = 200)
interval_1.place(x = 140, y = 200)
root_1.place(x = 230, y = 200)
f_1.place(x = 320, y = 200)
n_1.place(x = 410, y = 200)
error_1.place(x = 500, y = 200)

error_message.place(x = 230, y = 400)

root.mainloop()
