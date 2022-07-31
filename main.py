import time
import pyautogui
from ctypes import *


# Fill those manually for your screen with data from other script
start_light_x = 838
start_light_y = 503
gray = 12632256
red = 6899952
get_color_from = (windll.user32.GetDC(0), start_light_x, start_light_y)


def space(seconds):
    pyautogui.keyDown('space')
    time.sleep(seconds)
    pyautogui.keyUp('space')


def space_boost(seconds):
    pyautogui.keyDown('space')
    pyautogui.press('shift')
    time.sleep(seconds)
    pyautogui.keyUp('space')


def wait(seconds):
    time.sleep(seconds)


def race_start():
    space(1.767)  # z1
    wait(0.33)
    space(4.824)  # z2
    wait(0.39)
    space(4.36)  # z3
    wait(0.31)
    space(3.88)  # z4 bull
    wait(0.26)
    space(1.56)  # z5
    # wait(0.0001)
    space(2.09)  # z6
    wait(0.06)
    space(1)  # z7
    wait(0.01)
    space_boost(5)
    quit()


def main():
    while True:
        color = windll.gdi32.GetPixel(*get_color_from)
        if color == red:
            y = True
            while y:
                color = windll.gdi32.GetPixel(*get_color_from)
                if color == gray:
                    race_start()


if __name__ == "__main__":
    main()
