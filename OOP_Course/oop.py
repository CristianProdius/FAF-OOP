class Item:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
    def CalculateTotalPrice(self, x, y):
        return x * y

item1 = Item("Phone", 100, 5)
print(item1.CalculateTotalPrice(item1.price, item1.quantity))


item2 = Item("Laptop", 100,3)
