class Person(object):
    
    
    def __init__(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def isEmployee(self):
        return False
    
class Employee(Person):
    
    def isEmployee(self):
        return True
    
emp = Person("Griffin")
print(emp.getName(), emp.isEmployee())
emp = Employee("Geofrey")
print(emp.getName(), emp.isEmployee())