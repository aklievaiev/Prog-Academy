from math import sqrt

# Exercise 1

int_num = int('123')

# Exercise 2

float_num = float(123)

# Exercise 3

int_from_float = int(12.345)

# Exercise 4

credit_card = str(1111222233334444)
last_4_digits = credit_card[12:]

# Exercise 5

num = input('Please, write three-digit number ')
sum_of_num_digits = int(num[0]) + int(num[1]) + int(num[2])

# Exercise 6

a = float(input("Please, write the length of first triangle's side "))
b = float(input("Please, write the length of second triangle's side "))
c = float(input("Please, write the length of third triangle's side "))
p = (a+b+c)/2
h = (2*sqrt(p*(p-a)*(p-b)*(p-c)))/a
area = (a*h)/2
print('The area of triangle is ' + str(area))

# Exercise 7

number = input('Please, write number ')
print(sum([int(i) for i in list(number)]))

# Exercise 8

print(len(number))

# Exercise 9

print(number[::-1])
