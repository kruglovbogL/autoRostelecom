# import main
# import window

import time
from contextlib import redirect_stdout

import win32gui
import win32ui
import win32con
import win32api
import numpy as np
import cv2


import dxcam

import win32gui
import win32ui
import win32con
import time
import win32gui
import win32ui
import win32con
import win32api
import numpy as np
import cv2

from auto_laile import PressKey, ReleaseKey


# class Start():
#     def Next(self):
#         while True:
#             button = main.Button()
#             button.Cycle()
#             screen = window.Screentake()
#             screen.screen()

class Cameras():
    def cam(self):
        camera = dxcam.create()
        # frame = camera.grab()  # full screen
        left,top,right,bottom = 832, 717, 922, 791
        frame = camera.grab(region=(left, top, right, bottom))  # region
        camera.start(target_fps=60)  # threaded
        for i in range(1000):
            image = camera.get_latest_frame()  # Will block until new frame available
        camera.stop()

class Test_Screen():
    def window_capture(self):
        hwnd = 0
        hwndDC = win32gui.GetWindowDC(hwnd)
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        saveBitMap = win32ui.CreateBitmap()

        MoniterDev = win32api.EnumDisplayMonitors(None, None)
        w = MoniterDev[0][2][2]
        h = MoniterDev[0][2][3]

        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        saveDC.SelectObject(saveBitMap)
        saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
        im = saveBitMap.GetBitmapBits(True)  # Tried False also
        img = np.frombuffer(im, dtype=np.uint8).reshape((h, w, 4))
        image = True
        low_red = (45, 45, 255)
        high_red = (45, 45, 255)
        red_error = cv2.inRange(image, low_red, high_red)
        np_array = np.array(red_error)
        booling = np.where(np_array == 255, True, False)
        if (booling == True).any():
            #     # with open('lg.txt', 'w') as f, redirect_stdout(f):
            #     #     # pixel_color = screenShot().getpixel((x, y))
            #     #     print(f"Цвет пикселя на позиции ({x}, {y}): {pixel_color}")
            KEYS = 0x39
            PressKey(KEYS)
            time.sleep(1)
            ReleaseKey(KEYS)
            print('Done!!!!!!!')
        # # Отображаем фрагмент
        else:
            Test_Screen().window_capture()
            print('Screen!!!!')
            with open('lg.txt', 'w') as f, redirect_stdout(f):
                print(None)
                print(f"Цвет пикселя на позиции ({np_array[0:3]}, {np_array[:6]}):", file=f)






        # cv2.imshow("demo", img)
        # cv2.waitKey(100)

    # beg = time.time()
    # for i in range(100):
    #     window_capture()
    # end = time.time()
    # print(end - beg)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    test = Test_Screen()
    test.window_capture()
    # start = Start()
    # start.Next()
    # begin = Test_Screen()
    # begin.window_capture()