def describe_pet(pet_name,animal_type="dog"):
    """
    display a information about a dog with dict use define instead of default
    :param pet_name:
    :param animal_type:
    :return:
    """
    pet = {'pet_name':pet_name,'animal_type':animal_type}
    print(pet)
describe_pet("cc",animal_type="rabbit")