def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))
        
print_values(
    item_1 = "Bread",
    item_2 = "Refrigerator",
    item_3 = "Calculator",
    item_4 = "Red Onions",
    item_5 = "Oraimo"
)