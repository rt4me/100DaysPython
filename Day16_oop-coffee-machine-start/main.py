from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_program():
    is_on = True
    my_menu = Menu()
    my_coffee_maker = CoffeeMaker()
    my_money_machine = MoneyMachine()

    while is_on:
        customer_input = input(f"What would you like? ({my_menu.get_items()}): ").lower()

        if customer_input == "report":
            my_coffee_maker.report()
            my_money_machine.report()
        elif customer_input == "off":
            is_on = False
        else:
            if my_menu.find_drink(customer_input).name == customer_input:
                drink = my_menu.find_drink(customer_input)
                if my_coffee_maker.is_resource_sufficient(drink):
                    if my_money_machine.make_payment(drink.cost):
                        my_coffee_maker.make_coffee(drink)

coffee_program()