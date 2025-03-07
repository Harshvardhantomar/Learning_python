sandwich_orders = ['Pastrami','Panner tikka','chesse corn','Bombay chesse grill','vada pav','Pastrami']

finished_sandwiches = []

index = 0
while index <len(sandwich_orders):

    sandwich = sandwich_orders[index].title()
    index +=1
    if(sandwich=='Pastrami'):
        print(f"Sorry! We have run out of {sandwich}.")
        continue
    else:
        print(f"Your {sandwich.title()} sandwich has been made.")
    finished_sandwiches.append(sandwich)
    

print(finished_sandwiches)