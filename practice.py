# while True:
#     age = int(input("enter age of the person: "))
#     if age < 0:
#         print("enter valid age")
#     else:
#         print(f"your age is {age}")

# import math
# print(math.ceil(3.1))
# print(math.floor(3.9))

# from functools import reduce
# nums = [1, 2, 3, 4]
# result = reduce(lambda x, y: x if x > y else y, nums)
# print(result)

# nums = list(range(1, 6))
# mapped = list(map(lambda x: x**2, nums))
# print(mapped)

# (lambda  a: a+5) (20)


# x = lambda a: a+6
# print(x(50))

# x = (lambda a,b: a if a>b else b)
# print(x(30,20))

# import random
# import math
# from functools import reduce

# temperatures = [random.randint(-10, 45) for _ in range(20)]
# print("Temperatures:", temperatures)

# def sum_of_temperature(temperature):
#     if not temperature:
#         return 0
#     return temperature[0] + sum_of_temperature(temperature[1:]) 

# total_temperature = sum_of_temperature(temperatures)
# print("Total Sum of Temperatures:", total_temperature)
# fahrenheit = list(map(lambda c: (c * 9/5) + 32, temperatures))
# print("Fahrenheit:", fahrenheit)
# extreme_temperature = list(filter(lambda x: x < 0 or x > 35, temperatures))
# print("Extreme Temperatures:", extreme_temperature)
# highest_temperature = reduce(lambda a, b: a if a > b else b, temperatures)
# print("Highest Temperature:", highest_temperature)
# square_roots = [round(math.sqrt(t), 2) for t in temperatures if t > 0]
# print("Square roots of positive temperatures:", square_roots)

'''Write a Python script that:

Generates 10 random temperatures between -5 and 40

Converts each temperature to Fahrenheit

Prints both the original and converted temperatures using map() and lambda'''

# import random
# temperature = [random.randint(-5,40) for _ in range(10)]
# print(temperature)
# fahrenheit = list(map(lambda c : (c*9/5) + 32, temperature))
# print(fahrenheit)

# def recursive_sum(lnd):
#     if not sum:
#         return 0
#     else:
#         return lnd[0] + recursive_sum(lnd[1:])
        
# Write a recursive function that takes a list of integers and returns their sum.
# Then test your function using this list: [1, 3, 5, 7]
# def recursive_sum(lnd):
#     if not lnd:
#         return 0
#     else:
#         return lnd[0] + recursive_sum(lnd[1:])
    
# test_list = [1,3,5,7]
# print(recursive_sum(test_list))


# B3.
# Create a list of 15 random integers between -20 and 50.
# Then use a lambda and filter() to return only the values that are:

# Less than 0, or

# Greater than 35

# import random
# import math

# my_list = [random.randint(-20, 50) for _ in range(15)]
# print(my_list)

# nummbers = list(filter(lambda x: x<0 or x>35, my_list))
# print(my_list)

'''Write a list comprehension that returns the square root
(rounded to 2 decimal places) of all positive numbers in the list:
temps = [-2, 4, 9, 0, 16, -5, 25]
📌 Requirements:

Use list comprehension

Use math.sqrt()

Use round(..., 2)

Only include positive values (i.e. > 0)'''

# import math

# temps = [-2, 4,9,0,16,-5,25]
# square_roots = [round(math.sqrt(x)) for x in temps if x > 0]
# print("Square roots", square_roots)

# from functools import reduce

# nums = [8, 3, 10, 1, 4]
# smallest = reduce(lambda x, y: x if x < y else y, nums)
# print(smallest)

# x = 5
# y = 10
# if x * 2 > y or y - 5 == x:
#     print("Yes")
# else:
#     print("No")

'''Write a Python function called is_even that takes an integer parameter n and returns True if n is even, and False otherwise.'''
# def is_even(n):
#     return n % 2 == 0

# value = int(input("Enter an integer: "))
# print(is_even(value))


'''Write a function called count_vowels that takes a string parameter text and returns the number of vowels (a, e, i, o, u, both uppercase
 and lowercase) in the string.'''

# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in text:
#         if char in vowels:
#             count += 1
#     return count
#     print(count)

# word = input("Enter a word: ")
# print("Number of vowels:", count_vowels(word))

'''Write a function called reverse_string that takes a string as input and returns the reversed version of that string.'''
# def reverse_string(text):
#     return text[::-1]

# text = input("enter a text: ")
# print("reversed text is", reverse_string(text))

'''Write a function called is_palindrome that takes a string as input and returns True if the string is a palindrome 
(same forward and backward), and False otherwise.'''

# def is_palindrome(text):
#     cleaned = text.replace(" ", "").lower()
#     return cleaned == cleaned[::-1]

# text = input("enter a text: ")
# print("ans is ", is_palindrome(text))

'''Write a function called sum_of_digits that takes an integer n and returns the sum of its digits.'''
# def sum_of_digits(sum):
#     if sum+1 == sum:
#         print(sum)
#     else:
#         print("invalid")

# sum = int(input("enter a integer: "))
# print("ans is ", sum_of_digits(sum))

    
'''Write a function is_positive(n) that takes an integer n and:

Returns "Positive" if n > 0

Returns "Negative" if n < 0

Returns "Zero" if n == 0

Then, get user input and print the result of calling the function.'''

# def is_positive(n):
#     if n > 0:
#         return "positive"
#     elif n < 0:
#         return "negative"
#     else:
#         return "zero"

# n = int(input("enter a interger: "))
# print(is_positive(n))

'''Write a function get_even_numbers(lst) that takes a list of integers and returns a new list containing only the even numbers.

Then:

Ask the user to enter 5 numbers, store them in a list.

Call the function and print the result.'''

# def get_even_numbers(lst):
#     even = []
#     for num in lst:
#         if num % 2 == 0:
#             even.append(num)
#     return even
# nums = []
# for i in range(5):
#     number = int(input("Enter a number: "))
#     nums.append(number)
# print("Even numbers:", get_even_numbers(nums))

'''Write a function convert_to_fahrenheit(celsius_list) that:

Takes a list of temperatures in Celsius

Returns a new list with each temperature converted to Fahrenheit, using the formula:
use map() and lambda to do the conversion
Then:
Ask the user to enter 5 temperatures in Celsius

Call the function and print the result'''


# def convert_to_fahrenheit(celsius_list):
#     return list(map(lambda c: (c * 9/5) + 32, celsius_list))

# # Input from user
# temperatures = []
# for i in range(5):
#     temp = float(input("Enter temperature in Celsius: "))
#     temperatures.append(temp)

# # Output
# print("Temperatures in Fahrenheit:", convert_to_fahrenheit(temperatures))
















