# use slice and dict change dict value
import random
aliens = []
for alien in range(30):
    new_alien = {'color': 'green', 'points': random.randint(20, 50), 'speed': 'medium'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] =='green':
        alien['color'] = 'red'
        alien['points'] = random.randint(1,10)
        alien['speed'] = 'slow'
for alien in aliens[:5]:
    print(alien)