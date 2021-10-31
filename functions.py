import fnmatch

## check if schau is in input
def umschauen():
    x = [input('Was machst du?\n')]
    try:
        if fnmatch.filter(x, '*schau*'):
            print('Du schaust dich um und siehst' + ' die Variable Nichts')
        else:
            print('Das kannst du nicht machen.\n')
    except:
        print('testtest')