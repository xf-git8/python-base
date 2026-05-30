# use list comprehensions with range
squares = [value ** 2 for value in range(1, 11)]
print(squares)
# use list comprehensions with range by condition
squares2 = [value ** 2 for value in range(1, 11) if value % 2 == 0]
print(squares2)