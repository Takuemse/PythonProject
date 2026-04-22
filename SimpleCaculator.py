print("⌨ Welcome to basic caculator for basic caculations ⌨")

num1 = float(input("\n Enter the first number: "))
operator = input("Enter your operator (+, -, *,/):")
num2 = float(input("Enter the second number: "))

if operator == "+":
    print("This is for addition")
    result = num1 + num2
    print(f"the result of {num1} + {num2} is {result}")
elif operator == "-":
    print("This is for subtraction")
    result = num1 - num2 
    print(f"the result of {num1} - {num2} is {result}")
elif operator == "*":
    print("This is for multiplication")
    result = num1 * num2 
    print(f"the result of {num1} * {num2} is {result}")  
elif operator == "/":
    print("This is for division")
    result = num1 / num2 
    print(f"the result of {num1} / {num2} is {result}")
else:
    print("This is invalid input. Please enter the required inputs")    
        
