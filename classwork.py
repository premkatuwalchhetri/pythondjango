#WAP to take 5 input number and find sum of all
# wap to make a calculator and choices is like y/n if user press "y" then he can add, subtract, 

# multiply, divide and if user press "n" then he can exit the program.

# first_number = int(input("enter a nujmber"))
# operator = input("enter operator (+,_)")
# second_number = int(input("enter second number"))

# if operator == '+' :
#   print(first_number + second_number)
# elif operator == '-' :
#   print(first_number - second_number)
# else:
#   print("invalid operator")  

# choice = input("Do you want to continue? (y/n): ")
# if choice.lower() == 'n':
#     print("Terminating the program.")

# import time

# temp = int(input("enter your starting temperature: "))

# while True:
#   if temp < 30:
#     print(f"your ac is off and temperature is {temp}")
#     temp += 1
#   else:
#     print(f"your ac is on and temperature is {temp}")
#     break
  
# for i in range(1,25):    
#   print("hello world")  



# WAP to make combitation of letters
import itertools

letters = "abcdefghijklmnopqrstuvwxyz"

for i in letters:
  print(i)
for i in letters:
  for j in letters:
    print(i+j)
    
for i in letters:
  for j in letters:
    for k in letters:
      print(i+j+k)    
