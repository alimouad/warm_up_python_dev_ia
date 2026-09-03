# exercice1
# name = input("type your name: ")
# last_name = input("type your last name: ")
#
# hour_salary = input("type your hour salary: ")
#
# hours_worked = input("type your hours worked: ")
#
#
# def calculate_salary(hour_salary, hours_worked):
#    try :
#         if not type(hour_salary) is int and not type(hours_worked) is int:
#            raise TypeError("Only integers are allowed")
#    except TypeError as e:
#         print(e)
#         return 0
#    else:
#         if hours_worked > 40:
#             added_hours = hours_worked - 40
#             added_salary = added_hours * (hour_salary * 1.5)
#         else:
#             added_salary = 0
#         return (hour_salary * hours_worked) + added_salary
#
#
# result = calculate_salary(hour_salary, hours_worked)
# print(f"Hello {name} {last_name}, your salary is: {result}")
#
#

# exercice2
# n1 = int(input("type your first number: "))
# n2 = int(input("type your second number: "))
# result = ''
# def calculate_multi(n1,n2):
#     try:
#         if isinstance(n1, int) and isinstance(n2, int):
#             pass
#         else:
#             raise TypeError("Only integers are allowed")
#     except TypeError as e:
#         print(e)
#         return 0
#     else:
#         if (n1 < 0 and n2 < 0) or (n1 > 0 and n2 > 0):
#             result = f'the result will be postive'
#         elif n1 == 0 or n2 == 0:
#             result = f'the result will be 0'
#         else :
#             result = f'the result will be negative'
#         return result
#
# output = calculate_multi(n1,n2)
# print(output)


# exercice 3

# number = int(input("type a number: "))
# result = 0

# while number > 0:
#     result += number
#     number -= 1

# print (f"the sum of all numbers from 1 to {number} is: {result}")


# exercice 6
# word = input("type a word: ")
# reverse_result = ''
#
# while len(word) > 0:
#     reverse_result += word[-1]
#     word = word[:-1]
#
# print(f"the reverse of the word is: {reverse_result}")


# exercice7:

import math


x1 = float(input("type the x1 number: "))
x2 = float(input("type the x2 number: "))
y1 = float(input("type the x3 number: "))
y2 = float(input("type the x4 number: "))


def calculate_distance(x1, x2, y1, y2):
    try:
        if not all(isinstance(i, (int, float)) for i in [x1, x2, y1, y2]):
            raise TypeError("Only numbers are allowed")
    except TypeError as e:
        print(e)
        return 0
    else:
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance

result = calculate_distance(x1, x2, y1, y2)
print(f"the distance between the two points is: {result:.2f}")