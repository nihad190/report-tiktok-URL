import requests
from requests.sessions import session
import json
import time
import colorama
from colorama import Fore, Back, Style

colorama.init()

session = requests.session()

print(Fore.CYAN + """  
░█▀▀▄░█▀▀░▄▀▀▄░▄▀▀▄░█▀▀▄░▀█▀░░░▀█▀░░▀░░█░▄░▀█▀░▄▀▀▄░█░▄░░░█▀▀▄░░▀░░█░░░░█▀▀▄░█▀▄
░█▄▄▀░█▀▀░█▄▄█░█░░█░█▄▄▀░░█░░░░░█░░░█▀░█▀▄░░█░░█░░█░█▀▄░░░█░▒█░░█▀░█▀▀█░█▄▄█░█░█
░▀░▀▀░▀▀▀░█░░░░░▀▀░░▀░▀▀░░▀░░░░░▀░░▀▀▀░▀░▀░░▀░░░▀▀░░▀░▀░░░▀░░▀░▀▀▀░▀░░▀░▀░░▀░▀▀░

 """)
print("")
print("")
print("code by nihad")
print("")
print("")

x = input('URL tikto kaka lera dabne: ')
print("")
print("")

print('Reporting the poor sod.....')
print('')
print('')

while True:
    req = session.post(x)
    
    print(req.text)
    print('reported :D')

    time.sleep(10)


input()



