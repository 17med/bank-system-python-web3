from colorama import Fore, Back, Style
from  os import system as s
from time import sleep
"""
print(Fore.RED + 'some red text')
print(Back.GREEN+Fore.BLACK + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
"""
def affiche():
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print("------------------------------------------------------------------------------")
    print("-                          "+Fore.CYAN+"Ahmed Crypto bank"+Fore.GREEN+"                                 -")
    print("------------------------------------------------------------------------------")
def loading():
    print(Style.RESET_ALL)
    affiche()
    sleep(0.5)
    for i in range(5):
        s("cls")
        affiche()
        print(Style.RESET_ALL)
        print(Fore.GREEN+"loading .")

        sleep(0.1)
        s("cls")
        affiche()
        print(Style.RESET_ALL)
        print(Fore.GREEN+"loading ..")
        sleep(0.1)
        s("cls")
        affiche()
        print(Style.RESET_ALL)
        print(Fore.GREEN+"loading ...")
        sleep(0.1)

def faild():
    s("cls")
    affiche()
    print(Fore.RED+"\nFAILD")
    input(""+Style.RESET_ALL)
def hiuser(adress,sold):
    s("cls")
    affiche()
    print(Fore.CYAN+"hi user")
    print(Fore.GREEN+f"public key : {adress}")
    print(f"sold :{sold}\n")
    print(Fore.LIGHTBLACK_EX+"1-send money")
    print("2-exit")
def listuser(l):
    s("cls")
    affiche()
    print(Fore.LIGHTBLACK_EX)
    for i in range(len(l)):
        print(f"{i+1}-{l[i]}")
def sendreq(b):
    s("cls")
    affiche()
    if(b):
        print(Fore.GREEN+"req done")
    else:
        print(Fore.RED+"req faild")
def login():
    s("cls")
    affiche()
    print(Fore.LIGHTBLACK_EX+"\nprivate key")

