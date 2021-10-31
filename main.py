from classes import *
import fnmatch

print('Hallo und herzlich Willkommen zu unserem Textabenteuer.\nZiel ist es alle Gegenstände deines'
      ' Computers zu finden und sie in einem bestimmten Raum zu bringen.'
      '\nDu kannst immer folgendes tun: \numschauen, nehmen, geben, ansprechen, benutzen, öffnen, gehen\n')

# enter playername
PlayerName = ''
# doesnt allow empty input
while PlayerName == '':
    try:
        PlayerName = input('Bitte geben deinen Namen ein.\n')
    except:
        print('Some Error occurred')

print('Hallo', PlayerName, '!\nWir wünschen dir viel Erfolg!')

print('\n\nDu kommst von der Arbeit nach Hause und stehst ohne Schlüssel vor der Tür.')

game = True
# starting room
room = outdoor
# starting inventory
inventory = []
# players name, starting room and inventory
Player(PlayerName, room, inventory)

while game:
    x = [input('Was machst du nun?\n')]
    try:
        if fnmatch.filter(x, '*schau*'):
            print('Du schaust dich um und siehst ' + room.description)

        elif fnmatch.filter(x, '*nehm*'):
            print('Du schaust dich um und siehst ' + ' die Variable Nichts')

        elif fnmatch.filter(x, '*geb*'):
            print('Du schaust dich um und siehst ' + ' die Variable Nichts')

        elif fnmatch.filter(x, '*sprech*'):
            print('Du schaust dich um und siehst ' + ' die Variable Nichts')

        elif fnmatch.filter(x, '*benutz*'):
            print('Du schaust dich um und siehst ' + ' die Variable Nichts')

        elif fnmatch.filter(x, '*öffne*'):
            print('Du schaust dich um und siehst ' + ' die Variable Nichts')

        elif fnmatch.filter(x, '*geh*'):

            Player.move(self=Player,position=outdoor)

            print('Du gehst in', outdoor.name, 'und dir fallen folgende Sachen auf:')
            for item in outdoor.items:
                print(item)

        else:
            print('Das kannst du leider nicht machen.')

    except:
        print('Das kannst du nicht machen.\n')



