from classes import Room
from classes import Player

### outdoor
outdoor = Room(name='draußen', description='Draußen siehst du nichts')
outdoor.items.append('test1')

### room1
room1 = Room(name='room1', description='Raum1 ist geil')
outdoor.items.append('test2')

#x = outdoor
x = input('wo gehst du hin\n')
player = Player('Robert', outdoor)
player.move(x)

