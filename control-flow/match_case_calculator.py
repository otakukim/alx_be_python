num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
input("Choose the operation (+, -, *, /): ")
match operation :
    case "+":
        print(f"The result is {num1 + num2}")
    case "-" : 
        print(f"The result is {num1 - num2}")
    case "*" :
        print(f"The result is {num1 * num2}")
    case "/" : 
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Cannot divide by zero")
