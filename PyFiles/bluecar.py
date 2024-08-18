class Car:
    
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
        
        
    #first instance method
    def description(self):
        return f"The {self.color} car has {self.mileage:,} miles"
    
car1 = Car("blue", 20000)
car2 = Car("red", 30000)

for car in (car1, car2):
    print(car.description())