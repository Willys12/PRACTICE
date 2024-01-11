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
        
    @staticmethod 
    def is_integer(num):
        #counting floats with zero decimal points
        #i.e 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
print(Item.is_integer(11))