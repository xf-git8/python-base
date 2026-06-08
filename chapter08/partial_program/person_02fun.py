
def build_person(first_name,last_name,age=None):
    """
    Return a dict of information about a person
    :param first_name:
    :param last_name:
    :param age:
    :return:
    """
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person
musician = build_person("jimi","hendrix",age=27)
print(musician)