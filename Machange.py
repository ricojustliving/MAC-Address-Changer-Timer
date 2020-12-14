import subprocess
import time
import random
import tkinter







# INTERFACE NAME IS SET HERE OR CHANGED HERE

interface = "en0"



print("THIS PROGRAM WAS DESIGNED TO CHANGE YOUR MAC ADDRESS.")
print("EVERY 5 SECONDS FOR 5 TIMES")

print("Designed & Developed by Richard Nieves")

x = 1

for x in range(1,5):
    mod = 0

    #THIS WILL CHANGE THE MAC ADDRESS 5 TIMES BEFORE STOPPING

    #TO CHANGE THIS CHANGE THE NUMBER 5 TO THE AMOUNT OF TIMES YOU WANT YOUR ADDRESS TO CHANGE
    while mod < 5:
        mod += 1



        #first set one numbers
        fo = random.choice('abcdef0123456789')
        fo2 = random.choice('abcdef0123456789')

        #first set two numbers
        ft = random.choice('abcdef0123456789')
        ft2 = random.choice('abcdef0123456789')


        #middle set one numbers
        mo = random.choice('abcdef0123456789')
        mo2 = random.choice('abcdef0123456789')

        #middle set two numbers
        mt = random.choice('abcdef0123456789')
        mt2 = random.choice('abcdef0123456789')


        #last set one numbers
        lo = random.choice('abcdef0123456789')
        lo2 = random.choice('abcdef0123456789')

        #last set two numbers
        lt = random.choice('abcdef0123456789')
        lt2 = random.choice('abcdef0123456789')



        #THIS PART IS THE COMMANDS AND NEW RANDOM ADDRESS IS CREATED

        new_adres = fo + fo2 +":"+ ft + ft2 +":"+ mo + mo2 +":"+ mt + mt2 + ":"+ lo + lo2 + ":" + lt + lt2
        subprocess.call("ifconfig " + interface + " ether " + new_adres, shell=True)
        subprocess.call("ifconfig " + interface + " ether ", shell=True)



        #HERE IS THE TIMER, CURRENTLY SET TO 5 SECONDS, YOU CAN CHANGE THIS TO LENGTHEN OR SHORTEN.
        time.sleep(5)

        x += 1
            
        loop = str(x)
        print("Number of times changed: " + loop)
        print("Your New MAC Address:")
        print(new_adres)
    
