from objects import *


def connection_check(x, y):
    for connection in room_connections:
        if x in connection:
            if y in connection:
                return True
