# print make pizza for loop with *variable and other variables
def make_pizza(size, *toppings):
    print("making a pizza with the following topping")
    for topping in toppings:
        print(f"{size}寸大小：include-{topping}")


make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green pepper", "extra cheese")
