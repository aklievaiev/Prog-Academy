# Exercise 1

ticket = input('Please, write your ticket number: ')
int_ticket = list(map(int, ticket))
mid = len(ticket) // 2

if sum(int_ticket[:mid]) == sum(int_ticket[mid:]):
    print('Lucky ticket!')
else:
    print('Not lucky!')

# Exercise 2

txt = input('Please, write some text for testing: ')

print(txt == txt[::-1])

# Exercise 3

x = int(input('Please, write point x: '))
y = int(input('Please, write point y: '))
r = 5
d = (x * x + y * y) ** 0.5

if d > r:
    print('Point out circle')
else:
    print('Point in circle')