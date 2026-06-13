# input two number and use while control
print("please give me two nubmers,adn I'll divide them")
print("Enter 'q' to quit")
while True:
    first_number=input("First number:")
    if first_number == 'q':
        break
    second_number = input("Second_number")
    if second_number == 'q':
        break
    answer = int(first_number)/int(second_number)
    print(answer)