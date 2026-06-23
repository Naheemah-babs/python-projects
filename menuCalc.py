def add (a, b):
    return a + b

def substract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"

while True:
    print("\n Menu: ")
    print("1. Addition")
    print("2. Multiplication")
    print("3. Substraction")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")
   if choice == "5":
        print("Exiting program. Goodbye!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice, please try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if choice == "1":
        result = add(num1, num2)
        print(f"Result: {result}")

    elif choice == "2":
        result = multiply(num1, num2)
        print(f"Result: {result}")

    elif choice == "3":
        result = subtract(num1, num2)
        print(f"Result: {result}")

    elif choice == "4":
        result = divide(num1, num2)
        print(f"Result: {result}")

    
    again = input("\nDo you want another calculation? (y/n): ").lower()

    if again != "y":
        print("Thank you for using the calculator. Goodbye!")
        break


