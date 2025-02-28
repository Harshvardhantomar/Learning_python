famous_person= "Woody allen"
quote = "Eighty percent of success is just showing up."

length = int((len(quote))/8 -1)

position = "\t"*length
message = f'"{quote}"\n{position}{famous_person}'
print(message)
