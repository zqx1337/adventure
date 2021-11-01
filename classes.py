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


class Person:
    def __init__(self, name, description):
        self.name = name
        self.description = description


# searchable objects
class Objects:
    def __init__(self, name, description, searchable, inventory):
        self.name = name
        self.description = description
        self.searchable = searchable
        self.inventory = inventory


# collectable stuff
class Items(Objects):
    def __init__(self, name, description, collectable):
        self.name = name
        self.description = description
        self.collectable = collectable

# producing stuff
class Coffeemachine(Objects):
    pass
    def __init__(self, name, description, inventory, active):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.active = active
    def makes_coffe(self):
        print('Die Kaffeemaschine geht an und macht einen Kaffee')
        self.activate = True


# activatable stuff
class Powerbox(Objects):
    pass
    def __init__(self, name, description, active):
        self.name = name
        self.description = description
        self.active = active
    def activate_power(self):
        print('Der Strom geht an.')


class Room:
    def __init__(self, name, description, items, person):
        self.name = name
        self.description = description
        self.items = items
        self.person = person


