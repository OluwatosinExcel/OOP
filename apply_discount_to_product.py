# An extension of file3
class Item:
    pay_rate = 0.8

    def __init__(self, name: str, price: float, quantity: float):
        self.name = name
        self.price = price
        self.quantity = quantity

    def apply_discount(self):
       # self.price = self.price * Item.pay_rate # Item.pay_rate restricts us from changing the rate for another item.

        self.price = self.price * self.pay_rate


item1 = Item("Cargo pant", 100, 1)
item1.apply_discount()
print(f"The discounted price is: {item1.price}")

item2 = Item("Sweatshirt", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(f"The discounted price for a sweatshirt is 30%: {item2.price}")
