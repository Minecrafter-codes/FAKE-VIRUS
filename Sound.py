from pygame import mixer
import pygame
import os, sys, time
from threading import Thread
import faulthandler; faulthandler.enable()
mixer.init()
def music():
    while True:
        crash_sound = mixer.Sound("Sound.mp3")
        mixer.Sound.play(crash_sound)
        if os.path.isfile("exit/exit.txt"):
            print('Exit Now. Activated on Thread')
            exit()

t1 = Thread(target=music)
t1.start()
time.sleep(0.5)
t2 = Thread(target=music)
t2.start()
time.sleep(0.5)
t3 = Thread(target=music)
t3.start()
time.sleep(0.5)
t4 = Thread(target=music)
t4.start()
time.sleep(0.5)
t5 = Thread(target=music)
t5.start()
time.sleep(0.5)
    

while True:
    if os.path.isfile("exit/exit.txt"):
        print('Exit Now')
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        mixer.quit()
        pygame.quit()
        exit()