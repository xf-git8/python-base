def describe_pet(animal_type,pet_name):
    """
    display a information about a pet
    :param animal_type:
    :param pet_name:
    :return:
    """
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")
describe_pet("dog","小黑")
describe_pet("cat","皮皮")