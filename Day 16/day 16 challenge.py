from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

drinksMenu = Menu()
coffeeMaker = CoffeeMaker()
money = MoneyMachine()


def coffee_machine():
    flag=True
    while flag:
        drink = input(f"What would you like to have? ({drinksMenu.get_items()}: ")
        if drink == "report":
            coffeeMaker.report()
            money.report()

        elif drink == "off":
            flag = False
            return 0

        else:
            coffee_type = drinksMenu.find_drink(drink)
            has_enough_resources = coffeeMaker.is_resource_sufficient(coffee_type)
            if has_enough_resources:
                has_enough_money = money.make_payment(coffee_type.cost)
                if has_enough_money:
                    coffeeMaker.make_coffee(coffee_type)


coffee_machine()
