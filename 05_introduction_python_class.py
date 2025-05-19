# 5.1: introduction to Simple Class
class Phone:
    price = 19000
    color = 'blue'
    brand = 'samsung'

# print(Phone().price)
my_phone = Phone()
print(my_phone.price, my_phone.color, my_phone.brand)


# 5.2: Creating and Using Methods
def call():
    print('Calling Someone i dont know')

call()

def hello():
    return 'Hi, How are you??'

print(hello())

class Phone:
    price = 19000
    color = 'blue'
    brand = 'samsung'
    features = ['camera', 'speaker', 'hammer']

    def call(self):
        print('Calling One Person')

    def send_sms(self, phone, sms):
        text = f'sending SMS to: {phone} and message: {sms}'
        print(text)

phone = Phone()
print(phone.features)
phone.call()
phone.send_sms(999, 'Govt info')

# Home Task: make a simple calculator
class Calculator: 
    brand = 'Casio MS990'

    def add(self, num1, num2):
        print(num1 + num2)

    def deduct(self, num1, num2):
        print(num1 - num2)

    def multi(self, num1, num2):
        print(num1 * num2)

    def divide(self, num1, num2):
        print(num1 / num2)
    

calculate = Calculator()
calculate.add(80, 20)
calculate.deduct(80, 20)
calculate.multi(80, 20)
calculate.divide(80, 20)

# 5.3: Constructor and __init__ in python
class Phone:
    manufactured = 'China'

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self, phone, sms):
        text = f'sending to: {phone} {sms}'
        print(text)

oppo = Phone('Ronaldo', 'Oppo', 98000)
print(oppo.owner, oppo.brand, oppo.price)

iphone =  Phone('Kaka', 'iphone', 120000)
print(iphone.owner, iphone.brand, iphone.price)


# 5.4: Class Attributes vs instance attributes
class Shop:
    # cart  = []            # class attribute

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []      # instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)

sakib = Shop('Sakib Khan')
sakib.add_to_cart('shoes')
sakib.add_to_cart('phone')
print(sakib.cart)

amir = Shop('Amir khan')
amir.add_to_cart('cap')
amir.add_to_cart('watch')
print(amir.cart)

# 5.5: Explore Bank withdraw deposit and balance using class
class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f'You can not withdraw below {self.min_withdraw}') 
        elif amount > self.max_withdraw:
            print(f'Limit Out. you can not with more than {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'Your aviable balance is: {amount}')

brac = Bank(15000)
# brac.withdraw(25)
# brac.withdraw(250000)
brac.deposit(10000)
brac.withdraw(5000)
print(brac.get_balance())


dbbl = Bank(50000)
dbbl.deposit(2500)
dbbl.deposit(4500)
print(dbbl.get_balance())

# 5.6: Shoping checkout and price calculations
class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity']
        print('Total price', total)
        if amount < total:
            print(f'Please provide {total - amount} more money')
        else:
            extra = amount - total
            print(f'You will return {extra} money')


amir = Shopping('Amir Khan')
amir.add_to_cart('Potato', 40, 5)
amir.add_to_cart('Egg', 12, 30)
amir.add_to_cart('Rice', 50, 5)
# print(amir.cart)

amir.checkout(920)

# 5.7: Use multiple classes to create a school
class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.id = id
        self.current_class = current_class

    def __repr__(self):
        return f'Student Name: {self.name}, class: {self.current_class}, id: {self.id}'
    

class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self):
        return f'Teacher name: {self.name}, Subject: {self.subject}'
    
class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            id = len(self.students) + 1
            student = Student(name, 'C++', id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money { fee - 6500}'
        
    def __repr__(self):
        print('Welcome to', self.name)
        print('------ Our Teachers--------')
        for teacher in self.teachers:
            print(teacher)

        print('------ Our Student--------')
        for student in self.students:
            print(student)
        
        return 'All Done for now'

# alia = Student('Alia Bhatt', 12, 1)
# rubel = Teacher('Rubel B.Sc', 'Algorithm', 101 )
# print(alia)
# print(rubel)

phitron = School('Phitron')
phitron.enroll('sakib', 5200)
phitron.enroll('tamim', 8000)
phitron.enroll('riyad', 7000)

phitron.add_teacher('Dulal Sir', 'Chemistry')
phitron.add_teacher('Arun Sir', 'Math')

print(phitron)

# 5.8: Module Summary and documentation

# https://docs.python.org/3/tutorial/classes.html

