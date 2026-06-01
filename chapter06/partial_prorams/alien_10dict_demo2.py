# demo: make dict in list and print dict slice top five
import random
# make an empty list for store aliens
aliens = []
# make dict join in list
for alien in range(30):
    new_alie = {'color': 'green', 'points': random.randint(1, 30), 'speed': 'slow'}
    aliens.append(new_alie)
# make top three dict value by key
for alien in aliens[:3]:
    print(alien)
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['points'] = random.randint(1,30)
        alien['speed'] = 'medium'
# print one and five dict element use index slice
for alien in aliens[:5]:
    print(alien)
# print make dict num
print(f"Total num of aliens:{len(aliens)}")