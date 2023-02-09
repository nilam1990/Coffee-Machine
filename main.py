
from Menu import Menu
from Menu_Item import MenuItem
from Coffee_Maker import CoffeeMaker
from Money_Machine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    names = menu.get_items_names()
    choice = input(f"What would you like?{names} : ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report_resources()
        money_machine.report()
    else:
         drink = menu.find_drink(choice)
         if coffee_maker.is_resources_sufficient(drink):
             if money_machine.make_payment(drink.item_cost):
                 coffee_maker.make_coffee(drink)

         else:
             is_on = False









