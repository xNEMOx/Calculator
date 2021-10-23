# simple calculator by xNEMOx

# asking for the numbers and symbols
number1 = input("Enter your first number: ")
symbol = input("Enter your symbol: ")
number2 = input("Enter your 2nd number: ")
answer = print("Your answer is: ")


# calculation
if symbol == "+":
    print(int(number1) + int(number2))
elif symbol == "-":
    print(int(number1) - int(number2))
elif symbol == "*":
    print(int(number1) * int(number2))
elif symbol == "/":
    print(int(number1) / int(number2))
