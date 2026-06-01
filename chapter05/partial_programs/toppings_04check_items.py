# use for and list check items with if-else
requested_toppings = ["mushrooms","green peppers","extra cheese"]
for requested_topping in requested_toppings:
    if requested_toppings =="green peppers":
        print("Sorry,we are out of green peppers right now")
    else:
        print(f"Adding {requested_topping}")
print("\nFinished making your pizza!")