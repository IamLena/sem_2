# Лучина ИУ7-21Б защита
# перевод из 8 в 10

# библиотека
from tkinter import *
from math import pow

# окно
root = Tk()
root.minsize(410,170)
root.title('перевод из восьмиричной в десятичну СС')

#функции
def solve():
    output.delete(0, END)
    a = input.get()
    a = a[::-1]
    b = 0
    for i in range(len(a)):
        if int(a[i])>7:
            output.insert(END, 'ошибка ввода')
            return
        b+=int(a[i])*pow(8,i)
    output.insert(END, round(b))

def clear():
    input.delete(0, END)
    output.delete(0, END)


# виджеты
lab = Label (root, text = 'Перевод из восьмиричной CC в десятичную', \
             font = ('Times New Roman', 14,'bold'))
lab1 = Label(root, text = '8')
input = Entry(root, width = 20)
lab2 = Label(root, text = '10')
output = Entry(root, width = 20)
solveb = Button (root, height = 1, width = 20, text = 'решить',\
                 bg = 'black', fg = 'white', command = solve)
clearb = Button (root, height = 1, width = 20, text = 'очистить',\
                 bg = 'black', fg = 'white', command = clear)

#расположение в окне
lab.place(x = 10, y = 10)
lab1.place(x = 15, y = 60)
input.place(x = 35, y = 60)
lab2.place(x = 15, y = 92)
output.place(x = 35, y = 92)
solveb.place(x = 200, y = 58)
clearb.place(x = 200, y = 90)

root.mainloop()
