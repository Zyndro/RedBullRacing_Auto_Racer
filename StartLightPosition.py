from pynput.mouse import Listener
from ctypes import *

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


if __name__ == "__main__":
    with Listener(on_click=on_click) as listener:
        listener.join()