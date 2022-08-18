class Item:                 # class
    pass


item1 = Item()              # instance or object calling the class above
item1.name = "Android"               # attribute(name) of an Object(item1)
item1.price = 100
item1.quantity = 5
item1.total = item1.price * item1.quantity
total = print(item1.total)


item2 = Item()              # instance or object calling the class above
item2.name = "Iphone"               # attribute(name) of an Object(item1)
item2.price = 1000
item2.quantity = 2
item2.total = item2.price * item2.quantity
total = print(item2.total)

