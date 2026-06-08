def get_formatted_name(first_name,last_name,middle_name)->str:
    """
    Return a full name and According to condition
    :param first_name:
    :param last_name:
    :param middle_name:
    :return:
    """
    if middle_name:
        full_name = f"{last_name} {middle_name} {first_name}"
    else:
        full_name = f"{last_name}{first_name}"
    return full_name
full_name = get_formatted_name("小德","欧阳",None)
print(full_name)
