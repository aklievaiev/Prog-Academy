# Exercise 1

n = int(input('Please, write negative number: '))
n > 0 or print(n)

# Exercise 2

a = int(input('Please, write the value for A: '))
a > 20 or print('A is less then 20')

# Exercise 3

num = int(input('Please, write the value for number: '))
num == 0 or print("Number isn't zero value")

# Exercise 4

even_odd_number = int(input('Please, write thr value for number: '))
even_odd_number % 2 == 0 or print('Number is odd')

# Exercise 5

numbers_list = input('Please, write the value for three numbers: ')
numbers_list = numbers_list.split()
print(max(map(int, numbers_list)))