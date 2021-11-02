from objects import *
import fnmatch

print('####################################################################'
      '\nHallo und herzlich Willkommen zu unserem Textabenteuer.\nZiel ist es alle Gegenstände deines'
      ' Computers zu finden und sie in dein Arbeitszimmer zu bringen.'
      '\n\nDu kannst immer folgendes tun: \numschauen, nehmen, geben, ansprechen, benutzen, öffnen, gehen, untersuchen\n'
      '\nDein Inventar kannst du dir anschauen wenn du "Invetar" eingibst.'
      '\nFalls du erneut sehen möchtest, was du tun kannst, tippe "Hilfe" ein, ohne die Anführungszeichen :)\n')

# doesnt allow empty input
while Player.name == '':
    Player.name = input('Bitte geben deinen Namen ein.\n')

print('\nHallo ' + Player.name + '!\nWir wünschen dir viel Erfolg!'
      '\n\nDu kommst von der Arbeit nach Hause und stehst ohne Schlüssel vor der Tür.')

game = True

# game is going on as long game is True
while game:

    # player inputs text, which is checked for specific pieces of words
    x = [input('\nWas machst du nun?\n')]

    # help command if commands forgotten - fnmatch is case-insensitive
    if fnmatch.filter(x, '*Hilfe*'):
        print('\nDu kannst immer folgendes tun: \numschauen, nehmen, geben, ansprechen,'
              ' benutzen, öffnen, gehen, untersuchen\n')

    elif fnmatch.filter(x, '*inventar*'):
        print('\nIn deinem Inventar hast du folgendes:\n')
        for item in Player.inventory:
            print(item.name)

    else:
        try:
            # checks input for *schau* and shows you the room you're in
            # and the items available to interact with
            if fnmatch.filter(x, '*schau*'):
                print('Zur Zeit befindest du dich hier:')
                print(Player.position.name)
                print('Du schaust dich um und siehst:')
                for item in Player.position.items:
                    print(item.name)

            elif fnmatch.filter(x, '*nehm*'):
                already = False
                # checks player inventory if item already in inventory
                for item in Player.inventory:
                    if fnmatch.filter(x, '*' + item.name + '*'):
                        print('Du hast das schon im Inventar.')
                        already = True
                # only checks if not already in inventory
                if not already:
                    # looks in the inventory of all objects in the room and check if it is in the input
                    for object in Player.position.items:
                        # objects are not collectable so if we can break the loop
                        if fnmatch.filter(x, '*' + object.name + '*'):
                            print('Das kannst du nicht ins Inventar legen.')
                            break
                        # goes through the inventory of the items and checks if it is in input text
                        for item in object.inventory:
                            if fnmatch.filter(x, '*' + item.name + '*'):
                                # the object with the item in it has to be searched, so you know that is actually exists
                                if object.searched:
                                    # the object with the item in it has to be collectable
                                    if item.collectable:
                                        print('Du packst', item.name + ' in dein Inventar.')
                                        # adding to player inventory and removing from object inventory
                                        Player.inventory.append(item)
                                        object.inventory.remove(item)
                                    else:
                                        print('Das kannst du nicht ins Inventar legen.')
                                else:
                                    print('Du musst vorher wahrscheinlich noch was dafür machen.')

            elif fnmatch.filter(x, '*geb*'):
                print('Du schaust dich um und siehst ' + ' die Variable Nichts')

            elif fnmatch.filter(x, '*sprech*'):
                print('Du schaust dich um und siehst ' + ' die Variable Nichts')

            elif fnmatch.filter(x, '*benutz*'):
                print('Du schaust dich um und siehst ' + ' die Variable Nichts')


    # checks if any word with "suche" is in input, then checks if any word in input is in the list of items
    # in the room you're in, finally prints inventory of the item

            elif fnmatch.filter(x, '*suche*'):
                already = False
                # checks player inventory if item already in inventory
                for item in Player.inventory:
                    if fnmatch.filter(x, '*' + item.name + '*'):
                        print(item.name,'liegt in deinem Inventar.')
                        print(item.description)
                        already = True
                # only checks if not already in inventory
                if not already:
                    for object in Player.position.items:
                        # checks if input words could be a object
                        if fnmatch.filter(x,'*' + object.name + '*'):
                            print('Du untersuchst:\n',object.name)
                            print(object.description)
                            # if object has inventory prints out text and content
                            if object.inventory:
                                print('Du findest folgendes:')
                                for item in object.inventory:
                                    print(item.name)
                            # if object has no inventory prints out text
                            else:
                                print('Dir fällt sonst nichts besonders auf.')
                # if no word from input was found in items
                    else:
                        print('Das gibts hier nicht.')


            elif fnmatch.filter(x, '*geh*'):
                # checks if input words could be a room
                for room in rooms:
                    if fnmatch.filter(x, '*' + room.name + '*'):
                        if room.name == Player.position.name:
                            print('Du bist bereits hier.')
                        else:
                            print('Du gehst jetzt hierhin:\n', room.name)
                            print(room.description)
                            # changes player position to new room
                            Player.position = room


            # if no command in input gets recognized
            else:
                print('Das kannst du leider nicht machen.')

    # if any python error occurs
        except:
            print('Das kannst du nicht machen.\n')



