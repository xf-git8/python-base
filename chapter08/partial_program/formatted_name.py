def get_formatted_name(first_name,last_name):
    """
    Return a  full_name neatly formatted
    :param first_name:
    :param last_name:
    :return:
    """
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name("jimi","hendrix")
print(musician)
