import time
import os
from authuser import login
def menu(secure):
    while True:
        os.system('clear')
        if secure == True:
            print(' | Secured | ')
            print('')
            print('| Main Menu |')
            print('(1) - ')
            print('(2) - ')
            print('(3) - Log Out')
            menuChoice = input('-> ')
            if menuChoice == '1':
                return
            if menuChoice == '2':
                return
            if menuChoice == '3':
                secure = False
                return

secure = False

if __name__ == '__main__':
    while True:
        securedName = login(False)
        if securedName:
            secure = True
            menu(secure)