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


#Login
def login(secure):
    attempts = 0
    while secure == False and attempts < 3:
        try:
            conn = psycopg2.connect(**DB_SETTINGS)
            cur = conn.cursor()
            time.sleep(1)
            print('\n | Connected to Server | \n')
            time.sleep(1)
            secure = False
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
                cur.execute("SELECT 1 FROM accesscodes WHERE name = %s;", (nameValue,))
                if cur.fetchone():
                    print(f"Sorry, this name already exists.")
                    time.sleep(5)
                    continue
                
                cur.execute("SELECT 1 FROM accesscodes WHERE code = %s;", (codeValue,))
                if cur.fetchone():
                    print(f"Sorry, this Secure Access Code already exists.")
                    time.sleep(5)
                    continue

                else:
                    cur.execute("INSERT INTO accesscodes (name, code) VALUES (%s, %s);", (nameValue, codeValue))
                    conn.commit()
                    print(f"Secure Access Code added for {nameValue}")
                    time.sleep(5)
                    cur.close()
                    conn.close()
                    os.system('clear')
                    print('Please wait while you are securely returned')
                    time.sleep(3)
                    os.system('clear')
                    return nameValue
            
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
                    return securedName
                else:
                    print('Sorry, your Secure Access Code does not match our records')
                    print('Please contact the system administrator')
                    attempts += 1
                    if attempts == 3:
                        time.sleep(2)
                        print('')
                        print('Incorrect Secure Access Code entered too many times. Exiting...')
                        time.sleep(3)
                        return None
                    time.sleep(3)
                    os.system('clear')
        except Exception as e:
            print('Error: ', e)
            time.sleep(10)
            