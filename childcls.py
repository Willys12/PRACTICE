class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Gsd(Dog):
    pass

class Pitbull(Dog):
    pass

class St_benard(Dog):
    pass

Bella = Gsd("Bella", 5)
Jusper = Pitbull("Jusper", 3)
Rex = St_benard("Rex", 3)

for dog in (Bella, Jusper, Rex):
    print(dog.name)