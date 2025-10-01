import math

operator = input("sqrt or pow: ")
if operator == "sqrt":
    num = int(input('Enter a number: '))
    print(math.sqrt(num))
elif operator == "pow":
    num = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    print(math.pow(num, num2))

