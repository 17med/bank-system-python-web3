from web3 import Web3 as web3t
import web3,math
def stringtohex(wb,string):
    return wb.toHex(text=string)
def hextostring(wb,hex):
    return wb.toText(hex)
def cheackaddres(wb,addres):
    return web3.Web3.isAddress(addres)
def connect(adress):
    return web3t(web3.HTTPProvider(adress))
def _isconnected(wb):
    return wb.isConnected()

def login(wb,key):
    try:
        c=wb.eth.account.from_key(key).address
        return {"adress":c,"privatekey":key,"login":True}
    except:
        return {"login":False}
def getsold(wb,c):
    x=wb.eth.getBalance(c["adress"])
    return math.ceil(wb.fromWei(x,"ether"))
def getalladress(wb,c):
    l = wb.eth.accounts
    x=[]
    for i in l:
        if(i!=c["adress"]):
            x.append(i)
    return x
def send(w3,c,amount,publickey2):
    try:
        nonce = w3.eth.getTransactionCount(c["adress"])
        tx = {
            'nonce': nonce,
            'to': publickey2,
            'value': w3.toWei(amount, 'ether'),
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei')
        }
        signed_tx = w3.eth.account.sign_transaction(tx, c["privatekey"])
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return True
    except:
        return False
