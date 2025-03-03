cars = ["Subaru","bmw",'audi','mercedes']

for car in cars:
    if(car == 'Subaru'):
        print("Yeah Subu")
    else:
        print("CHubu")

print(cars[0].lower()=="subaru")

car = "subaru"
print( car.title() in cars)

car2 = "Hyundai"
print(car2 not in  cars)