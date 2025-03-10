class Restaurant:
    def __init__(self,name,cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"Welcome! To {self.name} restaurant, we are a {self.cuisine} restaurant.")
    def open_restaurant(self):
        print(f"Welcome! {self.name} is open.")


restaurant = Restaurant('Wendy','continental')
print(restaurant.name)
print(restaurant.cuisine)
restaurant.describe_restaurant()
restaurant.open_restaurant()