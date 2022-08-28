# Exercise 1

num_1 = int(input('Please, write integer number: '))
num_2 = int(input('Please, write integer number: '))
num_3 = int(input('Please, write integer number: '))
num_4 = int(input('Please, write integer number: '))
print(max(num_1, num_2, num_3, num_4))

# Exercise 2

floors = 9
flats_in_floor = 4
flat = int(input('Please, write the flat number: '))

entrance = (flat - 1) // (floors * flats_in_floor) + 1
floor = (flat - 1) // flats_in_floor + 1 - (entrance - 1) * floors
flat_in_floor = (flat - 1) % flats_in_floor + 1

print(entrance, floor, flat_in_floor)

# Exercise 3

year = int(input('Year = '))

if year % 4 or not year % 100 and year % 400:
    print('Not leap year')
else:
    print('Leap year')

# Exercise 4

a = int(input('Please, write triangle a-side: '))
b = int(input('Please, write triangle b-side: '))
c = int(input('Please, write triangle c-side: '))

if a + b > c and a + c > b and b + c > a:
    print(True)
else:
    print(False)
