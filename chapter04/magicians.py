# list  for loop and list condition comprehensions print element
magicians = ["alice", "david", "carolina"]
for magician1 in magicians:
    print(magician1)

magician2 = [magician for magician in magicians if len(magician) >6]
print(magician2)
