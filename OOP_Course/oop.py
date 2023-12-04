import csv

class Item:
    pay_rate = 0.8 #the pay after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0) -> None:
        #Validate the reciving data
        assert price >= 0, f"Price {price} is not greater then zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater then zero"

        #Asing to self objecte
        self.name = name
        self.price = price
        self.quantity = quantity

        #Action to execute
        Item.all.append(self)

    def CalculateTotalPrice(self):
        return self.price * self.quantity
    
    def ApplyDiscount(self):
        self.price =self.price * self.pay_rate

    @classmethod
    def InstantiateCSV(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get("name"),
                price = float( item.get("price")),
                quantity= int(item.get("quantity"))
            )

    @staticmethod
    def isInteger(num):
        #we will count the number of flouts data
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self) -> str:
        return f"Item('{self.name}','{self.price}','{self.quantity}')"

print(Item.isInteger(7))

"""
Here we see how to apply a different discount to different items

item1 = Item("Phone", 100, 5)
item1.ApplyDiscount()
print(item1.price)

item2 = Item("Laptop", 150,3)
item2.pay_rate = 0.7 #change the discount for item 2 to 30% fut the item1 is still remain the same
item2.ApplyDiscount()
print(item2.price)
"""



"""
The diference between atributes form class and instance level

print(Item.__dict__) #print atributes for the class level
print(item1.__dict__) #print atributes for the instance level


item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 150, 3)
item2 = Item("TV", 1500, 1)
item2 = Item("PC", 2050, 2)
item2 = Item("Tablet", 250, 5)

print(Item.all)

for instance in Item.all:
    print(instance.name)
"""