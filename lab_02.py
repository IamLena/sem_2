# Лучина Елена ИУ7-21Б
# сортировка вставками с бинарным поиском

# библиотеки
from tkinter import *
from time import *

root = Tk()
root.title("sort")
root.minsize(400,200)

def correct (s):
    if s == '':
        return False
    else:
        x = s
        if x[0] == " ":
            x = x[1:]
        if x[-1] == " ":
            x = x[:-1]
        if x[0] == "-":
            x = x[1:]
        d = x.find(".")
        if d != -1:
            x = x[:d]+x[d+1:]
        if x.isdigit():
            return True
        else:
            return False

def massive ():
    a = entry.get()
    A = a.split(",")
    if len(A)>10:
        print("некорректная длина")
        return
    else:
        for i in range(len(A)):
            if correct(A[i]):
                A[i] = int(A[i])
            else:
                print("некорректный ввод")
                break
        return A

def sort(A):
    n = len(A)
    for i in range(n):
        key = A[i]
        j = i-1
        while j >= 0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A
            

def solve():
    M = massive()
    print(M)
    t0 = time()
    sort(M)
    t1 = time()
    print (t0, t1, t1-t0)
    print(M)



# виджеты
lab1 = Label (root, text = "Введите массив длинны, непревышающей 10.\nЭлементы вводите через запятую.")
lab2 = Label (root, text = "Массив:")
entry = Entry(root, width = 30, borderwidth = 4)
solveb = Button(root, text = "отсортировать",borderwidth = 4, width = 20, bg = "black", fg = "white", command = solve)

# размещение
lab1.pack()
lab2.pack()
entry.pack()
solveb.pack()


root.mainloop()

