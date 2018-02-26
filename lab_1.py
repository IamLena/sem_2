# Лучина Елена ИУ7-21Б
# Калькулятор квадратного уравнения

# Подключение библиотек
from tkinter import *
from math import sqrt

# Окно с именем 'calculator' размера 400*200
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
                m['text'] = 'x может принимать любые значения'
            else:
                m['text'] = 'нет корней'
        else:
            x = -c/b
            if x == -0.0:
                x = 0.0
            m['text'] = 'уравнение линейно, x = '+ str(round(x,2))

    else:
        D = b*b - 4*a*c
        if D<0:
            m['text'] = 'Дискриминант меньше нуля,\n нет действительных корней'
        elif D==0:
            x = b/(2*a)
            if x == -0.0:
                x = 0.0
            m['text'] = 'совпавшие корни, х = ' + str(round(x,2))
        else:
            x1 = (-b+sqrt(D))/(2*a)
            if x1 == -0.0:
                x1 = 0.0
            x2 = (-b-sqrt(D))/(2*a)
            if x2 == -0.0:
                x2 = 0.0
            m['text'] = 'x1 = ' + str(round(x1,2)) + '  x2 = ' + str (round\
                                                                    (x2, 2))

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
        m['text'] = 'некорректный ввод'

# Очистить поля ввода
def clear_a():
    a.delete(0, END)

def clear_b():
    b.delete(0, END)

def clear_c():
    c.delete(0, END)

def clear_all():
    a.delete(0, END)
    b.delete(0, END)
    c.delete(0, END)
    m["text"] = ""
    
# виджиты
f = ("Times New Roman",12)
lab4 = Label(root, text = "Решение квадратного уравнения",font=("Times New \
Roman", 16, "bold"))
a = Entry(root, text = "a", width = 5, font = f)
lab1 = Label(root, text = "x^2 + ", font = f)
b = Entry(root, text = "b", width = 5, font = f)
lab2 = Label(root, text = "x + ", font = f)
c = Entry(root, text = "c", width = 5, font = f)
lab3 = Label(root, text = " = 0", font = f)
lab5 = Label(root, text = 'ответ: ', font = f)
m = Label (root, text = '', font = f)
solveb = Button(root, bg = "black", fg = "white", text = "решить", width = \
15, command = solve, font = f)
clearb = Button(root, bg = "black", fg = "white", text = "очистить", width = \
15, command = clear_all, font = f)

# размещение в окне
lab4.place(x = 30, y = 5)
a.place(x = 60,y = 50)
lab1.place(x = 110,y = 50)
b.place(x = 160,y = 50)
lab2.place(x = 210,y = 50)
c.place(x = 250,y = 50)
lab3.place(x = 300,y = 50)
lab5.place(x = 30, y = 95)
m.place(x = 75, y = 95)
solveb.place(x = 55, y =150)
clearb.place(x = 205, y = 150)

# пункт меню об авторе
def info ():
    root2 = Tk()
    root2.title('info')
    lab4 = Label(root2, text = "Лучина Елена \
Иу7-21Б \n\nЗадание:\nСоздать калькулятор \
c графическим интерфейсом,\nрешающий квадратное \
уравнение. Также в\nпрограмме должно быть меню,\nвыполняющее \
очистку полей по одному и всех\nсразу, повторяющее \
математические\nдействия, выводящее информацию\nо программе и авторе.")
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
clearmenu.add_command(label = "a", command = clear_a)
clearmenu.add_command(label = "b", command = clear_b)
clearmenu.add_command(label = "c",command = clear_c)
clearmenu.add_command(label = "all", command = clear_all)

root.mainloop()
