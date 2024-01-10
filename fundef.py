class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_price_calc(self):
        return self.price * self.quantity
    
item1 = Item("TV", 25000, 2)
item2 = Item("Sound_bar", 15000, 1)
    
print(item1.total_price_calc())
print(item2.total_price_calc())