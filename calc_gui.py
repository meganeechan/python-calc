from tkinter import *
import sys

global num1
global num2
global op #if 0, no op yet
global resflag

def add():
    global op, resflag
    resflag = 0
    if op != 0:
        result()
    op = 1;

def subtract():
    global op, resflag
    resflag = 0
    if op != 0:
        result()
    op = 2;

def multiply():
    global op, resflag
    resflag = 0
    if op != 0:
        result()
    op = 3;

def divide():
    global op, resflag
    resflag = 0
    if op != 0:
        result()
    op = 4;

def insertOne():
    global num1, num2, op, resflag
    if resflag == 1:
        num1 = 0
        resflag = 0
    if op == 0:
        num1 = num1*10 + 1;
        updateDisp(num1)
    else:
        num2 = num2*10 + 1;
        updateDisp(num2)

def insertTwo():
    global num1, num2, op, resflag
    if resflag == 1:
        num1 = 0
        resflag = 0
    if op == 0:
        num1 = num1*10 + 2;
        updateDisp(num1)
    else:
        num2 = num2*10 + 2;
        updateDisp(num2)

def insertThree():
    global num1, num2, op, resflag
    if resflag == 1:
        num1 = 0
        resflag = 0
    if op == 0:
        num1 = num1*10 + 3;
        updateDisp(num1)
    else:
        num2 = num2*10 + 3;
        updateDisp(num2)

def insertFour():
    global num1, num2, op, resflag
    if resflag == 1:
        num1 = 0
        resflag = 0
    if op == 0:
        num1 = num1*10 + 4;
        updateDisp(num1)
    else:
        num2 = num2*10 + 4;
        updateDisp(num2)

def insertFive():
    global num1, num2, op, resflag
    if resflag == 1:
        num1 = 0
        resflag = 0
    if op == 0:
        num1 = num1*10 + 5;
        updateDisp(num1)
    else:
        num2 = num2*10 + 5;
        updateDisp(num2)

def insertSix():
    global num1, num2, op, resflag
    if resflag == 1:
        num1 = 0
        resflag = 0
    if op == 0:
        num1 = num1*10 + 6;
        updateDisp(num1)
    else:
        num2 = num2*10 + 6;
        updateDisp(num2)

def insertSeven():
    global num1, num2, op, resflag
    if resflag == 1:
        num1 = 0
        resflag = 0
    if op == 0:
        num1 = num1*10 + 7;
        updateDisp(num1)
    else:
        num2 = num2*10 + 7;
        updateDisp(num2)

def insertEight():
    global num1, num2, op, resflag
    if resflag == 1:
        num1 = 0
        resflag = 0
    if op == 0:
        num1 = num1*10 + 8;
        updateDisp(num1)
    else:
        num2 = num2*10 + 8;
        updateDisp(num2)

def insertNine():
    global num1, num2, op, resflag
    if resflag == 1:
        num1 = 0
        resflag = 0
    if op == 0:
        num1 = num1*10 + 9;
        updateDisp(num1)
    else:
        num2 = num2*10 + 9;
        updateDisp(num2)

def insertZero():
    global num1, num2, op, resflag
    if resflag == 1:
        num1 = 0
        resflag = 0
    if op == 0:
        num1 = num1*10;
        updateDisp(num1)
    else:
        num2 = num2*10;
        updateDisp(num2)

def insertDot():
    pass

def result():
    global num1, num2, op, resflag
    if op != 0:
        if op == 1:
            result = num1 + num2
        elif op == 2:
            result = num1 - num2
        elif op == 3:
            result = num1 * num2
        elif op == 4:
            result = num1 / num2       
        else:
            pass
        resflag = 1
        num1 = result
        num2 = 0
        op = 0
        result = str(result)
        updateDisp(result)
        print ("Result = " + result)

def clear():
    global num1, num2, op, resflag
    num1 = 0;
    num2 = 0;
    op = 0;
    resflag = 0;
    updateDisp(" ")

def back():
    global num1, num2, op, resflag
    if resflag == 1:
        num1 = 0
        resflag = 0
    if op == 0:
        num1 = int(num1/10);
        updateDisp(num1)
    else:
        num2 = int(num2/10);
        updateDisp(num2)

def updateDisp(input):
    disp.delete('1.0', END)
    disp.insert(INSERT, input)

op = 0
num1 = 0
num2 = 0
resflag = 0

root = Tk()
root.title("Integer Calculator")

disp = Text(root, width = 20, height = 1, padx = 8, pady = 8)
disp.grid(row = 0, column = 0, columnspan = 5, pady = 12)

one = Button(root, width = 5, text = "1", command = insertOne).grid(row = 3, column = 0, padx = 2, pady = 2)
two = Button(root, width = 5, text = "2", command = insertTwo).grid(row = 3, column = 1, padx = 2, pady = 2)
three = Button(root, width = 5, text = "3", command = insertThree).grid(row = 3, column = 2, padx = 2, pady = 2)
four = Button(root, width = 5, text = "4", command = insertFour).grid(row = 2, column = 0, padx = 2, pady = 2)
five = Button(root, width = 5, text = "5", command = insertFive).grid(row = 2, column = 1, padx = 2, pady = 2)
six = Button(root, width = 5, text = "6", command = insertSix).grid(row = 2, column = 2, padx = 2, pady = 2)
seven = Button(root, width = 5, text = "7", command = insertSeven).grid(row = 1, column = 0, padx = 2, pady = 2)
eight = Button(root, width = 5, text = "8", command = insertEight).grid(row = 1, column = 1, padx = 2, pady = 2)
nine = Button(root, width = 5, text = "9", command = insertNine).grid(row = 1, column = 2, padx = 2, pady = 2)
zero = Button(root, width = 12, text = "0", command = insertZero).grid(row = 4, column = 0, columnspan = 2, padx = 2, pady = 2)
dot = Button(root, width = 5, text = ".", command = insertDot).grid(row = 4, column = 2, padx = 2, pady = 2)
plus = Button(root, width = 5, text = "+", command = add).grid(row = 4, column = 3, padx = 2, pady = 2)
minus = Button(root, width = 5, text = "-", command = subtract).grid(row = 3, column = 3, padx = 2, pady = 2)
times = Button(root, width = 5, text = "x", command = multiply).grid(row = 2, column = 3, padx = 2, pady = 2)
div = Button(root, width = 5, text = "/", command = divide).grid(row = 1, column = 3, padx = 2, pady = 2)
equals = Button(root, width = 5, height = 3, text = "=", command = result).grid(row = 3, column = 4, rowspan = 2, padx = 2, pady = 2)
clear = Button(root, width = 5, text = "C", command = clear).grid(row = 1, column = 4, padx = 2, pady = 2)
back = Button(root, width = 5, text = "<-", command = back).grid(row = 2, column = 4, padx = 2, pady = 2)

root.mainloop()
        

