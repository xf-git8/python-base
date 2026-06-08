# have elements list pop() and another empty_list append()
# print add element list
from typing import List
def print_model(unprinted_designs, completed_models) -> List[str]:
    """
    unprinted_designs pop()nd completed_models append()
    :param unprinted_designs:
    :param completed_models:
    :return:
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        completed_models.append(current_design)
    return completed_models


def show_completed_models(completed_models) -> None:
    """
    show element list in completed_models
    :param completed_models:
    :return:
    """
    completed_models.reverse()
    for complete_model in completed_models:
        print(complete_model,end=",")

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
complete_models = []
completed_models = print_model(unprinted_designs,complete_models)
show_completed_models(completed_models)