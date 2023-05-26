pizzas = ['dml','kfc','mc']
for pizza in pizzas:
    print(pizza)
    print("I love " + pizza.upper() +  " pizza")
print(pizzas[0] + " is big\n" + pizzas[1] + " is dilicious.\n" + pizzas[2] + " is cheap.\n" + "I really love pizza")

pizzas_copy = pizzas[:]
pizzas.append('ls1')
pizzas_copy.append('ls2')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in pizzas_copy:
    print(pizza)