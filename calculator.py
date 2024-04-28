def addition(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y



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

def print_result(x,y,operator,result):
    print("The result of the operation is: %.2f %s %.2f == %.2f" %(x, operator, y, result))



def calculator():
    while True:
        x, y, operator = prompt_user_input()
        result = 0.0

        if(operator == "+"):
            result = addition(x,y)
        elif(operator == "-"):
            result = subtraction(x,y)
        elif(operator == "/"):
            if(y ==0):
                print("Cannot divide by 0")
                continue
            result = division(x,y)
        elif(operator == "*"):
            result = multiplication(x,y)

        print_result(x,y,operator, result)

        y = input("Do you want to continue? [y/n]: ")
        if(y.lower() == "n"):
            break


