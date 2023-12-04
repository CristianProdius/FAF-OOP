class Item:
    def CalculateTotalPrice(self, x, y):
        return x * y

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.CalculateTotalPrice(item1.price, item1.quantity))


item2 = Item()
item2.name = "Laptop"
item2.price = 100
item2.quantity = 5