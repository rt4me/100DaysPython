MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

total_money = 0

#TODO: Check for sufficient resources before making coffee.
# If not enough, print messages like "Sorry there is not enough water.”
def check_resources(coffee_type):
    for item in MENU[coffee_type]['ingredients']:
        if MENU[coffee_type]["ingredients"][item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

#TODO: Print report when entering "report"; Include Water, Milk, Coffee, and Money.
def output_report():
    for item in resources:
        print(f"{item.title()}: {resources[item]}")
    print(f"Money: ${total_money:.2f}")

def increase_money_on_hand(money_on_hand, amount):
    return money_on_hand + amount


#TODO: Keep track of money successfully taken
#TODO: Process coins; quarters, dimes, nickles, pennies;
# return overage (“Here is $2.45 dollars in change.”),
# return if under what is owned (“Sorry that's not enough money. Money refunded.”)
def handle_money(coffee_type):
    global total_money
    coin_type = {"quarters": .25,
                 "dimes": .10,
                 "nickles": .05,
                 "pennies": .01,
                 }
    total_given = 0

    print("Please insert coins.")
    for coin in coin_type:
        total_given += int(input(f"how many {coin}?")) * coin_type[coin]

    if total_given > MENU[coffee_type]['cost']:
        print(f"Here is ${total_given - MENU[coffee_type]['cost']:.2f} in change")
        total_money += MENU[coffee_type]['cost']
        return True
    elif total_given == MENU[coffee_type]['cost']:
        total_money += MENU[coffee_type]['cost']
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def handle_resources(coffee_type):
    for resource in MENU[coffee_type]['ingredients']:
         resources[resource] -= MENU[coffee_type]['ingredients'][resource]

#TODO: Prompt User "What would you like? (espresso/latte/cappuccino):" ; repeats after completing task
#TODO: Make Coffee.
def make_coffee():
    is_on = True
    while is_on:
        customer_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if customer_input == "espresso" or customer_input == "latte" or customer_input == "cappuccino":
            if check_resources(customer_input):
                if handle_money(customer_input):
                    handle_resources(customer_input)
                    print(f"Here is your {customer_input}. Enjoy!")
        if customer_input == 'report':
            output_report()
        #TODO: Turn off by typing "off"
        if customer_input == 'off':
            is_on = False

make_coffee()










