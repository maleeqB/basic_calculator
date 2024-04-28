def prompt_user_input():
    x = 0.0
    y = 0.0
    operator = ""
    while True:
        try:
            x = float(input("Enter first value: "))
            y = float(input("Enter second value: "))
        except ValueError:
            print("Invalid input. Enter valid number to continue")
            continue
        operator = input("Enter operation to be performed. Either of: '+', '-', '/', '*': ")
        if(not operator in "+-/*"):
            print("Invalid operator. Valid operators are: '+', '-', '/', '*'")
            continue
        break
    return x, y, operator

