from ahmedbank import banksystem
from ahmedbank import ui
def bankmain():
    nb = 0
    while not nb in range(1, 3):
        ui.hiuser(c["adress"], banksystem.getsold(w, c))
        nb = int(input("->"))

    if (nb == 1):
        nb = 0
        listad = banksystem.getalladress(w, c)
        while not nb in range(1, len(listad) + 1):
            ui.listuser(listad)
            nb = int(input("->"))
        p = 0
        while not p in range(1, banksystem.getsold(w, c) + 1):
            p = int(input("-amount:"))
        ui.affiche()
        b = banksystem.send(w,c, p, listad[nb - 1])
        ui.sendreq(b)
        input("")
        bankmain()
ui.affiche()
w=banksystem.connect("HTTP://127.0.0.1:7545")
ui.loading()
if(banksystem._isconnected(w)):

    ui.login()
    key=input(">")
    c=banksystem.login(w,key)
    if(not c["login"]):
        ui.faild()
    else:
        bankmain()

