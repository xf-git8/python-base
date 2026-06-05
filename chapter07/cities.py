# use while and count control input
prompt = "please enter the name of a city you have visited"
prompt += "\nenter 'quit' when you are finished.\ncity_name:"
count = 0
while True:
    city = input(prompt)
    count += 1
    if city == "quit" or count==4:
        print("You don't have chance input")
        break
    else:
        print(f"I'd love to go {city.title()}")
