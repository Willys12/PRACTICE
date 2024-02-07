class Person(object):
    
    
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    
    def Display(self):
        print(self.name, self.id)
        
emp = Person("Willys", 778)
emp.Display()
#print(emp.Display())

class Emp(Person):
    
    
    def Print(self):
        print("Emp class called")
    
Emp_details = Emp("Paul", 2001)

Emp_details.Display()
#print(Emp_details.Display())