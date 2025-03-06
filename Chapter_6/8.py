pet_1 = {"Owner name":'Harsh','Pet type':'dog','pet name':'sushi'}
pet_2 = {"Owner name":'Simon','Pet type':'dog','pet name':'lilo'}
pet_3 = {"Owner name":'Prassidhi','Pet type':'dog','pet name':'jumbo'}
pet_5 = {"Owner name":'talia','Pet type':'dog','pet name':'mushu'}
pet_6 = {"Owner name":'jj','Pet type':'cat','pet name':'beerus'}
pet_4 = {"Owner name":'vik','Pet type':'dog','pet name':'ralph'}

pets = [pet_1,pet_2,pet_3,pet_4,pet_5,pet_6]

for pet in pets:
    for detail,name in pet.items():
        print(f"{detail.title()}:{name.title()}")
    print("\n")