from objects import *
import fnmatch

print('####################################################################'
      '\nHallo und herzlich Willkommen zu unserem Textabenteuer.\nZiel ist es alle Gegenstände deines'
      ' Computers zu finden und sie in dein Arbeitszimmer zu bringen.'
      '\n\nDu kannst immer folgendes tun: \numschauen, nehmen, geben, ansprechen, benutzen, öffnen, gehen, untersuchen\n'
      '\nFalls du erneut sehen möchtest, was du tun kannst, tippe "Hilfe" ein, ohne die Anführungszeichen :)\n')

# enter playername
PlayerName = ''
# doesnt allow empty input
while PlayerName == '':
    PlayerName = input('Bitte geben deinen Namen ein.\n')

print('\nHallo ' + PlayerName + '!\nWir wünschen dir viel Erfolg!'
      '\n\nDu kommst von der Arbeit nach Hause und stehst ohne Schlüssel vor der Tür.')

game = True
# starting room
room = outdoor
# starting inventory
inventory = []
# players name, starting room and inventory
Player(PlayerName, room, inventory)

# game is going on as long game is True
while game:

    # player inputs text, which is checked for specific pieces of words
    x = [input('\nWas machst du nun?\n')]

    # help command if commands forgotten - fnmatch is case-insensitive
    if fnmatch.filter(x, '*Hilfe*'):
        print('\nDu kannst immer folgendes tun: \numschauen, nehmen, geben, ansprechen,'
              ' benutzen, öffnen, gehen, untersuchen\n')
    else:
        try:
            # checks input for *schau* and gives out all items in the room
            # shows you the room you're in and the items available to interact with
            if fnmatch.filter(x, '*schau*'):
                print('Zur Zeit bist befindest du dich hier:')
                print(room.name)
                print('Nun schaust du dich um und siehst:')
                for item in room.items:
                    print(item.name + ' - ' + item.description)

            elif fnmatch.filter(x, '*nehm*'):
                for object in room.items:
                    # print('objekt hat inventory')
                    for item in object.inventory:
                        #for item in object.inventory:
                        if object.inventory:

                            print(item.name)
                            if fnmatch.filter(x,'*' + item.name + '*'):
                                if object.collectable == True:
                                    print('Du packst', item.name + ' in dein Inventar.')
                                    #for item in object.inventory:
                                    #print(item.name)
                                else:
                                    print('Du kannst das nicht nehmen.')
                    else:
                        print('hier ist nichts drin')


            elif fnmatch.filter(x, '*geb*'):
                print('Du schaust dich um und siehst ' + ' die Variable Nichts')

            elif fnmatch.filter(x, '*sprech*'):
                print('Du schaust dich um und siehst ' + ' die Variable Nichts')

            elif fnmatch.filter(x, '*benutz*'):
                print('Du schaust dich um und siehst ' + ' die Variable Nichts')


    # checks if any word with "suche" is in input, then checks if any word in input is in the list of items
    # in the room you're in, finally prints inventory of the item

            elif fnmatch.filter(x, '*suche*'):
                for object in room.items:
                    if fnmatch.filter(x,'*' + object.name + '*'):
                        if object.inventory:
                            print('Du durchsuchst', object.name + '.')
                            print('Hier ist Folgendes drin:\n')
                            for item in object.inventory:
                                print(item.name)
                        else:
                            print('Hier ist nichts drin.')


            elif fnmatch.filter(x, '*geh*'):

                Player.move(self=Player,position=outdoor)

                print('Du gehst in', outdoor.name, 'und dir fallen folgende Sachen auf:')
                for item in outdoor.items:
                    print(item)

            else:
                print('Das kannst du leider nicht machen.')

    # if there is no word recognized from the input
        except:
            print('Das kannst du nicht machen.\n')



