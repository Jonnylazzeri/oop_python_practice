# from turtle import Turtle, Screen
# timmy = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkOliveGreen4")
# timmy.fd(100)
#
# my_screen = Screen()
#
# print(my_screen.canvheight)
# my_screen.exitonclick()
#
#
# from prettytable import PrettyTable
#
# table = PrettyTable()
#
# table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
# table.add_column("Type", ['Electric', 'Water', 'Fire'])
# table.align = 'l'
# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
items = menu.get_items()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

running = True
while running:
    query = input(f'What drink would you like to order? {items}: ')
    if query == 'report':
        coffee_maker.report()
        money_machine.report()
    elif query == 'exit':
        running = False
        break
    else:
        coffee = menu.find_drink(query)
        if coffee:
            sufficient = coffee_maker.is_resource_sufficient(coffee)
            if sufficient:
                payment = money_machine.make_payment(coffee.cost)
                if payment:
                    coffee_maker.make_coffee(coffee)
