available_toppings = ['mushrooms', 'olives', 'green peppers',
                        'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_toppign in requested_toppings:
    if requested_toppign in available_toppings:
        print(f"Adding{requested_toppign}")
    else:
        print(f"Sorry,we don't have {requested_toppign}")
print("\nFinished make your pizza!")
