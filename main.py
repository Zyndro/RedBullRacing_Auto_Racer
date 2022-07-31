import time
import pyautogui
from pynput.mouse import Listener
from ctypes import *

# Click on the start light in minigame to get its position on screen and color
# Set False to start racing
get_start_light_screen_location = True
# Fill those manually for your screen
start_light_x = 839
start_light_y = 502
gray = 13158600
red = 7491571
get_color_from = (windll.user32.GetDC(0), start_light_x, start_light_y)

pos_x = []
pos_y = []
color = []


# get screen loc for start lights
def on_click(x, y, button, pressed):
    if pressed:
        pos_x.append(x)
        pos_y.append(y)
        color.append(windll.gdi32.GetPixel(windll.user32.GetDC(0), pos_x[0], pos_y[0]))
        if len(color) == 2:
            listener.stop()
            print(pos_x[0], pos_y[0])
            print(color)


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
    if get_start_light_screen_location:
        with Listener(on_click=on_click) as listener:
            listener.join()
        quit()
    main()
