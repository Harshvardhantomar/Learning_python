fav_pizza = ["Farm House","Indi-tandoori","Peppy Paneer"]

print("My Favorite Pizzas are:")
for pizza in fav_pizza:
    print(pizza)
print("\n\n")


friend_fav_pizza = fav_pizza[:]
friend_fav_pizza2 = fav_pizza

# I have copied, the my list of favorite pizza in 2 different ways.

#The list of my friend_fav_pizza has copied the instance of the list at that time, and doesn't point to my list.
#The second of my friend_fav_pizza has copied the reference of my list and now points to the same location as my list and therefore any change in this list of the original list is shown in both.


friend_fav_pizza.append("Chicken supreme")
fav_pizza.append("Crispy corn")
friend_fav_pizza2.append("Onion and tomato")

print("My Favorite Pizzas are:")
for pizza in fav_pizza:
    print(pizza)
print("\n\n")

print("My 1st Friend Favorite Pizzas are:")
for pizza in friend_fav_pizza:
    print(pizza)
print("\n\n")

print("My 2nd Friend Favorite Pizzas are:")
for pizza in friend_fav_pizza2:
    print(pizza)
print("\n\n")