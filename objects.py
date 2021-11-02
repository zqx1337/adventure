from classes import *

### Person Class
# berty
Berty = Person(name='Berty', description='Schläfriger Typ, könnte einen Kaffee gebrauchen.')

### Items Class (collectable stuff) ###

# keyboard
keyboard = Items(name='Tastatur', description='Eine schöne RGB-Tastatur.', collectable=True)

# key
key = Items(name='Schlüssel', description='Schlüssel für die Haustür.', collectable=True)

# coffee
coffee = Items(name='Tasse Kaffee', description='Eine leckere Tasse Kaffee.', collectable=True)

### Objects Class (searchable stuff) ###

# postbox
postbox = Objects(name='Briefkasten', description='Ein Briefkasten - scheint leer zu sein.', searched=False, inventory=[])

# doormat
doormat = Objects(name='Matte', description='Schöne Fußmatte.', searched=False, inventory=[keyboard])

# stone
stone = Objects(name='Stein', description='Komischer Stein - da war doch was damit oder?', searched=False, inventory=[key])

# frontdoor
frontdoor = Objects(name='Haustür', description='Die Haustür. Um sie aufzumachen benötigst du einen Schlüssel.', searched=False, inventory=[])

# gate
gate = Objects(name='Garagentor', description='Das Garagentor ist kaputt. Momentan kann es nicht geöffnet werden.', searched=False, inventory=[])

# window
window = Objects(name='Fenster', description='Das Fenster scheint offen zu sein. Du könntest durchs Fenster ins Haus kommen. ', searched=False, inventory=[])

# bedroom_boxes
bedroom_boxes = Objects(name='Schlafzimmer Boxen', description='Die Kisten im Schlafzimmer. Was ist hier wohl drin?', searched=False, inventory=[])

# workbench
workbench = Objects(name='Werkbank', description='Tolle Werkbank. Gerade kannst du sie nicht gebrauchen.', searched=False, inventory=[])

# car
car = Objects(name='Auto', description='Dein Auto. Vielleicht ist noch was im Kofferraum?', searched=False, inventory=[])

# trunk
trunk = Objects(name='Kofferraum', description='War noch was im Kofferraum?', searched=False, inventory=[])

# chair
chair = Objects(name='Stuhl', description='Dein Bürostuhl. Du brauchst ihn für dein Arbeitszimmer.', searched=False, inventory=[])

# table
table = Objects(name='Tisch', description='Komischer Stein - da war doch was damit oder?', searched=False, inventory=[])

# fridge
fridge = Objects(name='Kühlschrank', description='Komischer Stein - da war doch was damit oder?', searched=False, inventory=[])

# storeroom_box
storeroom_box = Objects(name='Abstellkammer-Box', description='Die Kiste in Abstellkammer. Was ist hier wohl drin?', searched=False, inventory=[])

# bathroom_boxes
bathroom_boxes = Objects(name='Badezimmer-Boxen', description='Die Kisten im Badezimmer. Was ist hier wohl drin?', searched=False, inventory=[])


### Powerbox Class (activateable stuff) ###

# powerbox
powerbox = Powerbox(name='Stromkasten', description='Der Stromkasten. Sind alle Sicherung drin?', active=False)


### Coffeemachine Class (Stuff that creates something) ###

# coffeemachine
coffeemachine = Coffeemachine(name='Kaffeemaschine', description='Vollautomatik - Eine Tasse steht schon da, '
                                                                 'du musst die Maschine nur noch anmachen.', inventory=[],
                              active=False)

### Room Class ###

# outdoor
front = Room(name='Vor dem Haus', description='', items=[postbox, doormat, stone, frontdoor, gate],
               person=[])

rear = Room(name='Hinter dem Haus', description='', items=[window],
               person=[])

# bedroom
bedroom = Room(name='Schlafzimmer', description='', items=[bedroom_boxes, window],
               person=[Berty])

# garage
garage = Room(name='Garage', description='', items=[workbench, car, trunk, chair],
              person=[])

# livingroom
livingroom = Room(name='Wohnzimmer', description='', items=[table, coffeemachine, fridge],
                  person=[])

# storeroom
storeroom = Room(name='Abstellkammer', description='', items=[storeroom_box, powerbox],
                 person=[])

# workroom
workroom = Room(name='Arbeitszimmer', description='', items=[], person=[])

# bathroom
bathroom = Room(name='Badezimmer', description='', items=[bathroom_boxes], person=[])

rooms = [bathroom, workroom, bedroom, livingroom, storeroom, garage, front, rear]

### Player Class
# Player
Player = Player(name='', position=front, inventory=[])
