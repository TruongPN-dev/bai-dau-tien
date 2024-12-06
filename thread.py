from threading import Thread
import time
import os

def symbol():
    key = ["\\", "|", "/","-"]
    while True:
        for i in key:
            # print()
            time.sleep(0.05)
            print("Loading...." + i,end="\r")
def cout():
    j = -1
    while True:
        os.system("cls")
        j += 1
        print(j)
        time.sleep(1)
thread1 = Thread(target=symbol)
thread1.start()
thread2 = Thread(target=cout)
thread2.start()