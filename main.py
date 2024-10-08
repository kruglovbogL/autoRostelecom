import webbrowser
from contextlib import redirect_stdout
import pygetwindow
import time
import os
import pyautogui
from PIL import ImageGrab
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
    pass
    p = pyautogui.screenshot()
    # screenshot = ImageGrab.grab()
    p.save(r'D:/Project_University/Auto_rostelecom/image/n.png')
    print('Screen!!!!')

def jump():
    KEYS = 0x39
    PressKey(KEYS)
    time.sleep(1)
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
            # Задаем координаты пикселя, который хотим найти
            x = 845
            y = 763
            # Получаем цвет пикселя на заданных координатах
            screenShot()
            image_path = 'D:/Project_University/Auto_rostelecom/image/n.png'
            image = cv2.imread(image_path)
            if image is None:
                raise ValueError("Не удалось загрузить изображение. Проверьте путь.")

            # Получаем размеры изображения
            height, width, _ = image.shape

            # Определяем размеры фрагмента (например, 100x100 пикселей)
            fragment_size = 125

            # Вычисляем координаты центрального фрагмента
            start_x = (width - fragment_size) // 2 - 72
            start_y = (height - fragment_size) // 2 + 230

            # Вырезаем фрагмент изображения
            fragment = image[start_y:start_y + fragment_size, start_x:start_x + fragment_size]

            # Преобразуем его в массив NumPy
            # fragment_array = np.array(fragment)
            # enemy = np.load('test3.npy')
            # gray = cv2.cvtColor(fragment, cv2.COLOR_BGR2GRAY)
            #
            # blur = cv2.GaussianBlur(gray, (11, 11), 0)
            # canny = cv2.Canny(blur, 30, 150, 3)
            # dilated = cv2.dilate(canny, (1, 1), iterations=0)
            #
            # (cnt, hierarchy) = cv2.findContours(
            #     dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            # rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # countour = cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)
            low_red = (45, 45, 255)
            high_red = (45, 45, 255)
            red_error = cv2.inRange(fragment, low_red, high_red)
            cv2.imwrite("output.jpg", red_error)
            cv2.imshow('countour',red_error)
            a = np.array(red_error)
            # np.save('test1.txt.npy', a)
            load = np.load('test1.txt.npy')
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

            if (load == a).all():
            #     # with open('lg.txt', 'w') as f, redirect_stdout(f):
            #     #     # pixel_color = screenShot().getpixel((x, y))
            #     #     print(f"Цвет пикселя на позиции ({x}, {y}): {pixel_color}")
                jump()
                screenShot()
            # # Отображаем фрагмент
            # else:
            #     #Print(f"Цвет пикселя на позиции ({x}, {y}): {pixel_color}", file=f)
            #     screenShot()
            #     # time.sleep(1)
            # # Выводим массив NumPy
            # # pri nt(fragment_array)












            # dilated = cv2.dilate(canny, (1, 1), iterations=0)
            #
            # (cnt, hierarchy) = cv2.findContours(
            #     dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            # rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)

            # if len(c) > 0:
            #     screenShot()
            #     jump()
            #     screenShot()
            # break

            #

#найти пересечние контура и линии на скриншоте

# # img_contou = np.uint8(np.zeros((image.shape[2],edged.shape[1])))
# # cv2.imshow('countour',img_contou)
# cv2.imwrite("output.jpg", image)
#             x1, y1 = 100, 50  # Начало линии
#             x2, y2 = 300, 350  # Конец линии
#             line = ((x1, y1), (x2, y2))
#
#             # Рисуем линию на изображении
#             cv2.line(image, line[0], line[1], (255, 0, 0), 2)
#             cv2.imwrite('output.png', image)

            # cv2.waitKey()
            # cv2.destroyAllWindows()
if __name__ == '__main__':
    button = Button()
    button.Cycle()
