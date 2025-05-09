import time
import os
import random

score = 0

def rpsMenu(securedName):
    os.system('clear')
    time.sleep(1)
    print('Rock Paper Scissors')
    print('')
    print('(1) - Play')
    print('(2) - Leaderboard')
    print('(3) - Exit')
    sel = input('-> ')
    if sel == '1':
        playGame()
    if sel == '2':
        leaderboard()
    if sel == '3':
        return
    if sel == 'whoami':
        print('You are', securedName)
    
def playGame():
    global score
    gameScore = 0
    compScore = 0
    while gameScore < 2 and compScore < 2:
        os.system('clear')
        choices = ['rock', 'paper', 'scissors']
        computerChoice = random.choice(choices)
        print('Your score is:', gameScore, 'and overall score is:', score)
        print('')
        print('Ready?')
        time.sleep(1.5)
        print('Rock')
        time.sleep(0.5)
        print('Paper')
        time.sleep(0.5)
        print('Scissors')
        time.sleep(0.5)
        gameSel = input('-> ').lower().strip()
        print(computerChoice)
        if gameSel == computerChoice:
            time.sleep(2)
        elif (
            (gameSel == 'rock' and computerChoice == 'scissors') or
            (gameSel == 'paper' and computerChoice == 'rock') or
            (gameSel == 'scissors' and computerChoice == 'paper')
        ):
            print("You win!")
            time.sleep(2)
            gameScore +=1
        else:
            print('You lose!')
            time.sleep(2)
            compScore += 1

    if gameScore == 2 or gameScore == 3:
        score += 1
    os.system('clear')
    print('Play again?')
    print('(1) - Yes')
    print('(2) - No')
    againSel = input('-> ')
    if againSel == '2':
        os.system('clear')
        print('Your score was', score)
        time.sleep(2)
        return
    if againSel == '1':
        playGame()
