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
    if b == 0:
        return "Undefined"
    else:
        result = a / b
        return str(a) + " / " + str(b) + " = " + str(result)
def factorial(a):
    nextnum = a
    shownum = a
    for i in range(a-1):
        nextnum = nextnum - 1
        a = a * nextnum
    result = a
    return str(shownum) + "! = " + str(result)
def fibonacci(a):
    sequence = []
    firstnum = 0
    secnum = 1
    sequence.append(str(firstnum))
    sequence.append(str(secnum))
    for i in range(a-2):
        add = firstnum + secnum
        firstnum = secnum
        secnum = add
        sequence.append(str(add))
    for j in sequence:
        print(j, end = " ")

#Triggers functions for addition, subtraction, multiplication, divison
while(again != "End"):
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
         while operation == "fibonacci":
            if num1 == 1 or num1 == 0:
                print("0")
            else:
                fibonacci(num1)
                print(" ")      
            break    
    again = input("Input anything to continue. Enter [End] to stop. ")


