# user  few dict value print make a value
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },

    }
for username,userinfo in users.items():
    print(f"{username}:",end=" ")
    full_name = f"{userinfo['first'].title()}{userinfo['last']}"
    print(full_name)
    location = userinfo['location']
    print(f"{full_name} is live in {location}")