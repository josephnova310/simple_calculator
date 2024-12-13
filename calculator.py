import math 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def square_root(x):
    if x >= 0:
        return  math.sqrt(x)
    else:
        return "error! Cannot calculate square root of a negative number."

def logarithm(x, base):
    if x > 0 and base > 0 and base != 1:
        return math.log(x, base)
    else:
        return "Error ! Invalid input for logarithm."

def calculator():
    while True:
        print("\nSelect operation:")
        print("0. Exit")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square Root")
        print("6. Power")
        print("7.Logarithm")

        choice = input("Enter choice (0/1/2/3/4/5/6/7): ")

        if choice == '0':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"The result is: {add(num1, num2)}")
                elif choice == '2':
                    print(f"The result is: {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"The result is: {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"The result is: {divide(num1, num2)}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        elif choice == '5':
            try:
                num = float(input("Enter the number: "))
                print(f"The square root is: {square_root(num)}")
            except ValueError:
                print("Invalid input! Please enter a numeriic value.")
        elif choice == '6':
            try:
                base = float(input("Enter the base number: "))
                exponent = float(input("Enter the exponent "))
                print(f"The result is: {power(base, exponent)}")
            except ValueError:
                print("Invaild input! please enter numeric values.")
        elif choice == '7':
            try:
                num = float(input("Enter the number (x): "))
                base = float(input("Enter the base "))
                print(f"The result is: {logarithm(num, base)}")
            except ValueError:
                    print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    calculator()
