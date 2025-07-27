my_favorite_pizza = ['chicken', 'beef', 'vegetable grill']
my_friends_pizza = my_favorite_pizza[:]
#Adding a new pizza to the original list.
my_favorite_pizza.append("pepperoni")
#Adding a different pizza to the list friend_pizzas.
my_friends_pizza.append('cheese')

print("My favorite pizzas are:")
for pizza in my_favorite_pizza:
    print("- " + pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in my_friends_pizza:
    print("- " + pizza)