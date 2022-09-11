# Exercise 1

text_1 = input('Text: ')
text_2 = input('Text: ')
print(set(text_1) & set(text_2))

# Exercise 2

list_1 = [i for i in range(100) if i % 3 == 0]
list_2 = [i for i in range(100) if i % 5 == 0]

print(set(list_1) & set(list_2))



