import data

MENU = data.MENU
resources = data.resources

machine_on = True


def pay():
    water_required = MENU[user_input]["ingredients"]["water"]
    milk_required = MENU[user_input]["ingredients"]["milk"]
    coffee_required = MENU[user_input]["ingredients"]["coffee"]
    cost = MENU[user_input]["cost"]
    if user_input != "report" and user_input != "off":
        for i in resources:
            if resources[i] >= water_required and resources[i] >= milk_required and resources[i] >= coffee_required:
                print("Please insert coins.")
                quarters = int(input("How many quarters? ")) * .25
                dimes = int(input("How many dimes? ")) * .10
                nickels = int(input("How many nickels? ")) * .05
                pennies = int(input("How many pennies? ")) * .01
                total_money_inserted = quarters + dimes + nickels + pennies
                if total_money_inserted > cost:
                    change = total_money_inserted - cost
                    print(f"Here is ${change:.2f} in change.")
                    print(f"Here is your {user_input} ☕ Enjoy!")
                    update_resources(total_money_inserted_local=total_money_inserted,
                                     water_required=water_required,
                                     milk_required=milk_required,
                                     coffee_required=coffee_required)
                    break
                elif total_money_inserted < cost:
                    print("Sorry that's not enough money. Money Refunded")
                    break
                else:
                    print(f"Here is your {user_input} ☕ Enjoy!")
                    update_resources(total_money_inserted_local=total_money_inserted,
                                     water_required=water_required,
                                     milk_required=milk_required,
                                     coffee_required=coffee_required)
                    break
            else:
                is_enough = check_resources(user_input_local=user_input)
                if not is_enough:
                    break


def check_resources(user_input_local):
    for i in MENU[user_input_local]["ingredients"]:
        for item in resources:
            if MENU[user_input_local]["ingredients"][i] >= resources[item]:
                print(f"Sorry there is not enough {item}")
                return False
    return True


def entry():
    if user_input == "report":
        for i in resources:
            if i == "water" or i == "milk":
                print(f"{i.title()}: {resources[i]}ml")
            elif i == "coffee":
                print(f"{i.title()}: {resources[i]}g")
            elif i == "money":
                print(f"{i.title()}: ${resources[i]:.2f}")
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        pay()


def update_resources(total_money_inserted_local, water_required, milk_required, coffee_required):
    resources["money"] += total_money_inserted_local
    resources["water"] -= water_required
    resources["milk"] -= milk_required
    resources["coffee"] -= coffee_required


while machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        print("Goodbye")
        machine_on = False
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino" or user_input == "report":
        entry()
    else:
        print("Sorry, invalid entry. Please try again.")


