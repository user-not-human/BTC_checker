import json, os
import time,generator, requests
from termcolor import colored
from colorama import Fore
check_link = 'https://blockchain.info/balance?active='
founded = 0

while True:
    generator.main()
    file = open('keys.txt','r')
    public=file.readline().replace('\r','')

    #public = '1LruNZjwamWJXThX2Y8C2d47QqhAkkc5os'

    try:
        result = json.loads(requests.get(check_link+public).content.decode('utf-8'))
        recv = result[f'{public}'][f'{"total_received"}']
        coins = result[f'{public}'][f'{"final_balance"}']

        if int(coins)>0:
            output = open('output.txt', 'a')
            wifs = open('wif.txt', 'r')
            output.write(*wifs)
            output.write(f' {public}\r')
            wifs.close()
            output.close()
            print(Fore.RED + f'BINGOOOOOOOOOOOOOOOOO⚠️\nBalance:{coins}\n')
            time.sleep(3)
            founded=+1
        else:
            os.system('cls')
            print(f'{public} | coins: {coins}; total received: {recv}')
            if founded>0:
                print(Fore.RED + f'WARNING! {founded} ADDR HAS BEEN FOUNDED')


        file.close()
        time.sleep(0.1)
    except: #print('wrong public key')
        continue