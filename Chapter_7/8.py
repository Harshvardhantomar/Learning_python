sandwich_orders = ['Panner tikka','chesse corn','Bombay chesse grill','vada pav']

finished_sandwiches = []

index = 0
while index <len(sandwich_orders):
    sandwich = sandwich_orders[index].title()
    print(f"Your {sandwich.title()} sandwich has been made.")
    finished_sandwiches.append(sandwich)
    index +=1

print(finished_sandwiches)