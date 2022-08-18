class Item:
    def calculate_total_price(self, x, y):  # A function defined in a class is METHOD
        return x * y


item1 = Item()  # instance or object calling the class above
item1.name = "Android"  # Instance attribute(name) of an Object(item1)
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item()  # instance or object calling the class above
item2.name = "Iphone"  # attribute(name) of an Object(item1)
item2.price = 1000
item2.quantity = 2
print(item2.calculate_total_price(item2.price, item2.quantity))
