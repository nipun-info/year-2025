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