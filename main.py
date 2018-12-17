import sys

from mobile_operator import Operator
from search import search

operators = int(input('Enter number of operators : '))
operator_objs = []
for i in range(operators):
    name = input('Enter name of operator : ')
    prefixes = int(input('Enter number of prefix supported by {} : '.format(name)))
    prices = {}
    for j in range(prefixes):
        key, value = input('Enter prefix price pairs for operator {} as PREFIX PRICE : '.format(name)).strip().split()
        prices[key] = value
    operator = Operator(name=name, prices=prices)
    operator_objs.append(operator)

phone_number = input('Enter telephone no to search : ')
cheapest_price, cheapest_operator = search(operator_objs, phone_number)
sys.stdout.write('Best suited operator for {} is {} charging {} USD/min\n'.format(phone_number, cheapest_operator, cheapest_price ))



