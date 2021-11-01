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
postbox = Objects(name='Briefkasten', description='Ein Briefkasten - haben wir Post?', searchable=True, inventory=[])

# doormat
doormat = Objects(name='Matte', description='Schöne Fußmatte.', searchable=True, inventory=[])

# stone
stone = Objects(name='Stein', description='Komischer Stein - da war doch was damit oder?', searchable=True, inventory=[key])

# frontdoor
frontdoor = Objects(name='Haustür', description='Die Haustür. Um sie aufzumachen benötigst du einen Schlüssel.', searchable=True, inventory=[key])

# gate
gate = Objects(name='Garagentor', description='Das Garagentor ist kaputt. Momentag kann es nicht geöffnet werden.', searchable=True, inventory=[key])

# window
window = Objects(name='Fenster', description='Das Fenster scheint offen zu sein. Du könntest durchs Fenster hinkommen. ', searchable=True, inventory=[key])

# bedroom_boxes
bedroom_boxes = Objects(name='Schlafzimmer Boxen', description='Die Kisten im Schlafzimmer. Was ist hier wohl drin?', searchable=True, inventory=[key])

# workbench
workbench = Objects(name='Werkbank', description='Tolle Werkbank. Gerade kannst du sie nicht gebrauchen.', searchable=True, inventory=[key])

# car
car = Objects(name='Auto', description='Dein Auto. Vielleicht ist noch was im Kofferraum?', searchable=True, inventory=[key])

# trunk
trunk = Objects(name='Kofferraum', description='War noch was im Kofferraum?', searchable=True, inventory=[key])

# chair
chair = Objects(name='Stuhl', description='Dein Bürostuhl. Du brauchst ihn für dein Arbeitszimmer.', searchable=True, inventory=[key])

# table
table = Objects(name='Tisch', description='Komischer Stein - da war doch was damit oder?', searchable=True, inventory=[key])

# fridge
fridge = Objects(name='Kühlschrank', description='Komischer Stein - da war doch was damit oder?', searchable=True, inventory=[key])

# storeroom_box
storeroom_box = Objects(name='Abstellkammer-Box', description='Die Kiste in Abstellkammer. Was ist hier wohl drin?', searchable=True, inventory=[key])

# bathroom_boxes
bathroom_boxes = Objects(name='Badezimmer-Boxen', description='Die Kisten im Badezimmer. Was ist hier wohl drin?', searchable=True, inventory=[key])


### Powerbox Class (activateable stuff) ###

# powerbox
powerbox = Powerbox(name='Stromkasten', description='Der Stromkasten. Sind alle Sicherung drin?', active=False)


### Coffeemachine Class (Stuff that creates something) ###

# coffeemachine
coffeemachine = Coffeemachine(name='Kaffeemaschine', description='Ob der Kaffee wohl schmeckt?', inventory=[],
                              active=False)

### Room Class ###

# outdoor
outdoor = Room(name='Draußen', description='Draußen siehst ', items=[postbox, doormat, stone, frontdoor, gate, window],
               person=[])

# bedroom
bedroom = Room(name='Schlafzimmer', description='In diesem Zimmer siehst ', items=[bedroom_boxes, window],
               person=[Berty])

# garage
garage = Room(name='Garage', description='In diesem Zimmer siehst ', items=[workbench, car, trunk, chair],
              person=[])

# livingroom
livingroom = Room(name='Wohnzimmer', description='In diesem Zimmer siehst ', items=[table, coffeemachine, fridge],
                  person=[])

# storeroom
storeroom = Room(name='Abstellkammer', description='In diesem Zimmer siehst ', items=[storeroom_box, powerbox],
                 person=[])

# workroom
workroom = Room(name='Arbeitszimmer', description='In diesem Zimmer siehst ', items=[], person=[])

# bathroom
bathroom = Room(name='Badezimmer', description='In diesem Zimmer siehst ', items=[bathroom_boxes], person=[])

