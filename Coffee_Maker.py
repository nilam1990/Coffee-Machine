from Menu_Item import MenuItem
class CoffeeMaker:
    def __init__(self):
        self.resources = {"water": 300, "milk": 200, "coffee": 100}

    def report_resources(self):

        """ Print report of all resources """
        print(f"Water: {self.resources['water']} ml")
        print(f"Milk: {self.resources['milk']} ml")
        print(f"Coffee: {self.resources['coffee']} g")

    def is_resources_sufficient(self, drink):
        """ Parameter drink: (MenuItem) The MenuItem object to make.
          Returns True when the drink order can be made, False if ingredients are insufficient.
         e.g.True"""
        can_make = False
        for res in drink.ingredients:
            if self.resources[res] > drink.ingredients[res]:
                can_make = True
            else:
                print(f"sorry there is not enough {res}")
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for res in order.ingredients:
            self.resources[res] -= order.ingredients[res]
        print(f"Here is your {order.item_name} 🍺 Enjoy!!")


