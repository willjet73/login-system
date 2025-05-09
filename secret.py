import time
import os
import pwinput
import psycopg2 
from dotenv import load_dotenv

load_dotenv()

#Database Settings
DB_SETTINGS = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': int(os.getenv('DB_PORT'))
}

#Add new user
def addCode(name, newCode):
    try:
        conn = psycopg2.connect(**DB_SETTINGS)
        cur = conn.cursor()

        cur.execute("SELECT 1 FROM accesscodes WHERE name = %s;", (name,))
        if cur.fetchone():
            print(f"Sorry, this name already exists.")
            time.sleep(5)
        
        cur.execute("SELECT 1 FROM accesscodes WHERE code = %s;", (newCode,))
        if cur.fetchone():
            print(f"Sorry, this Secure Access Code already exists.")
            time.sleep(5)
        else:
            cur.execute("INSERT INTO accesscodes (name, code) VALUES (%s, %s);", (name, newCode))
            conn.commit()
            print(f"Secure Access Code added for {name}")
            time.sleep(5)
            cur.close()
            conn.close()
    except Exception as e:
        print('Error: ', e)
        time.sleep(10)

time.sleep(1)
conn = psycopg2.connect(**DB_SETTINGS)
print('')
print(' | Connected to Server | ')
print('')
time.sleep(1)
secure = False

#Login
def login(secure):
    while secure == False:
        print('Enter your Secure Access Code')
        sac = pwinput.pwinput(prompt='-> ', mask='*').strip()
        if sac == 'reg':
            os.system('clear')
            print(' | Register | ')
            print('\nPlease Enter Your Name')
            nameValue = input('-> ')
            print('\nHello,',nameValue)
            print('\nPlease enter your chosen Secure Access Code')
            codeValue = pwinput.pwinput(prompt='-> ', mask='*').strip()
            addCode(nameValue, codeValue)
            os.system('clear')
            print('Please wait while you are securely returned')
            time.sleep(3)
            os.system('clear')
        
        elif sac != 'reg':
            conn = psycopg2.connect(**DB_SETTINGS)
            cur = conn.cursor()
            cur.execute("SELECT name FROM accesscodes WHERE code = %s;", (sac,))
            result = cur.fetchone()
            if result:
                securedName = result[0]
                secure = True
                cur.close()
                conn.close()
                time.sleep(1)
                loggedIn(secure, securedName)
            else:
                print('Sorry, your Secure Access Code does not match our records')
                print('Please contact the system administrator')
                time.sleep(3)
                os.system('clear')

def loggedIn(secure, securedName):
    while secure == True:
        os.system('clear')
        print(f"Success! Logged in as: {securedName} ")
        print(secure)
        time.sleep(1)
        secure = menu(secure)
    while secure == False:
        print('Authorisation lost... returning to main menu')
        time.sleep(2)

def menu(secure):
    print(secure)
    os.system('clear')
    if secure == True:
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
            login(secure)

login(secure)
os.system('clear')
