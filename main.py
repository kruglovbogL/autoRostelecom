import webbrowser
from contextlib import redirect_stdout

import numpy as np
import pyautogui
import pywinauto.keyboard
from PIL import ImageGrab
import cv2
from pynput.keyboard import Key, Controller
from pywinauto.mouse import click, press
from pywinauto.keyboard import send_keys
from auto_laile import ReleaseKey,PressKey
import time
game_coord = [948,752,1352,753]      #coordinate in window game

def open_browser():
    webbrowser.open('https://rt.habr.io/game')   #open website
    time.sleep(2)

def clicked():
    click(button='left', coords=(908, 673)), (click(button='left', coords=(927, 721)))  # coordinate cursor button
    click(button='left', coords=(939, 590)), (click(button='left', coords=(846, 712)))  # coordinate cursor button

def jump():
    # pyautogui.press('space')
    # time.sleep(0.1)  # Небольшая задержка между нажатиями
    keyboard = Controller()        #load class Controller
    keyboard.press(Key.space)      #press Key
    time.sleep(1)                  #sleep
    keyboard.release(Key.space)    #release key
    # KEYS = 0x39                          '''alternative
    # PressKey(KEYS)                          keys
    # time.sleep(0.1)                         insert
    # ReleaseKey(KEYS)                        game
    # time.sleep(1)                        '''
    # with open('log.txt', 'a') as f, redirect_stdout(f):   #save output in log files
    #     print('Done!!!!!!!',file=f)

class Auto_Game():
    def auto_clicked(self):
        while True:
            clicked()              #click def mouse
    def auto_game(self):
        while True:
            screen = np.array(ImageGrab.grab(bbox=game_coord))    #np.array screenshot
            low_red = (255, 45, 45)
            high_red = (255, 45, 45)
            red_error = cv2.inRange(screen, low_red, high_red)    #search pixel color
            # cv2.imshow('Read',red_error)            #read and write img in files
            # cv2.imwrite('output.jpg',red_error)     #write img in files
            # cv2.destroyAllWindows()                 #close window
            # print(red_error)                        #check array
            if (red_error[0] == 255).any():
                jump()                                #jump def button
            else:
                time.sleep(0.1)                       #sleeping

if __name__ == '__main__':                            #start
    open_browser()                                    #def browser
    button = Auto_Game()                              #class Auto_Game()
    button.auto_game()                                #Auto_Game.auto_game()
