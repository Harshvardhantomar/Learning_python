def makeSandwiches(*items):
    print("You ordered a sandwich with:")
    for item in items:
        print(f"\t{item.title()}")


makeSandwiches('Paneer')
makeSandwiches('Chesse','Paneer','Cucumber')