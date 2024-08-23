# calculator
#  first_step: ask first number from user
#   second_step: ask operation from user
#   hird_step: second number from user_
#   fourth_step: perform operation based on operator
  
first_num = int(input("enter a number"))
operator = input("enter operator (+,-,*,%): ")
second_num = int(input("enter second number"))

if operator == '+':
    print(first_num +second_num)
elif operator == '-':
    print(first_num - second_num)
elif operator == '*':
    print(first_num * second_num)
elif operator == '%':
    print(first_num % second_num)
else:
    print("invalid operator")

  
   