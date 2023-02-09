from Menu_Item import MenuItem
class Menu:
    def __init__(self):
        self.menu = [MenuItem(name="latte", cost=2.5, water=200, milk=150, coffee=24),
                      MenuItem(name="espresso", cost=1.5, water=50, milk=0, coffee=18),
                     MenuItem(name="cappuccino", cost=3, water=250, milk=50, coffee=24)]
    '''
        get_items() Returns all the names of the  available menu items as a concatenated string.
        e.g. “latte / espresso / cappuccino”
    '''
    def get_items_names(self):
        option = ""
        for item in self.menu:
            option += f"{item.item_name}/"
        return option

    '''
    find_drink(order_name)
    order_name: (str) The name of the drinks order.
    Searches the menu for a particular drink by name. Returns a MenuItem object if it exists,
    otherwise returns None.
    '''
    def find_drink(self, order_name):
        for item in self.menu:
            if item.item_name == order_name:
                return item

        print("Sorry that item is not available.")




