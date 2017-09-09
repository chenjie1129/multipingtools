# -*- coding: utf-8 -*-

from Tkinter import *
import os
import netifaces
import socket
import netifaces
import threading


#global dict
netint = {}
#Function

threads = []
addresses = []
exitFlag = 0

class myThreadPing(threading.Thread):
    def __init__(self,address):
        threading.Thread.__init__(self)
        self.address = address
    def run(self):
        print "Starting test " + self.address
        ping_test(self.address)
        print "Exiting test"

def ping_test(address):
    response = os.system("ping -c 5 " + address)

    if response == 0:
        print ('This address ' + address + " is reachable")
        # threading.Thread.exit()
    else:
        print ('This address ' + address + " is unreachable")
        # threading.Thread.exit()


for address in addresses:
    thread=myThreadPing(address)
    thread.start()

# 显示 所以地址ping的结果 包括：
#是否可达
#延时多少
#如果是url ip是多少

#advanced 形成图像

thread1=myThreadPing('8.8.8.8')
thread2=myThreadPing('www.thoritech.com.au')

thread1.start()
thread2.start()

print "Exiting Main Thread"

def get_local_network_info():
    cards = netifaces.interfaces()
    for i in range(0, len(cards)):
        cardname = "en" + str(i)
        for card in cards:
            if card == cardname and netifaces.AF_INET in netifaces.ifaddresses(card):
                ipv4_address = str(netifaces.ifaddresses(card)[netifaces.AF_INET][0]['addr'])
                gateway = str(netifaces.gateways()['default'][2][0])
                mac_address = str(netifaces.ifaddresses(card)[netifaces.AF_LINK][0]['addr'])
                if not ipv4_address.startswith("169."):
                    netint['ipv4_address'] = ipv4_address
                    netint['MAC_address'] = mac_address
                    netint['GW'] = gateway


def  ping_test  ():
    get_local_network_info()
    local_ipv4_address=netint['ipv4_address']
    print("You ip address is : " + local_ipv4_address)
    response = os.system("ping -c 5 -i 0.1 " + local_ipv4_address)
    if response==0:
        resultLbl.config(text="You ip address is : " + local_ipv4_address +" Your network card is working good")
    else:
        resultLbl.config(text="Your network card isnot working")



#GUI Area

root = Tk()
frame = Frame(root)
frame.pack()
# hintLbl = Label(frame,text="Input you ip address or url: ")
# hintLbl.grid(row=0,column=0)
# hintLbl.pack()
# address= Entry(frame)
# address.grid(row=0,column=1)
# address.pack()

testBtn = Button(root,text="Start to test",command=ping_test)
testBtn.grid(row=1,column=0)
testBtn.pack()

resultLbl=Label(root)
resultLbl.grid(row=2,column=0)
resultLbl.pack()
