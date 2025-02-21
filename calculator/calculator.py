def main():

    try:
        num1 = float(input("Enter your first number: "))
    except:
        print("Invalid input, please try again\n\n")
        main()
        
    op = input("Enter an operator: ")

    if op == "+":
        num2 = float(input("Enter another number: "))        
        print("The sum is " + str(add(num1, num2))+"\n\n")
        main()

    elif op == "-":
        try:
            num2 = float(input("Enter another number: "))
        except:
            print("Invalid input, please try again\n\n")
            main()
        print("The difference is " + str(subtract(num1, num2))+"\n\n")
        main()
        
    elif op == "*":
        try:
            num2 = float(input("Enter another number: "))
        except:
            print("Invalid input, please try again\n\n")
            main()
        print("The product is " + str(multiply(num1, num2))+"\n\n")
        main()

    elif op == "/":
        try:
            num2 = float(input("Enter another number: "))
        except:
            print("Invalid input, please try again\n\n")
            main()
        print("The quotient is " + str(divide(num1, num2))+"\n\n")
        main()
        
    else:
        print("Invalid operator, please try again\n\n")
        main()
        
def multiply(x, y):
    return float(x * y)
def add(x, y):
    return float(x + y)
def subtract(x, y):
    return float(x - y)
def divide(x, y):
    return float(x/ y)


print("=============================================")
print("  Welcome to the Python calculator program!")
print("=============================================\n\n")
main()