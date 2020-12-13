from tkinter import *
from math import sqrt


def solve(a, b, c):
    D = b * b - 4 * a * c
    if D >= 0:
        x1 = (-b + sqrt(D) // (2 * a))
        x2 = (-b - sqrt(D) // (2 * a))
        text = 'Дискриминант уравнения D = {D}, X1 = {x1}, X2 = {x2}.'
    else:
        text = 'Дискриминант уравнения D = {D}, корней не существует.'


def inserter(value):
    output.delete('1.0', END)
    output.insert(1.0, value)


def main():
    try:
        val1 = float(entry1.get())
        val2 = float(entry2.get())
        val3 = float(entry3.get())
        inserter(solve(val1, val2, val3))
    except ValueError:
        inserter('Впишите числа в каждое из трёх полей!')


root = Tk()
root.title('Калькулятор квадратных уравнений')
root.minsize(640,480)
root.resizable(width=False, height=False)

entry1 = Entry(root, font='Arial 16', width=5)
entry1.grid(row=1, column=1, ipady=10)

lab1 = Label(root, font='Arial 24', text='x² + ').grid(row=1, column=2, ipady=20)

entry2 = Entry(root, font='Arial 16', width=5)
entry2.grid(row=1, column=3, ipady=10)

lab2 = Label(root, font='Arial 24', text='x + ').grid(row=1, column=4)
 
entry3 = Entry(root, font='Arial 16', width=5)
entry3.grid(row=1, column=5, ipady=10)

lab3 = Label(root, font='Arial 24', text='= 0').grid(row=1, column=6)

btn = Button(root, font='Arial 16', text='Решить', command=main).grid(row=1, column=7, ipady=10)

output = Text(root, bg='lightblue', fg='navy', font='Arial 20', width=45, height=13, wrap='n')
output.grid(row=2, columnspan=8)

root.mainloop()
