# base class, parent class, common attribute + functionality class
# derived class, child class, uncommon attribute + functionality class

class Gadget:
    def __init__(self, brand, price, color, origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Running laptop: {self.brand}'
    

class Laptop:
    def __init__(self, memory, ssd):
        self.memory = memory
        self.ssd = ssd
    
    def coding(self):
        return f'learning python and practicing'
    

class Phone(Gadget):
    def __init__(self,brand, price, color, origin, dual_sim):
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)
    
    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'
    
    def __repr__(self):
        return f' phone: {self.price} {self.brand} {self.dual_sim}'
    
class Camera:
    def __init__(self, pixel):
        self.pixel = pixel

    def run(self):
        pass

    def change_lens(self):
        pass

# inheritance
my_phone = Phone('iphone', 120000, 'silver', 'china', True)
print(my_phone.brand)
print(my_phone)
