# 7.1: Operator Overloading and method overriding
class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('Good food need Everyone')

    def exercise(self):
        raise NotImplemented

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team):
        super().__init__(name, age, height, weight)
        self.team = team

    # override
    def eat(self):
        print('Strong healthy food')

    # override
    def exercise(self):
        print('Regular exercise good for health')

    # + sign operator overload
    def __add__(self, other):
        return self.age + other.age
    
    # * sign operator overload
    def __mul__(self, other):
        return self.weight * other.weight
    
    # > sign operator overload
    def __gt__(self, other):
        return self.age > other.age

musfiq = Cricketer('Musfiqur Rahim', 35, 60, 72, 'BD')
riyad = Cricketer('Riyad', 38, 68, 75, 'BD')
musfiq.eat()
musfiq.exercise()

# plus sign overload
print(45 + 65)
print('musfiq' + ' riyad')
print([25, 35] + [50, 60, 75])
print(True + False)
print(musfiq + riyad)
print(musfiq * riyad)
print(musfiq > riyad)


# 7.2: static attribute, static method and class method decorator
class Shopping:
    cart = []
    origin = 'bangladesh'

    def __init__(self, name, location):
        self.name = name
        self.location = location

    
    @staticmethod
    def static_method(arg1, arg2):
        return arg1 + arg2

    @classmethod
    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'Buying: {item} for price: {price} and remaining: {remaining}')


print(Shopping.static_method(50, 65))

bashundhara = Shopping("Bashundhara", 'panthpath')
print(bashundhara.name, bashundhara.location)
bashundhara.purchase('laptop', 60000, 80000)

# Shopping.purchase('self', 'Egg', 12, 150)   # without using classmethod
Shopping.purchase('Egg', 12, 150)


# 7.3: Getter Setter and Read Only property Using property Decorator
# read only --> you can not set the value. Value can not be changed
# getter --> get a value of a property through a method. most of the time, you will get the value of a private attribute.
# setter --> set a value of a property though a method. Most of the time, you will set the value of a private property.

class User:
    def __init__(self, name, age, money):
        self._name = name
        self._age = age
        self.__money = money

    # getter without any setter is readonly attribute
    @property
    def age(self):
        return self._age
    
    # getter
    @property
    def salary(self):
        return self.__money
    
    # setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            return 'salary can not be negative'
        self.__money += value


sams = User('Chowdhury', 18, 12000)
# print(sams.__money) 
print(sams.age)
print(sams.salary)
sams.salary = 4500
print(sams.salary)


# 7.4: Understanding inner function and wrapper function
# function is a first class object
# Example-1:
def double_decker():
    print('starting the double decker')
    def inner_fun():
        print('inside the inner')
        return 3000
    return inner_fun

# print(double_decker())
# print(double_decker()())


# Example-2:
def do_something(work):
    print('work stated')
    work()
    print('work ended')

# do_something(2)
# do_something('continous working')

def coding():
    print('coding in python')

do_something(coding)

""" 
Inner Function
An inner function, also called a nested function, is defined inside another 
function. It can access variables from its enclosing (outer) function's 
scope, but cannot be accessed or called directly from outside the outer
function.
একটি অভ্যন্তরীণ ফাংশন, যাকে নেস্টেড ফাংশনও বলা হয়, অন্য একটি ফাংশনের ভিতরে সংজ্ঞায়িত করা হয়। 
এটি তার এনক্লোজিং (বাইরের) ফাংশনের স্কোপ থেকে ভেরিয়েবল অ্যাক্সেস 
করতে পারে, কিন্তু বাইরের ফাংশনের বাইরে থেকে সরাসরি অ্যাক্সেস বা কল করা যায় না।   
"""

def outer_function(text):
    message = text

    def inner_function():
        print(message)
    
    return inner_function

my_func = outer_function("Hello, world!")
my_func() # Output: Hello, world!


# 7.5: How does decorator work



# 7.6: Class composition, inheritance vs composition



# 7.7: A shor overview of UML Diagrams



# 7.8: Design Patterns Singleton, Factory, Builder, etc



# 7.9: Summary

