class Restaurant:
    def __init__(self,name,cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def about_number_of_guest(self):
        print(f"We have served {self.number_served} people today!")
    def describe_restaurant(self):
        print(f"Welcome! To {self.name} restaurant, we are a {self.cuisine} restaurant.")
    def open_restaurant(self):
        print(f"Welcome! {self.name} is open.")
    def set_number_served(self,guest_num):
        self.number_served=guest_num
    def increment_number_served(self,new_guest):
        if(new_guest>0):
            self.number_served+=new_guest
        else:
            print("We can't reduced the number of people served.")



class IceCreamStand(Restaurant):
    def __init__(self,name,cuisine):
        super().__init__(name,cuisine)
        self.flavors = ['Vanilla','Chocolate','Strawberry','ButterScoth','Caramel Salted']

    def describe_flavors(self):
        print("These are the available flavors:")
        for flavor in self.flavors:
            print(f"\t{flavor}")


icecreamstand = IceCreamStand('Baskin Robin','Desert')

icecreamstand.describe_flavors()
icecreamstand.describe_restaurant()

    
