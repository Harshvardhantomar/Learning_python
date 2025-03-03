food_menu = ("Masala Dosa","Idli Sambhar","Chole Bhature","Aloo Paratha","Kadhi Chawal")

for food in food_menu:
    print(food)

print("\n\n")
# food_menu[-1] = "Dal Chawal" this doesn't work as the tuple can't be modified.

food_menu = ("Masala Dosa","Pav Bhaji","Chole Kulche","Paneer Paratha","Dal Chawal")

for food in food_menu:
    print(food)

#This works because we are reassinging the variable and not modifying the tuple.