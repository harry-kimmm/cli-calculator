again = "Yes"

#Functions for operations
def addition(a, b):
    result = a + b
    return str(a) + " + " + str(b) + " = " + str(result)
def subtraction(a, b):
    result = a - b
    return str(a) + " - " + str(b) + " = " + str(result)
def multiplication(a, b):
    result = a * b
    return str(a) + " * " + str(b) + " = " + str(result)
def division(a, b):
    result = a / b
    return str(a) + " / " + str(b) + " = " + str(round(result, 2))

def factorial(a):
    nextnum = a
    for i in range(a-1):
        nextnum = nextnum - 1
        a = a * nextnum
    result = a
    return str(a) + "! = " + str(result)


#Triggers functions for addition, subtraction, multiplication, divison
while(again != "No"):
    operation = input("Enter an operation (addition, subtraction, multiplication, divison, factorial, fibonacci): ")
    if operation == "addition" or operation == "subtraction" or operation == "multiplication" or operation == "division":
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter second number: "))        
        while operation == "addition":
            print(addition(num1, num2))
            break
        while operation == "subtraction":
            print(subtraction(num1, num2))
            break
        while operation == "multiplication":
            print(multiplication(num1, num2))
            break
        while operation == "division":
            print(division(num1, num2))
            break

#Triggers functions for factorial and fibonacci
    if operation == "factorial" or operation == "fibonacci":
         num1 = int(input("Enter a number: "))
         while operation == "factorial":
            print(factorial(num1))
            break           


#    if operation == "addition":
#        num1 = int(input("Enter a number: "))
#        num2 = int(input("Enter second number: "))
#        result = str(num1 + num2)
#        print(str(num1) + " + " + str(num2) + " = " + result)
#    if operation == "subtraction":
#        num1 = int(input("Enter a number: "))
#        num2 = int(input("Enter second number: "))
#        result = str(num1 - num2)
#        print(str(num1) + " - " + str(num2) + " = " + result)
#    if operation == "multiplication":
#        num1 = int(input("Enter a number: "))
#        num2 = int(input("Enter second number: "))
#        result = str(num1 * num2)
#        print(str(num1) + " * " + str(num2) + " = " + result)
#    if operation == "division":
#        num1 = int(input("Enter a number: "))
#        num2 = int(input("Enter second number: "))
#        result = (num1 / num2)
#        print(str(num1) + " / " + str(num2) + " = " + str(round(result, 3)))
#        
#    if operation == "factorial": 
#            num1 = int(input("Enter a number: "))
#            nextnum = num1
#            for i in range(num1-1):
#                nextnum = nextnum - 1
#                num1 = num1 * nextnum
#            result = num1
#            print(str(num1) + "! = " + str(result))
#    if operation == "fibonacci":
#        num1 = int(input("Enter a number: "))
#        arr = []
#        output = 0
#        for i in range(num1):
#            output = output + (num1-num1) + (num1+1)
#            print(str(output))
#
#    again = input("Input anything to continue. Enter [No] to stop. ")


