#A class is like a blueprint for creating objects. An object has properties and methods associated with it. Almost everything in Python is an object.

# Create Class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    # init user object
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    def has_birthday(self):
        self.age += 1

class Customer(User):
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    def set_balance(self, balance):
        self.balance = balance
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


brad = User('Brad Traversy', 'brad@gmail.com', 37)
#Init customer object
janet = Customer('Janet Johnson', 'Janet@gmail.com', 26)
janet.set_balance(500)
print(janet.greeting())

brad.has_birthday()
print(brad.greeting())
