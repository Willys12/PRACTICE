class Employee:
    def __init__(self, name, gender, age, salary):
        self.name = name
        self.gender = gender
        self.age = age
        self.salary = salary
        
manager = Employee("Hamisi", "Male", 43, "{:,}".format(50000))
print(manager.name)