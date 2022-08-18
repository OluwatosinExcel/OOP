class Item:
    pay_rate = 0.8 # The pay rate after 20% discount(class attribute)

    def __init__(self, name: str, price: float, quantity: float):      # instantiate
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):  # A function defined in a class is METHOD
        return self.price * self.quantity


item1 = Item("Android", 100, 5)  # instance or object calling the class above

item2 = Item("Iphone", 1000, 2)  # instance or object calling the class above

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)
print(item1.calculate_total_price())
print(item2.calculate_total_price())
print(Item.pay_rate) # Prints the Class attribute value
print(Item.__dict__) # Prints all the attribute for class level
print(item1.__dict__) # Prints all the attribute for object/instance level

