MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
             "milk": 0
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

def coffee_maker(ingredients_dict,resources):
    water_required=ingredients_dict["ingredients"]["water"]
    milk_required=ingredients_dict["ingredients"]["milk"]
    coffee_required=ingredients_dict["ingredients"]["coffee"]
    if(water_required>resources["water"] ):
        print("Sorry, there is not enough water")
        return False
    elif(milk_required>resources["milk"] ):
        print("Sorry, there is not enough milk")
        return False
    
    elif(coffee_required>resources["coffee"]):
        print("Sorry, there is not enough coffee")
        return False
    
    else:
        resources["water"]=resources["water"]-water_required
        resources["milk"]=resources["milk"]-milk_required
        resources["coffee"]=resources["coffee"]-coffee_required
        return True

def money_checker(coffee_dict):
    required_money=coffee_dict["cost"]
    print("Please insert coins.")
    quarters=int(input("How many quarters?: "))
    dimes=int(input("How many dimes?: "))
    nickles=int(input("How many nickles?: "))
    pennies=int(input("How many pennies?: "))
    total_money= ((25*quarters)+(10*dimes)+(5*nickles)+(pennies)) / 100
    if(total_money<required_money):
        print("Sorry that's not enough money. Money refunded.") 
        return False
    else:
        money_left=total_money-required_money
        print(f"Here is ${money_left:.2f} in change.") 
        return True
       
     
def print_report(resources,revenue):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${revenue}")
def coffee_machine():
    revenue=0
    flag=True
    while(flag):
        coffee=input("What would you like? (espresso/latte/cappuccino): ")
        if(coffee=="espresso" or coffee=="cappuccino" or coffee=="latte"):
            has_ingredients=coffee_maker(MENU[coffee],resources)  
            if(has_ingredients):
                    has_money=money_checker(MENU[coffee]) 
                    if(has_money): 
                        revenue+=MENU[coffee]["cost"]
                        print(f"Here's your required {coffee} ☕. Enjoy!")
            
        elif(coffee=="report"):
            print_report(resources,revenue)
            
        elif(coffee=="off"):
            return 0

        
coffee_machine()