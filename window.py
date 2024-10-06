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
from auto_laile import PressKey,ReleaseKey
from itertools import cycle
import window

webbrowser.open('https://rt.habr.io/game')
time.sleep(10)
# get screensize
x,y = pyautogui.size()
print(f"width={x}\theight={y}")

x2,y2 = pyautogui.size()
x2,y2=int(str(x2)),int(str(y2))
print(x2//2)
print(y2//2)

# find new window title
z1 = pygetwindow.getAllTitles()
time.sleep(1)
print(len(z1))
# # test with pictures folder
# os.startfile("D:\Project_University\Auto_rostelecom/image")
# time.sleep(1)
# z2 = pygetwindow.getAllTitles()
# print(len(z2))
# time.sleep(1)
# z3 = [x for x in z2 if x not in z1]
# z3 = ''.join(z3)
# time.sleep(3)

# also able to edit z3 to specified window-title string like: "Sublime Text (UNREGISTERED)"
# my = pygetwindow.getWindowsWithTitle(z3)[0]
# # quarter of screen screensize
# x3 = x2 // 2
# y3 = y2 // 2
# my.resizeTo(x3,y3)
# # top-left
# my.moveTo(0, 0)
# time.sleep(3)
# my.activate()
# time.sleep(1)
class Screentake():
    def screen(self):
        while True:
# save screenshot
            p = pyautogui.screenshot()
            p.save(r'D:\Project_University\Auto_rostelecom/image/p.png')
            print('Screen!!!!')
# # edit screenshot
# im = PIL.Image.open('D:\Project_University\Auto_rostelecom/image\\p.png')
# im_crop = im.crop((0, 0, x3, y3))
# im_crop.save('D:\Project_University\Auto_rostelecom/image\\p.jpg', quality=100)

# close window
            time.sleep(1)
                                #class example
            button = main.Button()
            button.Cycle()
            screen = Screentake()
            screen.screen()
# my.close()
# Opening image
#     img = cv2.imread("D:\Project_University\Auto_rostelecom\image\p.png")
#-------------------------------------------------------------------------------------

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray = cv2.GaussianBlur(gray, (3, 3), 0)
# cv2.imwrite("gray.jpg", gray)
# #---------------------------------------------------------------------------------
# edged = cv2.Canny(gray, 10, 250)
# cv2.imwrite("edged.jpg", edged)
# #--------------------------------------------------------------------------------
# # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
# # closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
# # cv2.imwrite("closed.jpg", closed)
#
#
# #search counters
# cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# total = 0
#
# img_contou = np.uint8(np.zeros((image.shape[2],image.shape[1])))
#
#
#
# cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# total = 0

# cv2.imshow('origin', image) # выводим итоговое изображение в окно
# cv2.imshow('res', edged) # выводим итоговое изображение в окно

# # цикл по контурам
# for c in cnts:
#     # аппроксимируем (сглаживаем) контур
#     peri = cv2.arcLength(c, True)
#     approx = cv2.approxPolyDP(c, 0.02 * peri, True)
#
#     # если у контура 4 вершины, предполагаем, что это книга
#     if len(approx) == 9:
#         cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
#         total += 1

