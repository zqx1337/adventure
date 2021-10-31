class Player:
    def __init__(self, name, position, inventory):
        self.name = name
        self.position = position
        self.inventory = inventory

    def move(self, position):
        self.position = position
        print('Spieler geht ', position.name,'.')

    def open(self):
        print('Du versuchst', x, 'öffnen.')

    def take(self):
        print('Du versuchst', x, 'aufzunehmen.')

    def look(self):
        print('testtest')

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

# outdoor
outdoor = Room(name='Draußen', description='Draußen siehst du nichts', items=['Matte, Schlüssel, Tor'])

# bedroom
bedroom = Room(name='Schlafzimmer', description='In diesem Zimmer siehst ', items=['Tastatur, Rechner'])

# garage
garage = Room(name='Garage', description='In diesem Zimmer siehst ', items=['Tastatur, Rechner'])

# livingroom
livingroom = Room(name='Wohnzimmer', description='In diesem Zimmer siehst ', items=['Tastatur, Rechner'])

# storeroom
storeroom = Room(name='Abstellkammer', description='In diesem Zimmer siehst ', items=['Tastatur, Rechner'])

# workroom
workroom = Room(name='Arbeitszimmer', description='In diesem Zimmer siehst ', items=['Tastatur, Rechner'])

# bathroom
bathroom = Room(name='Badezimmer', description='In diesem Zimmer siehst ', items=['Tastatur, Rechner'])


class Person:
    def __init__(self, name, description):
        self.name = name
        self.description = description

# bathroom
Berty = Person(name='Berty', description='Schläfriger Typ, könnte einen Kaffee gebrauchen.')


# usable objects
class Objects:
    def __init__(self, name, description, status):
        self.name = name
        self.description = description
        self.status = status


# postbox
postbox = Objects(name='Briefkasten', description='Ein Briefkasten - haben wir Post?', status=False)

# doormat
doormat = Objects(name='Fußmatte', description='Schöne Fußmatte - da war doch was damit oder?', status=False)

class Items(Objects):
    def __init__(self, name, description, status, taken):
        self.name = name
        self.description = description
        self.status = status
        self.taken = taken

class Coffeemachine(Objects):
    pass
    def makes_coffe(self):
        print('Die Kaffeemaschine geht an und macht einen Kaffee')


