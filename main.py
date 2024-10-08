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

import window
from auto_laile import PressKey, ReleaseKey
from itertools import cycle
import pyautogui
import threading

def locate_cat():
    cat=None
    while cat is None:
        cat = pyautogui.locateOnScreen('D:/Project_University/Auto_rostelecom/image/n.png',confidence=.65,region=(1722,748, 200,450))
        return cat

def screenShot():
    p = pyautogui.screenshot()
    p.save(r'D:/Project_University/Auto_rostelecom/image/n.png')
    print('Screen!!!!')

def jump():
    KEYS = 0x39
    PressKey(KEYS)
    time.sleep(2)
    ReleaseKey(KEYS)
    print('Done!!!!!!!')

def clicked():
    click(button='left', coords=(908, 673)), (
        click(button='left', coords=(927, 721)))  # coordinate cursor button
    click(button='left', coords=(939, 590)), (
        click(button='left', coords=(846, 712)))  # coordinate cursor button

class Button():
    def Cycle(self):

        while True:
            clicked()
            image = cv2.imread('D:/Project_University/Auto_rostelecom/image/n.png')
            # low_red = (45, 45, 255)
            # high_red = (45, 45, 255)
            # red_error = cv2.inRange(image, low_red, high_red)
            # cv2.imwrite("output.jpg", red_error)
            # # cv2.imshow('only car', red_error)
            # cv2.waitKey(0)
            # total = 0
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cnts = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if len(cnts) == 2 else cnts[1]

            for c in cnts:
                x, y, w, h = cv2.boundingRect(c)
                ROI = image[y:y + h, x:x + w]
                cv2.imwrite("output.jpg", ROI)


            # blur = cv2.GaussianBlur(gray, (11, 11), 0)
            # canny = cv2.Canny(blur, 30, 150, 3)
            # dilated = cv2.dilate(canny, (1, 1), iterations=0)
            #
            # (cnt, hierarchy) = cv2.findContours(
            #     dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            # rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)

            if len(c) > 0:
                screenShot()
                jump()
                screenShot()
            break

            #

#найти пересечние контура и линии на скриншоте

# # img_contou = np.uint8(np.zeros((image.shape[2],edged.shape[1])))
# # cv2.imshow('countour',img_contou)
# cv2.imwrite("output.jpg", image)
            x1, y1 = 100, 50  # Начало линии
            x2, y2 = 300, 350  # Конец линии
            line = ((x1, y1), (x2, y2))

            # Рисуем линию на изображении
            cv2.line(image, line[0], line[1], (255, 0, 0), 2)
            cv2.imwrite('output.png', image)
            cv2.imshow('result', image) # выводим итоговое изображение в окно
            cv2.waitKey()
            cv2.destroyAllWindows()
if __name__ == '__main__':
    button = Button()
    button.Cycle()
