import webbrowser
import pygetwindow
import time
import os
import pyautogui
import PIL

import imutils
import cv2
from matplotlib import pyplot as plt
import numpy as np
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto.mouse import click, press

import main
import window
from auto_laile import PressKey, ReleaseKey
from itertools import cycle


class Button():
    def Cycle(self):
        image = cv2.imread('D:\Project_University\Auto_rostelecom\image\p.png')
        while True:
            click(button='left', coords=(908, 673)), (
                click(button='left', coords=(927, 721)))  # coordinate cursor button
            click(button='left', coords=(939, 590)), (
                click(button='left', coords=(846, 712)))  # coordinate cursor button
            low_red = (45, 45, 255)
            high_red = (45, 45, 255)
            red_error = cv2.inRange(image, low_red, high_red)
            # cv2.imwrite("output.jpg", only_cat)
            # cv2.imshow('only car', only_cat)
            # cv2.waitKey(0)
            list_button_speed = 0x39
            total = 0
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            blur = cv2.GaussianBlur(gray, (11, 11), 0)
            canny = cv2.Canny(blur, 30, 150, 3)
            dilated = cv2.dilate(canny, (1, 1), iterations=0)

            (cnt, hierarchy) = cv2.findContours(
                dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)

            if len(cnt) > 0:
                time.sleep(1)
                KEYS = list_button_speed
                PressKey(KEYS)
                time.sleep(1)
                ReleaseKey(KEYS)
                print('Doneeeeeeeeeeeeeeeee!!!!')
                # screen = main.Screetake()
                # screen.screen()
            else:
                time.sleep(3)
                print('Error!!!!')
                screen = window.Screetake()
                screen.screen()
# # img_contou = np.uint8(np.zeros((image.shape[2],edged.shape[1])))
# # cv2.imshow('countour',img_contou)
# cv2.imwrite("output.jpg", image)
#                     cv2.imshow('result', image) # выводим итоговое изображение в окно
#                     cv2.waitKey()
#                     cv2.destroyAllWindows()