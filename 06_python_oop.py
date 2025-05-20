# 6.1: Introduction to OOP with Fleet Management
# google search object-oriented programming


# 6.2: Common and uncommon things and inheritance

class Gadget:
    def __init__(self, brand, price, color, origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Running laptop: {self.brand}'

class Laptop:
    def __init__(self, memory):
        self.memory = memory
   
    def coding(self):
        return f'learning python and practicing'
    
class Phone(Gadget):
    def __init__(self,brand, price, color, origin, dual_sim):
        self.duel_sim = dual_sim
        super().__init__(brand, price, color, origin)

    
    def phone_call(self, number, text):
        return f'Sending SMS to {number} with: {text}'
    
    def __repr__(self):
        return f'phone: {self.duel_sim}'
    
class Camera:
    def __init__(self, pixel):
        self.pixel = pixel


    def change_lens(self):
        pass

phone = Phone('iphone', 85000, 'silver', 'china', True)
print(phone)
print(phone.brand, phone.origin)
# print(phone.phone_call(777, 'denger'))


""" 
Note:
1. base class, parent class, common attribute + functionality class
2. derived class, child class, uncommon attribute + functionality class

 """

# 6.3: Multi-level Inheritance
class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def move(self):
        pass

class Bus(Vehicle):
    def __init__(self, name, price, seat):
        super().__init__(name, price)
        self.seat = seat

    def __repr__(self):
        return f'{self.name} {self.price}, {self.seat}'

class Truck(Vehicle):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight

class PickUpTruck(Truck):
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)

class AcBus(Bus):
    def __init__(self, name, price, seat, temperature):
        super().__init__(name, price, seat)
        self.temperature = temperature

    def __repr__(self):
        return f'Bus Name:{self.name}, Price: {self.price}, Seat: {self.seat}, Temp: {self.temperature}C'
    



bus = Bus("Nabil", 900, 38)
# print(bus.name, bus.price, bus.seat)
print(bus)

ac_bus = AcBus("Rahbar", 1200, 22, 28)
# print(ac_bus.name, ac_bus.price, ac_bus.temperature)
print(ac_bus)

 
# 6.4: Multiple Inheritance and Inheritance concepts
class Family:
    def __init__(self, address):
        self.adress = address

class School:
    def __init__(self, id, level):
        self.id = id
        self.level = level

class Sports:
    def __init__(self, game):
        self.game = game

class Student(Family, School, Sports):
    def __init__(self, address, id, level, game):
        School.__init__(self, id, level)
        Sports.__init__(self, game)
        Family.__init__(self, address)

    def __repr__(self):
        return f'{self.id} {self.level}, {self.adress}, {self.game}'

student = Student(5, 2, 'pirganj', 'hocky')
print(student)

# 6.5: Encapsulationa and Access Modifiers (Public, private, protected)
class Bank:
    def __init__(self, holder_name, initial_deposit):
        self.name = holder_name             # public attribute
        # self.balance = initial_deposit
        self.__balance = initial_deposit    # private attribute
        self._branch = "Dinajpur"           # protected attribute

    
    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'Your account no money '

    
    def __repr__(self):
        return f'{self.name}, {self.__balance}'

rafsun = Bank('Rafsun Hasan', 15000)
# rafsun.balance = 0
print(rafsun)
rafsun.deposit(25000)
print(rafsun.get_balance())

rafsun.name = "Rakib Hasan"
print(rafsun.name)
# rafsun._branch = 'Pirganj'
print(rafsun._branch)
# print(dir(rafsun))
# print(rafsun._Bank__balance)


# 6.6: Abstract Classes and abstract-method
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod     # enforce all derived class to have a eat method
    def eat(self):
        print('No one can alive without eating' )
    
    @abstractmethod
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self):
        super().__init__()
        # self.name = name
    
    def eat(self):
        print('Hey Bro!, eating banana')

    def move(self):
        print('Not only moved it hanging on tree')

monkey = Monkey()
monkey.eat()

""" 
Abstraction in Python, as part of Object-Oriented Programming (OOP), focuses on simplifying complex systems by presenting only essential information to the user while hiding unnecessary details. This is achieved through abstract classes and methods.
An abstract class cannot be instantiated directly and serves as a blueprint for other classes. It can contain abstract methods, which are declared but do not have an implementation in the abstract class itself. Subclasses inheriting from the abstract class must provide concrete implementations for these abstract methods.

পাইথনে অ্যাবস্ট্রাকশন, অবজেক্ট-ওরিয়েন্টেড প্রোগ্রামিং (OOP) এর অংশ হিসেবে, অপ্রয়োজনীয় বিবরণ লুকিয়ে রেখে ব্যবহারকারীর কাছে শুধুমাত্র প্রয়োজনীয় তথ্য উপস্থাপন করে জটিল সিস্টেমগুলিকে সরলীকরণের উপর দৃষ্টি নিবদ্ধ করে। এটি বিমূর্ত ক্লাস এবং পদ্ধতির মাধ্যমে অর্জন করা হয়।   
একটি বিমূর্ত শ্রেণী সরাসরি তাৎক্ষণিকভাবে তৈরি করা যায় না এবং অন্যান্য শ্রেণীর জন্য একটি নীলনকশা হিসেবে কাজ করে। এতে অ্যাবস্ট্রাক্ট মেথড থাকতে পারে, যেগুলো ডিক্লেয়ার করা হয় কিন্তু অ্যাবস্ট্রাক্ট ক্লাসে এর কোনও ইমপ্লিমেন্টেশন থাকে না। বিমূর্ত শ্রেণী থেকে উত্তরাধিকারসূত্রে প্রাপ্ত উপশ্রেণীগুলিকে এই বিমূর্ত পদ্ধতিগুলির জন্য সুনির্দিষ্ট বাস্তবায়ন প্রদান করতে হবে।


 """
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

# Attempting to instantiate Shape would raise an error
# shape = Shape() # TypeError: Can't instantiate abstract class Shape with abstract methods area

circle = Circle(5)
print(f"Area of circle: {circle.area()}")

square = Square(4)
print(f"Area of square: {square.area()}")

# 6.7: Abstract Classes vs Interfaces
""" 
Abstract Class:
Abstract classes and interfaces are both mechanisms for achieving abstraction in object-oriented programming, but they differ in their purpose and implementation.
Abstract Classes
An abstract class cannot be instantiated directly and serves as a blueprint for other classes. It can contain both abstract methods (methods without implementation) and concrete methods (methods with implementation). Subclasses of an abstract class must provide implementations for all abstract methods.

অবজেক্ট-ওরিয়েন্টেড প্রোগ্রামিংয়ে অ্যাবস্ট্রাক্ট ক্লাস এবং ইন্টারফেস উভয়ই বিমূর্ততা অর্জনের প্রক্রিয়া, তবে তাদের উদ্দেশ্য এবং বাস্তবায়নে তারা ভিন্ন।   
বিমূর্ত ক্লাস   
একটি বিমূর্ত শ্রেণী সরাসরি তাৎক্ষণিকভাবে তৈরি করা যায় না এবং অন্যান্য শ্রেণীর জন্য একটি নীলনকশা হিসেবে কাজ করে। এতে বিমূর্ত পদ্ধতি (বাস্তবায়ন ছাড়া পদ্ধতি) এবং সুনির্দিষ্ট পদ্ধতি (বাস্তবায়ন সহ পদ্ধতি) উভয়ই থাকতে পারে। একটি বিমূর্ত শ্রেণীর উপশ্রেণীগুলিকে অবশ্যই সমস্ত বিমূর্ত পদ্ধতির জন্য বাস্তবায়ন প্রদান করতে হবে।

 """
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        return 2 * (self.length + self.width)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
""" 
Interfaces
In Python, interfaces are typically implemented using abstract base classes. An interface defines a contract that classes must adhere to, specifying the methods they must implement. Unlike abstract classes in some other languages, Python interfaces (implemented via abstract base classes) cannot have concrete methods.
ইন্টারফেস   
পাইথনে, ইন্টারফেসগুলি সাধারণত বিমূর্ত বেস ক্লাস ব্যবহার করে বাস্তবায়িত হয়। একটি ইন্টারফেস এমন একটি চুক্তি সংজ্ঞায়িত করে যা ক্লাসগুলিকে মেনে চলতে হবে, তাদের বাস্তবায়নের পদ্ধতিগুলি নির্দিষ্ট করে। অন্যান্য কিছু ভাষার বিমূর্ত ক্লাসের বিপরীতে, পাইথন ইন্টারফেসে (বিমূর্ত বেস ক্লাসের মাধ্যমে বাস্তবায়িত) কংক্রিট পদ্ধতি থাকতে পারে না।   

 """
from abc import ABC, abstractmethod

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Bird(Flyable):
    def fly(self):
        return "Bird is flying"

# 6.8: Polymorphism
# poly --> many (multiple)
# morph --> shape

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print('animal making some sound')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print('meow, meow')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        print("ghew ghew")

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Haambaa...")

cat = Cat('Like Tiger')
dog = Dog('Real Don')
cow = Cow('Cows are beneficial animals')

# cat.make_sound()
# dog.make_sound()
# cow.make_sound()

animals = [cat, dog, cow]
for animal in animals:
    animal.make_sound()

# 6.9: Summary
class Book:
    def __init__(self, name):
        self.name = name

    def read(self):
        raise NotImplementedError

class Physics(Book):
    def __init__(self, name, writer):
        super().__init__(name)
        self.writer = writer

    def read(self):
        print("Reading physics Book")

topon = Physics('Topon', True)

print(issubclass(Physics, Book))
print(issubclass(Book, Physics))
print(isinstance(topon, Book))
print(isinstance(topon, Physics))

topon.read()

