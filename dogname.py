class Dog:
    def __init__(self, name):
        self.name = name
        
dog1 = Dog("Tim")
dog2 = Dog("Bella")

for dog in(dog1, dog2):
    print(dog.name)