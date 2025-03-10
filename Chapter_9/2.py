class Restaurant:
    def __init__(self,name,cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"Welcome! To {self.name} restaurant, we are a {self.cuisine} restaurant.")
    def open_restaurant(self):
        print(f"Welcome! {self.name} is open.")


restaurant = Restaurant('Wendy','continental')
restaurant1= Restaurant("Domnio's",'Italian')
restaurant2= Restaurant("Taj",'Indian')

restaurant.describe_restaurant()
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
