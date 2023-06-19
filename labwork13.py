import os
import time

def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')

def countdown():
    for i in range(20, 0, -1):
        clear_screen()
        print(i)
        time.sleep(1)

countdown()
