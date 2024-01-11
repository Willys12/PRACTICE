class Item:
    all = []
    pay_rate = 0.8
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        self.name = name
        self.price = price
        self.quantity = quantity
        
        #Action to execute
        Item.all.append(self)
        
    def total_price_calc(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
item1 = Item("TV", 25000, 2)
item2 = Item("Sound_bar", 15000, 1)
item3 = Item("Remote", 1500, 1)
item4 = Item("Stand", 10000, 1)

for i in Item.all:
    print(Item.all)