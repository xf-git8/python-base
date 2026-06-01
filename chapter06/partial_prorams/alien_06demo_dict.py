# use dict's value change other value by condition
alien_dict = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original alien_dict:{alien_dict}")
# use dict get condition value and judge
if alien_dict['speed'] == 'slow':
    x_increment = 1
elif alien_dict['speed'] =='medium':
    x_increment = 2
else:
    x_increment = 3
#  change's dict value
alien_dict['x_position'] = alien_dict['x_position']+ x_increment
print(f"New alien_dict:{alien_dict}")
