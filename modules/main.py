import cv2
import pyautogui
import time
import random

import pytesseract
from PIL import ImageGrab, Image


def get_img():
    left, top, right, bottom = 1201,285, 1339, 315
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    print('Screen!!!!')
    screen_shot = screenshot.save("test.png")
    return screen_shot
    # p.save("/image/n.pn")

    # region = (1208, 278, 1199, 0)
    # p = pyautogui.screenshot(region=region)
    # p.save(r'image/test.png')
    # print('Screen!!!!')


def get_score():
    get_img()
    # Эта функция должна возвращать количество очков с экрана.
    # В данном примере просто возвращаем случайное число
    # В реальной жизни вы должны использовать OCR или другой метод для получения очков
    # image = Image.open('test.jpg')
    img = cv2.imread('test.png')
    # imgs = cv2.resize(img, None, fx=9, fy=9)  # Увеличение изображения в 9 раз
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (11, 11), 0)
    canny = cv2.Canny(blur, 30, 150, 3)
    pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'
    score = pytesseract.image_to_string(canny,config='outputbase digits')
    return print(score)

# def press_space_based_on_score(score):
#     # Пример логики, основанной на количестве очков
#     int_score = int(score)
#     if int_score > 70:
#         # Если количество очков больше 70, нажимаем пробел 3 раза
#         for _ in range(3):
#             pyautogui.press('space')
#             time.sleep(0.1)  # Небольшая задержка между нажатиями
#     elif int_score > 40:
#         # Если количество очков больше 40, нажимаем пробел 2 раза
#         for _ in range(2):
#             pyautogui.press('space')
#             time.sleep(0.1)
#     elif int_score > 0:
#         # Если количество очков больше 0, нажимаем пробел 1 раз
#         pyautogui.press('space')
#
if __name__ == "__main__":
    while True:
        screen = get_img()
        score = get_score()
        print(f"Текущие очки: {score}")
        # press_space_based_on_score(score)
        # time.sleep(1)  # Задержка перед следующим проверкой
