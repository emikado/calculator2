operator = input("Enter operator (= + * /):")
num1 = float(input("Enter number:"))
num2 = float(input("Enter number:"))


if operator == "*":
    result = num1 + num2
    print(result)

elif operator == "-":
    result = num1 + num1
elif operator == "+":
    result = num1 + num2
elif operator == "/":
    result = num1 + num2
else:
    print(f"{operator}is not a valid operator")







