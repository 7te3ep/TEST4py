import threading
import time
import os 





def water():
    waternum = 0
    water = ["! ! ! ! ! !","O ! ! ! ! !","O O ! ! ! !","O O O ! ! !","O O O O ! !","O O O O O !", "O O O O O O"]
    print("WATER:" ,water[6])
    while True:
        time.sleep (2)
        waternum +=1
        os.system('clear')
        print("WATER:" ,water[6 - waternum])
        if waternum == 6 :
            print("you died")
            break
        

def user_action():
    waternum = 0
    while True:
        arroser = input("arroser ? y/n ")
        if arroser== "y" :
            waternum += -2

thread1 = threading.Thread(target=water)
thread1.start()

thread2 = threading.Thread(target=user_action)
thread2.start()
