class Item:
    #Placeholder for Item class
    pass

class Phone(Item):
    all = []
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than or equal to zero!"
        
        self.name = name
        self.price = price
        self.quantity = quantity
        self.broken_phones = broken_phones
        
        #Action to execute
        Phone.all.append(self)
          
Phone1 = Phone("jseriesv1", 50000, 5, 1)
Phone2 = Phone("jseriesv2", 68000, 6, 1)

for phone in Phone.all:
    print(phone.price)