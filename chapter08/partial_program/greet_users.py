def gree_users(names):
    """Print a simple greeting each user in the last"""
    for name in names:
        msg = f"hello ,{name.title()}"
        print(msg)
usernames =['hannh','ty','margot']
gree_users(usernames)