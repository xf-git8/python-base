# have elements list pop() and another empty_list append()
# print add element list
unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing  model:{current_design}")
    completed_models.append(current_design)
print("The following models have been printed:")
for completed_model in completed_models:
    print(completed_model,end=" ")