import time
import os
from authuser import login
from games import rps
from window import window, mainloop

def menu(secure):
    while True:
        os.system('clear')
        if secure == True:
            os.system('clear')
            print(' | Secured | ')
            print('')
            print('| Main Menu |')
            print('(1) - Rock Paper Scissors')
            print('(2) - Attacks')
            print('(3) - Log Out')
            menuChoice = input('-> ')
            if menuChoice == '1':
                rps.rpsMenu(securedName)
                time.sleep(2)
            if menuChoice == '2':
                os.system('clear')
                print(' | Secured | \n')
                print(' | Attacks |')
                print('(1) - DDOS')
                print('(2) - Brute Force')
                attacksel = input('-> ')
                if attacksel == '1':
                    return
                if attacksel == '2':
                    os.system('clear')
                    window.mainloop()
                    print('Running...')
                    time.sleep(2)
                    print('')
                    print('Attempting 23856 hash keys...')
                    time.sleep(3)
                    print('\nAttack Complete')
                    back = input('')
                    if back == '':
                        menu(secure)
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