class MenuItem:
    def __init__(self,name,cost,water,milk,coffee) -> None:
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }
class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=100, milk=50, coffee=14, cost=2.2),
            MenuItem(name="espresso", water=50, milk=0.5, coffee=14, cost=1.5),
            MenuItem(name="cappuccino", water=150, milk=30, coffee=20, cost=3.5),
        ]
        
        
        
    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options
    
    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry your order not available.")
    