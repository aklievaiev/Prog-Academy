import string
import math
# Exercise 1

text_b = input('Please. write your text: ')
print(text_b.count('b'))

# Exercise 2

name = input('Please, write your name: ')
for digits in string.digits:
    name = name.replace(digits, '')
    name = name.title()
print(name)

# Exercise 3

ord_text = input('Please, write some text: ')
for digits in string.digits:
    ord_text = ord_text.replace(digits, '')
summa = list(map(ord, ord_text))
print(sum(summa))

# Exercise 4

n = 12
i = 2
while i < n:
    print(round(math.pi, i))
    i += 1

# Exercise 5

string = input('Please, write some text: ')
string = string.split()
max_word = max(string, key=len)
print(max_word)
