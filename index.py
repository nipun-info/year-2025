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