# define a function to return an integer if result is an integer and to return a float if the rsult is in decimal

def format_result(result):
    if result.is_integer(): #check if result is an integr
        return int(result)
    return result #return as it is if it is a float
    

# ask the user for two numbers 
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter the second number: "))
operator = input("choose an operator from +, -, *, /: ")

# performs the calculator operator function
if operator == "/":
    if num2 == 0:
        print("error: cannot divide by zero")
    else:
        result = num1 / num2
elif operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
else:
    print("error, please choose a valid operator")

formatted_result = format_result(result)
print(formatted_result)