from huggingface_hub import duplicate_space


def describe_pet(animal_type,pet_name):
    """
    display information about a pet
    :param animal_type:
    :param pet_name:
    :return:
    """
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")
describe_pet(animal_type="hamster",pet_name="harry")
