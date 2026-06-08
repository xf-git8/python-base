
def get_formatted_name(first_name,middle_name,last_name):
    """
    Return a full name,neatly formatted
    :param first_name:
    :param middle_name:
    :param last_name:
    :return:
    """
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name
musician = get_formatted_name("jhin", "lee", "hooker")
print(musician)