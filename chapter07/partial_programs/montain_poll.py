# use dict print like mountain
# define empty dict
responses= {}
# set a flag to indicate that polling is active
polling_active = True
while polling_active:
    # input person's name and response
    name = input("what's your name?")
    response = input("Which mountain would you like to climb someday?")
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat =="no":
        polling_active = False
print(responses)
for name,response in responses.items():
    print(f"{name} like climb to  {response}")