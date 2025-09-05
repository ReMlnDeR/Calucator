from tkinter import *
from math import log10, tan

root = Tk()
root.geometry("300x500")
root.title("MyCalucator")

def b(n):
    my_input.insert(END, n)

def ClearAll():
    my_input.delete(0, END)
    
def Clear():
    my_input.delete(len(my_input.get()) - 1, END)

def Log_10():
    log = my_input.get()
    final = log10(float(log))
    ClearAll()
    my_input.insert(0, final)

def tanj():
    t = my_input.get()
    final = tan(float(t))
    ClearAll()
    my_input.insert(0, final)
d = {
    'padx': 10,
    'pady': 10,
    'ipadx': 5,
    'ipady': 5
}

my_input = Entry(root)
my_input.grid(row=1, column=1, columnspan=4, sticky="ew", cnf=d)

btn1 = Button(root, text="1", command=lambda: b('1'))
btn2 = Button(root, text="2", command=lambda: b('2'))
btn3 = Button(root, text="3", command=lambda: b('3'))
btn4 = Button(root, text="4", command=lambda: b('4'))
btn5 = Button(root, text="5", command=lambda: b('5'))
btn6 = Button(root, text="6", command=lambda: b('6'))
btn7 = Button(root, text="7", command=lambda: b('7'))
btn8 = Button(root, text="8", command=lambda: b('8'))
btn9   = Button(root, text="9", command=lambda: b('9'))

btn0   = Button(root, text="0", command=lambda: b('0'))
btnCA  = Button(root, text="CA", command=lambda: ClearAll())
btnC   = Button(root, text="C", command=lambda: Clear())
btnlog = Button(root, text="Log10", command=lambda: Log_10())
btntan = Button(root, text="Tan", command= lambda: tanj())

btn1  .grid(row=2, column=1, cnf=d)
btn2  .grid(row=2, column=2, cnf=d)
btn3  .grid(row=2, column=3, cnf=d)
btn4  .grid(row=3, column=1, cnf=d)
btn5  .grid(row=3, column=2, cnf=d)
btn6  .grid(row=3, column=3, cnf=d)
btn7  .grid(row=4, column=1, cnf=d)
btn8  .grid(row=4, column=2, cnf=d)
btn9  .grid(row=4, column=3, cnf=d)


btnCA .grid(row=5, column=1, cnf=d)
btn0  .grid(row=5, column=2, cnf=d)
btnC  .grid(row=5, column=3, cnf=d)

btnlog.grid(row=2, column=4, cnf=d)
btntan.grid(row=3, column=4, cnf=d)

root.mainloop()