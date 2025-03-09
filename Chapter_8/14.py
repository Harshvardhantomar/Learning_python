def make_car(manufacturer,model,**car_details):
    car_details['Company']= manufacturer.title()
    car_details['Model']= model.title()
    return car_details

car = make_car('subaru','outback',color='blue',tow_package='True')
print(car)