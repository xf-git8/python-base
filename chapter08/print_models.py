from typing import List

def print_models(unprinted_designs, completed_models) -> List:
    while unprinted_designs:
        current_model = unprinted_designs.pop()
        print(f"print model:{current_model}")
        completed_models.append(current_model)
    return completed_models


def show_completed_models(completed_models):
    completed_models.reverse()
    for completed_model in completed_models:
        print(completed_model, end=" ")


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# for unprinted_design in unprinted_designs:
#     print(unprinted_design,end=",")
completed_models = print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
