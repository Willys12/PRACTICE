class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    #First instance method
    def description(self):
        return f"{self.name} is {self.age} year old"
    
    #second instance method
    def speak(self, sound):
        return f"{self.name} say {sound}"