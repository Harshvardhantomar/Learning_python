river_dict = {'Ganga':'India',"Nile":"Egypt","Amazon":'Amazon jungle'}

for key,value in river_dict.items():
    print(f"The {key} river runs through {value}")

print("\n")
print("The rivers mentioned are:")
for counter,riv in enumerate(river_dict.keys(),start=1):
    print(f"{counter}. {riv}")

print("\n")
print("The countries of Origin are:")

for country in river_dict.values():
    print(country)