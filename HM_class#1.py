# Exercise 1

class Shop:
    def __init__(self, name, price, value):
        self.name = name
        self.price = price
        self.value = value


corn = Shop('Corn', 15, 4)
strawberry = Shop('Strawberry', 40, 200)
print(corn.name)
print(strawberry.price)

# Exercise 2


class Customer:
    def __init__(self, name, surname, age, phone_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone_number


customer_1 = Customer('Artur', 'Klievaiev', 29, 380933706113)
customer_2 = Customer('No-name', 'Unknown', '-', '-')
print(customer_1.surname)
print(customer_2.name)

# Exercise 3


class Order:
    def __init__(self, name, surname, sex, age, ):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age

    def __str__(self):
        return f'{self.surname} {self.name[0]}., {self.age}, {self.sex}'


class Product:
    def __init__(self, product_1, product_2, price_1, price_2):
        self.product_1 = product_1
        self.product_2 = product_2
        self.price_1 = price_1
        self.price_2 = price_2
        self.customer = []

    def __str__(self):
        return f'{self.product_1} and {self.product_2}, {self.price_1 + self.price_2}\n' +\
               ''.join(map(str, self.customer))


cust = Order('Artur', 'Klievaiev', 'male', 29)
order = Product('Bananas', 'Meat', 30, 150)
order.customer.append(cust)

print(order)
