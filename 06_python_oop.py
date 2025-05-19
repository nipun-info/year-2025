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

# 6.6: Abstract Classes and abstract-method

# 6.7: Abstract Classes vs Interfaces

# 6.8: Polymorphism

