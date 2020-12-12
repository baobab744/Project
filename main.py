from tkinter import Tk, ttk, Entry, INSERT, END, W, E, Label
import random


def start():
    a = random.randint(1, 99)
    b = random.randint(1, 99)
    c = 0
    result = a + b

    lab1['text'] = f'Score:{c}'
    lab2['text'] = f'{a} + {b}'

    block1.delete(0, END)


def check():
    num = block1.get()
    if num == result:
        lab1['text'] = f'Score:{c + 1}'
        lab2['text'] = f'{a} + {b}'
    else:
        lab2['text'] = f'Game Over, Try Again'


root = Tk()
root.title('Calcul to Win')

style = ttk.Style()
style.configure('TButton', background='white', foreground='black', font='Arial 15')

lab1 = Label(root, font='Arial 30', state='normal', fg='black')
lab1.grid(row=0, column=0, columnspan=2, sticky=W + E, ipady=20)

lab2 = Label(root, font='Arial 30', state='normal', fg='black')
lab2.grid(row=1, column=0, columnspan=2, sticky = W + E, ipady=20)

block1 = Entry(root, font='Arial 30', insertontime=0, relief='solid', state='normal', fg='black')
block1.focus()
block1.grid(row=2, column=0, columnspan=2, sticky=W + E, ipady=20)

button1 = ttk.Button(root, text='Enter', command=check)
button1.grid(row=3, column=0, ipady=10)

button2 = ttk.Button(root, text='Start/Play Again', command=start)
button2.grid(row=3, column=1, ipady=10)

root.mainloop()
