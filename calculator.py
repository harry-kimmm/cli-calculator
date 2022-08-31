again = "Yes"
while(again != "No"):
    operation = input("Enter an operation (addition, subtraction, multiplication, divison, factorial, fibonacci): ")

    if operation == "addition" or "subtraction" or "multiplication" or "division":
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter second number: "))

        if operation == "addition":
            result = str(num1 + num2)
            print("The result is: " + result)
        if operation == "subtraction":
            result = str(num1 - num2)
            print("The result is: " + result)
        if operation == "multiplication":
            result = str(num1 * num2)
            print("The result is: " + result)  
        if operation == "division":
            result = (num1 / num2)
            print("The result is: " + str(round(result, 3)))

    if operation == "factorial" or "fibonacci":
        if operation == "factorial":
            num1 = int(input("Enter a number: "))



    again = input("Enter [No] to stop: ")
