# Tast 1
# print(False == (not True))
# print(True and (False == (True and False)))
# print(not (True and "A" == "B"))

# #  # Task 2
# count = 0
# total = 0
# while count < 64:
#     total += 2**count
#     count += 1
# print('Total weights is', total*0.065/1000000, 'tons')


# # Task 3
# number = int(input('Input a positive number:'))
# factor = 1
# print(f'If the number is {number}, the factors are: ', end='')
# while number > 0 :
#     if number%factor == 0:
#         print(factor, end='')
#     factor += 1
#     if factor > number:
#         break
#     if number%(factor-1) == 0:
#         print(', ', end='')

# # Task 4
# a = float(input('Input first triangle length: '))
# b = float(input('Input second triangle length: '))
# c = float(input('Input third triangle length: '))
# if a == b == c:
#     print('The triangle is equilateral.')
# elif a == b or b == c or c == a:
#     print('The triangle is salene.')
# else:
#     print('The triangle is isosceles.')


# # Task 5
# month_list_31 = [1, 3, 5, 7, 8, 10, 12]
# month_list_30 = [4, 6, 9, 11]
# year = int(input('Input a year: '))
# month = int(input('Input a month of a year: '))
# day = int(input('Input a day of a month: '))
# # Validation
# if month in month_list_31 and day > 31 \
#     or month in month_list_30 and day > 30 \
#     or month == 2 and (day > 29 and (year)%4 == 0) or (day > 28 and (year)%4 != 0):
#     print ('The day is wrong')
# else:
#     print(f'Input day is {year}-{month}-{day}')
#     if day == 31 and month in month_list_31:
#         day = 1 
#         year = year if month != 12 else (year + 1 )
#         month = (month + 1) if month != 12 else 1
#     elif day == 30 and month in month_list_30:
#         day = 1
#         month += 1
#     elif month == 2 and (day == 28 and (year)%4 != 0  or day == 29 and (year)%4 == 0):
#         day = 1
#         month += 1
#     else:
#         day += 1
#     print(f'The next day is {year}-{month}-{day}')
