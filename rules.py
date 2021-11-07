from objects import *


# returns True or False if rooms are connected or not
def connection_check(room1, room2):
    for connection in room_connections:
        if room1 in connection:
            if room2 in connection:
                return True


