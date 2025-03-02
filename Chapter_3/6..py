My_Idols = ["Mother","Bruce Lee","Chadwick Boseman","Robert Downey Jr.","Tom Holland"]
print(f"Hi {My_Idols[0]}, I would love to invite you for dinner.")
print(f"Hi {My_Idols[1]}, I would love to invite you for dinner.")
print(f"Hi {My_Idols[2]}, I would love to invite you for dinner.")
print(f"Hi {My_Idols[3]}, I would love to invite you for dinner.")
print(f"Hi {My_Idols[4]}, I would love to invite you for dinner.\n\n")

print("Oh no, I heard Tom Holland can't make to the dinner, but Joe Rogan is free\n\n")
My_Idols[-1]= "Joe Rogan"

print(f"Hi {My_Idols[0]}, I would love to invite you for dinner.")
print(f"Hi {My_Idols[1]}, I would love to invite you for dinner.")
print(f"Hi {My_Idols[2]}, I would love to invite you for dinner.")
print(f"Hi {My_Idols[3]}, I would love to invite you for dinner.")
print(f"Hi {My_Idols[4]}, I would love to invite you for dinner.\n\n")


print("Alert: Guys I found a bigger table for dinner, we can have more people to the party\n")

My_Idols.insert(0,"Father")
mid = len(My_Idols)
My_Idols.insert(int(mid/2),"Jackie Chan")
My_Idols.append("Shahrukh Khan")

for idol in My_Idols:
    print(f"Hi {idol}, I would love to invite you for dinner.")
