# Лучина Елена ИУ7-21Б
# Калькулятор квадратного уравнения

# Подключение библиотек
from tkinter import *
from math import sqrt

# Окно с именем 'calculator'
root = Tk()
root.title('calculator')
root.minsize(400,200)

# Описание функций

# Проверка ввода
def cor_inp(h):
    if h == '':
        return False
    else:
        x = h
        c = h.find('.')
        if c != -1:
            x = h[:c]+ h[c+1:]
        if h[0] == '-':
            x = x[1:]
        if x.isdigit():
            return True
        else:
            return False

# Решение уравнения, поиск корней, вывод результата
def find_root(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                m.delete(0, END)
                m.insert(END, 'x может принимать любые значения')
                m.insert(END, a)
            else:
                m.delete(0, END)
                m.insert(END, 'нет корней')
        else:
            x = -c/b
            m.delete(0, END)
            m.insert(END, 'уравнение линейно, x = ')
            m.insert(END, x)

    else:
        D = b*b - 4*a*c
        if D<0:
            m.delete(0, END)
            m.insert(END, 'Дискриминант меньше нуля, нет корней')
        elif D==0:
            x = b/(2*a)
            m.delete(0, END)
            m.insert(END, 'совпавшие корни, х = ')
            m.insert(END, x)
        else:
            x1 = (-b+sqrt(D))/(2*a)
            x2 = (-b-sqrt(D))/(2*a)
            m.delete(0, END)
            m.insert(END, 'x1 =')
            m.insert(END, x1)
            m.insert(END, 'x2 =')
            m.insert(END, x2)

# Прием аргументов у пользователя и их передача в функцию решения    
def solve ():
    A = a.get()
    B = b.get()
    C = c.get()
    if cor_inp(A) and cor_inp(B) and cor_inp(C):
        A = float(A)
        B = float(B)
        C = float(C)
        find_root(A, B, C)
    else:
        m.insert(END, 'некорректный ввод')

# Очистить поле ввода
def clear(x):
    x.delete(0, END)

def clear_a():
    clear(a)

def clear_b():
    clear(b)

def clear_c():
    clear(c)

def clear_all():
    clear(a)
    clear(b)
    clear(c)
    
# виджиты
f = ("Times New Roman",12)
lab4 = Label(root, text = "Решение квадратного уравнения", font=("Times New Roman", 16, "bold"))
a = Entry(root, text = "a", width = 5, font = f)
lab1 = Label(root, text = "x^2 + ", font = f)
b = Entry(root, text = "b", width = 5, font = f)
lab2 = Label(root, text = "x + ", font = f)
c = Entry(root, text = "c", width = 5, font = f)
lab3 = Label(root, text = " = 0", font = f)
m = Listbox (root, height = 2, width = 35, font = f, justify='center')
solveb = Button(root, bg = "black", fg = "white", text = "решить", width = 25, command = solve, font = f)

# размещение в окне
lab4.place(x = 30, y = 5)
a.place(x = 60,y = 50)
lab1.place(x = 110,y = 50)
b.place(x = 160,y = 50)
lab2.place(x = 210,y = 50)
c.place(x = 250,y = 50)
lab3.place(x = 300,y = 50)
m.place(x = 60, y = 105)
solveb.place(x = 80, y =150)

# пункт меню о авторе
def info ():
    root2 = Tk()
    root2.title('info')
    lab4 = Label(root2, text = "Лучина Елена \nИу7-21Б \nКалькулятор")
    lab4.pack()
    root2.mainloop()

#меню
menubar = Menu(root)
menulist = Menu(menubar, tearoff = 0)
root.config(menu=menubar)
menubar.add_cascade(label="Menu", menu=menulist)
menulist.add_command(label="info", command = info)
menulist.add_command(label="solve", command = solve)
clearmenu = Menu(menubar, tearoff = 0)
menulist.add_cascade(label="clear...", menu = clearmenu)
clearmenu.add_command(label = "a", command = clear_a())
clearmenu.add_command(label = "b", command = clear_b())
clearmenu.add_command(label = "c",command = clear_c())
clearmenu.add_command(label = "all", command = clear_all)

root.mainloop()



