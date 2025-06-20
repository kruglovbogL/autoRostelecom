import time
import webbrowser
import pyautogui
import pygetwindow

import main
import numpy as np
webbrowser.open('https://rt.habr.io/game')
time.sleep(1)
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

class Screentake():
    def screen(self):
        while True:
            buttons = main.Button()
            but = buttons.Cycle()
            if len(main.send_keys()) ==  0x39:
                                                # save screenshot
                p = pyautogui.screenshot()
                p.save(r'image/n.png')
                print('Screen!!!!')
                time.sleep(1)
            else:
                print('NONEEEEEEEEEEEEEEEEEE!')
                                #class example
if __name__ == '__main__':
    screen = Screentake()
    screen.screen()



