import time
import os
from authuser import login
from games import rps

def menu(secure):
    while True:
        os.system('clear')
        if secure == True:
            os.system('clear')
            print(' | Secured | ')
            print('')
            print('| Main Menu |')
            print('(1) - Rock Paper Scissors')
            print('(2) - ')
            print('(3) - Log Out')
            menuChoice = input('-> ')
            if menuChoice == '1':
                rps.rpsMenu(securedName)
                time.sleep(2)
            if menuChoice == '2':
                return
            if menuChoice == '3':
                secure = False
                return
            if menuChoice == 'whoami':
                print('You are', securedName)
                time.sleep(2)

secure = False

if __name__ == '__main__':
    while True:
        securedName = login(False)
        if securedName:
            secure = True
            menu(secure)
        else:
            break