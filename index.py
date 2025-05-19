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