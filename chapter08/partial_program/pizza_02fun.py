# print make pizza for loop with *variable
def make_pizza(*toppings):
    print("making a pizza with the following topping")
    for topping in toppings:
        print(f"-{topping}")
make_pizza("pepperoni")
make_pizza("mushrooms","green pepper","extra cheese")