#7-8
# sandwich_orders = ['Ham Sandwich', 'Chicken Sandwich', 'Beef Sandwich', 'Vegetarian Sandwich']
# finished_sandwiches = []

# active = True
# while active:
#     if sandwich_orders:
#         for sandwich_order in sandwich_orders:
#             print("I made your " + sandwich_order)
#             finished_sandwiches.append(sandwich_orders.pop(0))
#     else:
#         active = False
# print("These are finished sandwiches:" + "\n" + str(finished_sandwiches))

#7-9
print("Pastrami has been sold out!")
sandwich_orders = ['Ham Sandwich', 'Pastrami Sandwich', 'Chicken Sandwich', 'Pastrami Sandwich', 'Beef Sandwich', 'Vegetarian Sandwich', 'Pastrami Sandwich']
finished_sandwiches = []


while 'Pastrami Sandwich' in sandwich_orders:
    sandwich_orders.remove('Pastrami Sandwich')

active = True
while active:
    if sandwich_orders:
        for sandwich_order in sandwich_orders:
            print("I made your " + sandwich_order)
            finished_sandwiches.append(sandwich_orders.pop(0))
    else:
        active = False
print("These are finished sandwiches:" + "\n" + str(finished_sandwiches))
