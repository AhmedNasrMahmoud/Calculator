from tkinter import *
from tkinter import ttk
root = Tk()
root.title("CalcuNow")
root.geometry("320x300")
frm = ttk.Frame(root, padding=10)
frm.grid()
expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set(expression)

def equal():
    global expression
    total = str(eval(expression))
    expression = ""
    equation.set(total)

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

#Buttons
equation = StringVar()
EntryField = Entry(frm, textvariable=equation, width= 30)
EntryField.grid(row= 2 , column= 0, columnspan= 3)

PlusButton = Button(frm, text= "+", height= 2, width= 7, background= "green", command=lambda: press("+"))
PlusButton.grid(row= 3, column= 0)

MinusButton = Button(frm, text= "-", height= 2, width= 7, background= "red", command=lambda: press("-"))
MinusButton.grid(row= 3, column= 1)

MultiButton = Button(frm, text= "x", height= 2, width= 7, background= "blue", command=lambda: press("*"))
MultiButton.grid(row= 3, column= 2)

DivButton = Button(frm, text= "/", height= 2, width= 7, background= "orange", command=lambda: press("/"))
DivButton.grid(row= 3, column= 3)

EqualButton = Button(frm, text= "=", height= 2, width= 7, background= "white", command=lambda: equal())
EqualButton.grid(row= 4, column= 3)

BsButton = Button(frm, text= "Backspace", height= 2, width= 7, background= "white", command=lambda: backspace())
BsButton.grid(row= 7, column= 1)

ClearButton = Button(frm, text= "Clear", height= 2, width= 7, background= "white", command=lambda: clear())
ClearButton.grid(row= 7, column= 2)

OneButton = Button(frm, text= "1", height= 2, width= 7, background= "white", command=lambda: press("1"))
OneButton.grid(row= 4, column= 0)

TwoButton = Button(frm, text= "2", height= 2, width= 7, background= "white", command=lambda: press("2"))
TwoButton.grid(row= 4, column= 1)

ThreeButton = Button(frm, text= "3", height= 2, width= 7, background= "white", command=lambda: press("3"))
ThreeButton.grid(row= 4, column= 2)

FourButton = Button(frm, text= "4", height= 2, width= 7, background= "white", command=lambda: press("4"))
FourButton.grid(row= 5, column= 0)

FiveButton = Button(frm, text= "5", height= 2, width= 7, background= "white", command=lambda: press("5"))
FiveButton.grid(row= 5, column= 1)

SixButton = Button(frm, text= "6", height= 2, width= 7, background= "white", command=lambda: press("6"))
SixButton.grid(row= 5, column= 2)

SevenButton = Button(frm, text= "7", height= 2, width= 7, background= "white", command=lambda: press("7"))
SevenButton.grid(row= 6, column= 0)

EightButton = Button(frm, text= "8", height= 2, width= 7, background= "white", command=lambda: press("8"))
EightButton.grid(row= 6, column= 1)

NineButton = Button(frm, text= "9", height= 2, width= 7, background= "white", command=lambda: press("9"))
NineButton.grid(row= 6, column= 2)

ZeroButton = Button(frm, text= "0", height= 2, width= 7, background= "white", command=lambda: press("0"))
ZeroButton.grid(row= 7, column= 0)


root.mainloop()