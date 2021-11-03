from objects import *
import fnmatch

# debug stuff
import traceback
import sys

print('####################################################################'
      '\nHallo und herzlich Willkommen zu unserem Textabenteuer.\nZiel ist es alle Gegenstände deines'
      ' Computers zu finden und sie in dein Arbeitszimmer zu bringen.'
      '\n\nDu kannst immer folgendes tun: \numschauen, nehmen, geben, ansprechen, benutzen, öffnen, gehen, untersuchen\n'
      '\nDein Inventar kannst du dir anschauen wenn du "Inventar" eingibst.'
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
              ' benutzen, gehen, untersuchen\n')

    elif fnmatch.filter(x, '*inventar*'):
        print('\nIn deinem Inventar hast du folgendes:\n')
        inventar_list = []
        if Player.inventory:
            for item in Player.inventory:
                inventar_list.append(item.name)
            joined_inventar = ", ".join(inventar_list)
            print(joined_inventar)
        else:
            print('Nichts.')

    else:
        try:
            # checks input for *schau* and shows you the room you're in
            # and the items available to interact with
            if fnmatch.filter(x, '*schau*'):
                print('Zur Zeit befindest du dich hier:')
                print(Player.position.name)
                print('Du schaust dich um und siehst:')
                # creates comma seperated string and prints it out
                item_list = []
                for item in Player.position.items:
                    item_list.append(item.name)
                joined_itemlist = ", ".join(item_list)
                print(joined_itemlist)
                # if any person exists in room prints out
                if Player.position.person:
                    person_list = []
                    print('Außerdem befinden sich folgende Personen im Raum:')
                    for person in Player.position.person:
                        person_list.append(person.name)
                    joined_person_list = ", ".join(person_list)
                    print(joined_person_list)

            elif fnmatch.filter(x, '*nehm*'):
                check = False
                # checks player inventory if item already in inventory
                for item in Player.inventory:
                    if fnmatch.filter(x, '*' + item.name + '*'):
                        print('Du hast das schon im Inventar.')
                        check = True
                # only checks if not already in inventory
                if not check:
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
                # check if any person in room
                if Player.position.person:
                    # check if the wanted person in in room
                    check = False
                    for person in Player.position.person:
                        if not fnmatch.filter(x, '*' + person.name + '*'):
                            print('Die Person der du etwas geben möchtest, gibt es hier nicht.')
                            check = True
                        # if person does not need anything
                        elif not person.mission:
                            print(person.name, 'möchte nichts von dir bekommen.')
                            check = True
                    if not check:
                        check2 = False
                        # checks if item is in players inventory
                        for item in Player.inventory:
                            if fnmatch.filter(x, '*' + item.name + '*'):
                                check2 = True
                        if not check2:
                            print('Soetwas hast du nicht.')
                        # only checks if not already in inventory
                        elif check2:
                            # looks in mission list of person to see if needed
                            for mission in person.mission:
                                # breaks loop if mission accomplished
                                if fnmatch.filter(x, '*' + mission.name + '*'):
                                    print('Du gibst', person.name, 'folgendes:')
                                    print(mission.name)
                                    person.inventory.append(mission)
                                    Player.inventory.remove(mission)
                                    break
                                else:
                                    print(person.name, 'möchte das nicht von dir bekommen.')
                else:
                    print('Hier ist niemand außer dir.')


            elif fnmatch.filter(x, '*sprech*'):
                # check if any person in room
                if Player.position.person:
                    # check if the wanted person in in room
                    check = False
                    for person in Player.position.person:
                        if not fnmatch.filter(x, '*' + person.name + '*'):
                            print('Die Person mit der du sprechen möchtest, gibt es hier nicht.')
                            check = True
                        # if person has nothing to say
                        elif not person.talk:
                            print('Die Person möchte nicht mit der sprechen.')
                            check = True
                    if not check:
                        print(person.talk)



                else:
                    print('Hier ist niemand außer dir.')

            elif fnmatch.filter(x, '*benutz*'):
                for object in Player.position.items:
                        if fnmatch.filter(x, '*' + object.name + '*'):
                            if not object.inventory:
                                if not object.active:
                                    Coffeemachine.makes_coffe(object,coffee)
                                else:
                                    print('Du schaltest',object.name,'aus.')
                                    object.active = False
                            else:
                                print('Das geht gerade nicht.')


    # checks if any word with "suche" is in input, then checks if any word in input is in the list of items
    # in the room you're in, finally prints inventory of the item

            elif fnmatch.filter(x, '*suche*'):

                # will be set to true if input is in the room list
                check = False
                check2 = False
                # checks player inventory if item already in inventory
                for item in Player.inventory:
                    if fnmatch.filter(x, '*' + item.name + '*'):
                        print(item.name,'liegt in deinem Inventar.')
                        print('Info -', item.description)
                        check = True
                # only checks if not already in player inventory
                if not check:
                    # check if object is in the room
                    if not check2:
                        for object in Player.position.items:
                            # checks if input words could be a object
                            if fnmatch.filter(x,'*' + object.name + '*'):
                                print('Du untersuchst:\n',object.name)
                                print(object.description)
                                check2 = True
                                # sets searched status to true so it can be picked up
                                object.searched = True
                                # if object has inventory prints out text and content
                                if object.inventory:
                                    print('Du findest folgendes:')
                                    for item in object.inventory:
                                        print(item.name)
                                # if object has no inventory prints out text
                                else:
                                    print('Dir fällt sonst nichts besonders auf.')
                    # if no word from input was found in items
                    if not check2:
                        print('Das kannst du nicht untersuchen.')

            elif fnmatch.filter(x, '*geh*'):

                # will be set to true if input is in the room list
                check = False
                # checks if input words could be a room
                for room in rooms:
                    if fnmatch.filter(x, '*' + room.name + '*'):
                        check = True
                        if room.name == Player.position.name:
                            print('Du bist bereits hier.')
                        else:
                            print('Du gehst jetzt hierhin:\n', room.name)
                            print(room.description)
                            # changes player position to new room
                            Player.position = room
                if not check:
                    print('Dahin kannst du nicht gehen.')

            # if no command in input gets recognized
            else:
                print('Das kannst du leider nicht machen.')

    # if any python error occurs
        except Exception:
            print(traceback.format_exc())
            print(sys.exc_info()[2])


