from tkinter import Tk, ttk, Entry, INSERT, END, W, E, Label
import random


def start():
    global a
    a = random.randint(1, 99)
    global b
    b = random.randint(1, 99)
    global c
    c = 0
    global result
    result = a + b

    lab1['text'] = f'Score:{c}       {a} + {b}'
    block1.delete(0, END)


def check():
    num = block1.get()
    if num == result:
        lab1['text'] = f'Score:{c + 1}       {a} + {b}'
    else:
        lab1['text'] = f'Game Over, Try Again'


root = Tk()
root.title('Calcul to Win')

style = ttk.Style()
style.configure('TButton', background='white', foreground='black', font='Arial 15')

lab1 = Label(root, font='Arial 30', state='normal', fg='black')
lab1.grid(row=0, column=0, columnspan=2, sticky=W + E, ipady=20)

block1 = Entry(root, font='Arial 30', insertontime=0, relief='solid', state='normal', fg='black')
block1.focus()
block1.grid(row=1, column=0, columnspan=2, sticky=W + E, ipady=20)

button1 = ttk.Button(root, text='Enter', command=check)
button1.grid(row=2, column=0, ipady=10)

button2 = ttk.Button(root, text='Start/Play Again', command=start)
button2.grid(row=2, column=1, ipady=10)

root.mainloop()