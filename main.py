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
game_coords = [948, 752,1352, 753]

def open_browser():
    webbrowser.open('https://rt.habr.io/game')
    time.sleep(3)

def clicked():
    click(button='left', coords=(908, 673)), (
        click(button='left', coords=(927, 721)))  # coordinate cursor button
    click(button='left', coords=(939, 590)), (
        click(button='left', coords=(846, 712)))  # coordinate cursor button

def jump():
    # pyautogui.press('space')
    # time.sleep(0.1)  # Небольшая задержка между нажатиями
    keyboard = Controller()
    keyboard.press(Key.space)
    time.sleep(1)
    keyboard.release(Key.space)
    # KEYS = 0x39
    # PressKey(KEYS)
    # time.sleep(0.1)
    # ReleaseKey(KEYS)
    # time.sleep(1)
    # with open('log.txt', 'a') as f, redirect_stdout(f):
    #     print('Done!!!!!!!',file=f)

class Auto_Game():
    def auto_game(self):
        while True:
            clicked()
            screen = np.array(ImageGrab.grab(bbox=game_coords))
            low_red = (255,45,45)
            high_red = (255,45,45)
            red_error = cv2.inRange(screen, low_red,high_red)
            # print(red_error)
            if (red_error[0] == 255).any():
                jump()
            else:
                time.sleep(0.1)

if __name__ == '__main__':
    open_browser()
    button = Auto_Game()
    button.auto_game()
