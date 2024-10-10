# import webbrowser
# from contextlib import redirect_stdout
# import pygetwindow
# import time
# import os
# import pyautogui
# from PIL import ImageGrab
# import imutils
# import cv2
# from PIL.Image import Image
# from matplotlib import pyplot as plt
# import numpy as np
# from pywinauto.application import Application
# from pywinauto.keyboard import send_keys
# from pywinauto.mouse import click, press
#
# import window
# from auto_laile import PressKey, ReleaseKey
# from itertools import cycle
# import pyautogui
# import threading
#

#
#
#
#
#
# def clicked():
#     click(button='left', coords=(908, 673)), (
#         click(button='left', coords=(927, 721)))  # coordinate cursor button
#     click(button='left', coords=(939, 590)), (
#         click(button='left', coords=(846, 712)))  # coordinate cursor button
#
# class Button():
#     def Cycle(self):
#
#         while True:
#             clicked()
#             # Задаем координаты пикселя, который хотим найти
#             x = 845
#             y = 763
#             # Получаем цвет пикселя на заданных координатах
#             # p = pyautogui.screenshot()
#             screenshot = ImageGrab.grab(bbox=(870, 741, 872, 742))
#             screenshot.save("test.jpg", quality="web_medium")
#             # p.save("D:/Project_University/Auto_rostelecom/image/n.png")
#             print('Screen!!!!')
#             # screenshot.show()
#
#
#             #
#             # cv2.imwrite('sc.png', screenshot)
#             # image_path = 'sc.png'
#             image = cv2.imread('test.jpg')
#
#             if image is None:
#                 raise ValueError("Не удалось загрузить изображение. Проверьте путь.")
#
#             # Получаем размеры изображения
#             # height, width, _ = image.shape
#             #
#             # # Определяем размеры фрагмента (например, 100x100 пикселей)
#             # fragment_size = 125
#             #
#             # # Вычисляем координаты центрального фрагмента
#             # start_x = (width - fragment_size) // 2 - 72
#             # start_y = (height - fragment_size) // 2 + 230
#
#             # Вырезаем фрагмент изображения
#             # fragment = image[start_y:start_y + fragment_size, start_x:start_x + fragment_size]
#             # cv2.imshow('fragments',fragment)
#             low_red = (45, 45, 255)
#             high_red = (45, 45, 255)
#             red_error = cv2.inRange(image, low_red, high_red)
#             # cv2.imwrite("output.jpg", red_error)
#             # cv2.imshow('countour',red_error)
#             np_array = np.array(red_error)
#             # np.save('test1.txt.npy', a)
#             # load = np.load('test1.txt.npy')
#             # cv2.waitKey(0)
#             # cv2.destroyAllWindows()
#             booling = np.where(np_array==255,True,False)
#
#             if (booling == True).any():
#                 KEYS = 0x39
#                 PressKey(KEYS)
#                 time.sleep(1)
#                 ReleaseKey(KEYS)
#                 print('Done!!!!!!!')
#             #     # with open('lg.txt', 'w') as f, redirect_stdout(f):
#             #     #     # pixel_color = screenShot().getpixel((x, y))
#             #     #     print(f"Цвет пикселя на позиции ({x}, {y}): {pixel_color}")
#
#             # # Отображаем фрагмент
#             else:
#                 screenshot = ImageGrab.grab(bbox=(832, 717, 922, 791))
#                 screenshot.save("test.jpg", quality="web_medium")
#                 print('Screen!!!!')
#                 with open('lg.txt', 'w') as f, redirect_stdout(f):
#                     print(None)
#                     print(f"Цвет пикселя на позиции ({np_array[0:3]}, {np_array[:6]}):",file=f)
#             #     # time.sleep(1)
#             # # Выводим массив NumPy
#             # # pri nt(fragment_array)
#
#
#
#
#
#
#
#
#
#
#
#
#             # dilated = cv2.dilate(canny, (1, 1), iterations=0)
#             #
#             # (cnt, hierarchy) = cv2.findContours(
#             #     dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#             # rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#             # cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)
#
#             # if len(c) > 0:
#             #     screenShot()
#             #     jump()
#             #     screenShot()
#             # break
#
#             #
#
# #найти пересечние контура и линии на скриншоте
#
# # # img_contou = np.uint8(np.zeros((image.shape[2],edged.shape[1])))
# # # cv2.imshow('countour',img_contou)
# # cv2.imwrite("output.jpg", image)
# #             x1, y1 = 100, 50  # Начало линии
# #             x2, y2 = 300, 350  # Конец линии
# #             line = ((x1, y1), (x2, y2))
# #
# #             # Рисуем линию на изображении
# #             cv2.line(image, line[0], line[1], (255, 0, 0), 2)
# #             cv2.imwrite('output.png', image)
#
#             # cv2.waitKey()
#             # cv2.destroyAllWindows()
# if __name__ == '__main__':
#     button = Button()
#     button.Cycle()
from contextlib import redirect_stdout
import webbrowser
from contextlib import redirect_stdout
import pygetwindow
import time
import os
import pyautogui
from PIL import ImageGrab
import imutils
import cv2
from PIL.Image import Image
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
import numpy as np
from PIL import Image, ImageGrab

def clicked():
    click(button='left', coords=(908, 673)), (
        click(button='left', coords=(927, 721)))  # coordinate cursor button
    click(button='left', coords=(939, 590)), (
        click(button='left', coords=(846, 712)))  # coordinate cursor button


def press():
    KEYS = 0x39
    PressKey(KEYS)
    time.sleep(1)
    ReleaseKey(KEYS)

def open_game():
    webbrowser.open('https://rt.habr.io/game')

class Color():
    def colorize(self):
        while True:

            im = Image.open('test.png')
            if im is None:
                raise ValueError("Не удалось загрузить изображение. Проверьте путь.")
            im_matrix = np.array(im)
            with open('log.txt', 'a') as f, redirect_stdout(f):
                print(im_matrix[1][1], file=f)
                red = (115, 255, 0)
                vision = im_matrix[1][1]
                if (vision == red).all():
                    press()
                    print('Done')

                else:
                    print(None)


            # r,g,b = im_rgb.getpixel((871, 741))
            # print(r,g,b)


if __name__ == '__main__':
    col = Color()
    col.colorize()