first_num = int(input("Enter the first number: "))
operator = input("Enter operator (+, -, *, %): ")
second_num = int(input("Enter the second number: "))

if operator == '+':
    print(first_num + second_num)
elif operator == '-':
    print(first_num - second_num)
elif operator == '*':
    print(first_num * second_num)
elif operator == '%':
    print(first_num % second_num)
else:
    print("Invalid operator")
