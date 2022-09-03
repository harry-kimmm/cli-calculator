again = "Yes"
while(again != "No"):
    operation = input("Enter an operation (addition, subtraction, multiplication, divison, factorial, fibonacci): ")

    if operation == "addition":
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter second number: "))
        result = str(num1 + num2)
        print(str(num1) + " + " + str(num2) + " = " + result)
    if operation == "subtraction":
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter second number: "))
        result = str(num1 - num2)
        print(str(num1) + " - " + str(num2) + " = " + result)
    if operation == "multiplication":
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter second number: "))
        result = str(num1 * num2)
        print(str(num1) + " * " + str(num2) + " = " + result)
    if operation == "division":
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter second number: "))
        result = (num1 / num2)
        print(str(num1) + " / " + str(num2) + " = " + str(round(result, 3)))
        
    if operation == "factorial": 
            num1 = int(input("Enter a number: "))
            nextnum = num1
            for i in range(num1-1):
                nextnum = nextnum - 1
                num1 = num1 * nextnum
            result = num1
            print(str(num1) + "! = " + str(result))
    if operation == "fibonacci":
        num1 = int(input("Enter a number: "))
        arr = []
        output = 0
        for i in range(num1):
            output = output + (num1-num1) + (num1+1)
            print(str(output))

    again = input("Input anything to continue. Enter [No] to stop. ")


