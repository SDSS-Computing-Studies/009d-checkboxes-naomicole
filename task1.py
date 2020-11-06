#! python3
""" 
Create a binary converter.
Recall that binary is a system of counting based on powers of 2.
00000001 = 1
00000010 = 2
00001110 = 14

Create a converter that will convert binary to decimal or decimal to
binary using the interface shown in task1.png.  Use the shell that
has been started in task1.py
This is an incomplete program.  You will need to add onto it, 
but you should not change any of the commands that are already 
here

Use assignment_test.py to test your functions
"""

import tkinter as tk 
from tkinter import *

win = tk.Tk()

ch1 = IntVar()
ch1.set(0)
ch2 = IntVar()
ch2.set(0)
ch3 = IntVar()
ch3.set(0)
ch4 = IntVar()
ch4.set(0)
ch5 = IntVar()
ch5.set(0)
ch6 = IntVar()
ch6.set(0)
ch7 = IntVar()
ch7.set(0)
ch8 = IntVar()
ch8.set(0)

def binary_to_decimal(binary):
    # binary is a list of length 8
    # return value is an integer decimal
    decimal = 0
    if binary[0] == 1:
        decimal = decimal + 128
    if binary[1] == 1:
        decimal = decimal + 64
    if binary[2] == 1:
        decimal = decimal + 32
    if binary[3] == 1:
        decimal = decimal + 16
    if binary[4] == 1:
        decimal = decimal + 8
    if binary[5] == 1:
        decimal = decimal + 4
    if binary[6] == 1:
        decimal = decimal + 2
    if binary[7] == 1:
        decimal = decimal + 1

    return decimal 

def decimal_to_binary(decimal):
    # decimal is an integer value
    # binary is a list of length 8 that contains 1's and 0's
    decimal = decimal
    v1 = 0
    v2 = 0
    v3 = 0
    v4 = 0
    v5 = 0
    v6 = 0
    v7 = 0
    v8 = 0

    if decimal >= 128:
        v1 = 1
        decimal = decimal - 128
    if decimal >= 64:
        v2 = 1
        decimal = decimal - 64
    if decimal >= 32:
        v3 = 1
        decimal = decimal - 32
    if decimal >= 16:
        v4 = 1
        decimal = decimal - 16
    if decimal >= 8:
        v5 = 1
        decimal = decimal - 8
    if decimal >= 4:
        v6 = 1
        decimal = decimal - 4
    if decimal >= 2:
        v7 = 1
        decimal = decimal - 2
    if decimal >= 1:
        v8 = 1
        decimal = decimal - 1

    binary = [v8, v7, v6, v5, v4, v3, v2, v1]

    return binary

def get_binary():
    # function should read the entry widget and generate an integer
    # this integer will be used as an input parameter for decimal to binary and the result updated
    # in the 8 checkboxes
    decimal = int(e1.get())

    binary = decimal_to_binary(decimal)
    
    ch1.set(binary[0])
    ch2.set(binary[1])
    ch3.set(binary[2])
    ch4.set(binary[3])
    ch5.set(binary[4])
    ch6.set(binary[5])
    ch7.set(binary[6])
    ch8.set(binary[7])
    
def get_decimal():
    # function should read the checkboxes and generate a tuple called binary of length 8 that has 1's and 0's
    # this tuple will be used as an input parameter for binary_to_decimal and the result updated
    # in the entry box
    binary = []

    binary.append(ch8.get())
    binary.append(ch7.get())
    binary.append(ch6.get())
    binary.append(ch5.get())
    binary.append(ch4.get())
    binary.append(ch3.get())
    binary.append(ch2.get())
    binary.append(ch1.get())

    decimal = binary_to_decimal(binary)
    e1.delete(0,END)
    e1.insert(0,decimal)

l1 = Label(win,text="Binary / Decimal Converter!")
cb1 = Checkbutton(win,variable=ch8)
cb2 = Checkbutton(win,variable=ch7)
cb4 = Checkbutton(win,variable=ch6)
cb8 = Checkbutton(win,variable=ch5)
cb16 = Checkbutton(win,variable=ch4)
cb32 = Checkbutton(win,variable=ch3)
cb64 = Checkbutton(win,variable=ch2)
cb128 = Checkbutton(win,variable=ch1)
b1 = Button(win, text="Convert to Binary", command=get_binary)
b2 = Button(win, text="Convert to Decimal", command=get_decimal)
e1 = Entry(win)

l1.grid(row=1,column=1,rowspan=2,columnspan=8)
cb1.grid(row=3,column=1)
cb2.grid(row=3,column=2)
cb4.grid(row=3,column=3)
cb8.grid(row=3,column=4)
cb16.grid(row=3,column=5)
cb32.grid(row=3,column=6)
cb64.grid(row=3,column=7)
cb128.grid(row=3,column=8)
b1.grid(row=4,column=1,columnspan=4)
b2.grid(row=4,column=5,columnspan=4)
e1.grid(row=5,column=1,rowspan=2,columnspan=8)

win.mainloop()