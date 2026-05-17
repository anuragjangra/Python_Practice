try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    match operator:
        case '+': print(f"{num1} + {num2} = {num1 + num2}")
        case '-': print(f"{num1} - {num2} = {num1 - num2}")
        case '*': print(f"{num1} * {num2} = {num1 * num2}")
        case '/': 
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            print(f"{num1} / {num2} = {num1 / num2}")
        case default: raise ValueError("Invalid operator.")
except Exception as e:
    print(f"Invalid input: {e}")
    exit()    