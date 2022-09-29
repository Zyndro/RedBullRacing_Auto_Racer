import time
import pyautogui
from ctypes import *

# Fill those manually for your screen with data from StartLightPosition.py
start_light_x = 958
start_light_y = 516
get_color_from = (windll.user32.GetDC(0), start_light_x, start_light_y)


def space(seconds):
    pyautogui.keyDown('space')
    time.sleep(seconds)
    pyautogui.keyUp('space')


def space_boost(seconds):
    pyautogui.keyDown('space')
    time.sleep(0.1)
    pyautogui.press('shift')
    time.sleep(seconds)
    pyautogui.keyUp('space')


def wait(seconds):
    time.sleep(seconds)


def detect_start():
    start = True
    while start:
        color = windll.gdi32.GetPixel(*get_color_from)

        if 5500000 < int(color) < 7000000:
            color_changed = True
            while color_changed:
                color = windll.gdi32.GetPixel(*get_color_from)
                print(color)
                if 12000000 < int(color) < 13000000:
                    print("start")
                    start = False
                    break
    race_start()


def race_start():
    space(1.767)  # corner 1
    wait(0.33)
    space(4.824)  # corner 2
    wait(0.39)
    space(4.36)  # corner 3
    wait(0.31)
    space(3.88)  # corner 4 (Bull)
    wait(0.26)
    space(1.56)  # corner 5
    # wait(0.0001)
    space(2.09)  # corner 6
    wait(0.06)
    space(1)  # corner 7
    wait(0.01)
    space_boost(5)  # finish
    quit()
    # Best time: 1'05'741


def main():
    detect_start()


if __name__ == "__main__":
    main()
