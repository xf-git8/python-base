def build_person(first_name,last_name):
    """
    return a dict of full name about a person
    :param first_name:
    :param last_name:
    :return:
    """
    person = {'first_name':first_name,'last_name':last_name}
    return  person
musician = build_person("jimi","hendrix")
print(musician)
