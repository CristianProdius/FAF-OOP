class Item:
    def __init__(self, name: str, price: float, quantity=0) -> None:
        #Validate the reciving data
        assert price >= 0, f"Price {price} is not greater then zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater then zero"

        #Asing to self objecte
        self.name = name
        self.price = price
        self.quantity = quantity
    def CalculateTotalPrice(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 150,3)

print(item1.CalculateTotalPrice())
print(item2.CalculateTotalPrice())