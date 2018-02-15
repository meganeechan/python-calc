import sys

def add(num1, num2):
    asum = str(num1 + num2)
    print ("The sum is " + asum + ".")
    newOp()

def subtract(num1, num2):
    diff = str(num1 - num2)
    print ("The difference is " + diff + ".")
    newOp()

def multiply(num1, num2):
    prod = str(num1 * num2)
    print ("The product is " + prod + ".")
    newOp()

def divide(num1, num2):
    quot = str(num1 / num2)
    print ("The quotient is " + quot + ".")
    newOp()

def exitCheck(op):
    if op == 5:
        print ("Goodbye.")
        sys.exit()

def newOp():
    print ("\n====================================================================")
    print ("Welcome to calculator.\n")
    print ("Select an operation. Enter the corresponding number.")
    print ("1. Addition")
    print ("2. Subtraction")
    print ("3. Multiplication")
    print ("4. Division")
    print ("5. Exit")
    while True:
        try:
            op = int(input("> "))
            break
        except:
            print ("Input was not a number. Try again.")
    exitCheck(op)
    print("Input the two operands.")
    while True:
        try:
            num1 = int(input("Operand 1: "))
            break
        except:
            print ("Input was not a number. Try again.")
    while True:
        try:
            num2 = int(input("Operand 2: "))
            break
        except:
            print ("Input was not a number. Try again.")
    if op == 1:
        add(num1, num2)
    if op == 2:
        subtract(num1, num2)
    if op == 3:
        multiply(num1, num2)
    if op == 4:
        divide(num1, num2)
    if op == 5:
        print ("Goodbye.")

newOp()
        

    
    
