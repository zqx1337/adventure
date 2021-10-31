class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def move(self, room):
        self.position = self.position
        print('Spieler geht in Raum ' + room)

    def open(self):
        print('test')

    def take(self):
        print('test')

    def look(self):
        print('test')

#class inventory:


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

### Draußen
outdoor = Room(name='draußen', description='Draußen siehst du nichts')
outdoor.items.append('test1')




#class person:
'''
class Objects:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Coffemachine(Objects):
    def __init__(self, name, description):
        Objects.__init__(self, name, description)
    def makes_coffe()
'''
