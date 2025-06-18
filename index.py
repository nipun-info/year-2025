class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Animal making some sound")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Meow, Meow..")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("ghew ghew...")

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Haambaa...")


cat = Cat("Pushy")
dog = Dog("Doggy")
cow = Cow("Big Bull")

animals = [cat, dog, cow]
for animal in animals:
    animal.make_sound()