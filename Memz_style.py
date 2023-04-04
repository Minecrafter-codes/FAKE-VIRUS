import faulthandler; faulthandler.enable()
from win32gui import *
from win32ui import *
from win32api import *
import time, threading
## I cant do the memz tunnel effect. Hope it works on your pc.
hwnd = GetDesktopWindow()
hdc2 = GetWindowDC(0)
x2 = GetSystemMetrics(0)
y2 = GetSystemMetrics(0)

def tunnel_effect():
    for i in range(0, 50):
        StretchBlt(hdc2, 25, 25, x2 - 50, y2 - 50, hdc2, 0, 0, x2, y2, 0x00CC002)
def patinvert():
    while True:
        PatBlt(hdc2, 0, 0, x2, y2, 5898313)
        time.sleep(0.5)
        
def worker():
    import os
    while True: #check for exit
        if os.path.isfile("exit/exit.txt"):
            print('exit now')
            os._exit(0)

threading.Thread(target=worker).start()
tunnel_effect()
patinvert()