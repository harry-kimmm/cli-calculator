again = "Yes"
while(again != "No"):
    operation = input("Enter an operation (addition, subtraction, multiplication, divison, factorial, fibonacci): ")

    if operation == "addition":
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter second number: "))
        result = str(num1 + num2)
        print("The result is: " + result)
    if operation == "subtraction":
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter second number: "))
        result = str(num1 - num2)
        print("The result is: " + result)
    if operation == "multiplication":
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter second number: "))
        result = str(num1 * num2)
        print("The result is: " + result)  
    if operation == "division":
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter second number: "))
        result = (num1 / num2)
        print("The result is: " + str(round(result, 3)))
        
    if operation == "factorial": 
            num1 = int(input("Enter a number: "))
            for i in range(num1):
                nextnum = (num1 - 1)
                num1 = num1 * nextnum
            result = num1
            print("The result is: " + str(result))
    again = input("Enter [No] to stop: ")
