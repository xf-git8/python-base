def get_formatted_name(fist_name, last_name) -> str:
    """
    Return a full_name by the function
    :param fist_name:
    :param last_name:
    :return:
    """
    full_name = f"{last_name}{fist_name}"
    return full_name
"""This is  an infinite loop"""
while True:
    print("please input your name:")
    print("enter 'q' at any time to quit")
    first_name = input("First_name:")
    if first_name == 'q':
        break
    last_name = input("Last_name:")
    if last_name == 'q':
        break
    formatted_name = get_formatted_name(first_name,last_name)
    print(f"Hello,{formatted_name}")
