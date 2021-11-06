from objects import *

rooms = [bathroom, workroom, bedroom, livingroom, storeroom, garage, front, rear]

room_connections = [[front, rear], [bathroom, livingroom],
                    [workroom, livingroom], [storeroom, livingroom], [garage, bedroom], [bedroom, livingroom]]


def connection_check(room1, room2):
    for connection in room_connections:
        if room1 in connection:
            if room2 in connection:
                return True


def winning(comp, player):
    if Player.position == workroom:
        if all(x in [comp] for x in [player]):
            return True
