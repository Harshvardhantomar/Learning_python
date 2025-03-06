person1_dic = {
    'first_name':'Harshvardhan',
    'last_name':'Tomar',
    'age':24,
    'city':"Gwalior",
    'Hobbies':'Football'
}

person2_dic = {
    'first_name':'Anshuman',
    'last_name':'Tomar',
    'age':27,
    'city':"Orcha",
    'Hobbies':['cricket','movies']
}

person3_dic = {
    'first_name':'Ranbir',
    'last_name':'Kapoor',
    'age':34,
    'city':"Mumbai",
    'Hobbies':['Football','Acting']
}

persons = [person1_dic,person2_dic,person3_dic]
a=1
for person in persons:
    print(f"Details about Person {a}")
    for details,values in person.items():
        print(f"{details.title()}: {values}")
    a+=1
    print("\n")


