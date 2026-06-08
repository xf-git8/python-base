def make_pizza(size,*toppings):
    print("making a {size}-inch pizza with the following topping:")
    for topping in toppings:
        print(f"-{topping}")
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green pepper','extra cheess')
