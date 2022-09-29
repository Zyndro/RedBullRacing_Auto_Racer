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
        print(pos_x[0], pos_y[0])
        listener.stop()


if __name__ == "__main__":
    with Listener(on_click=on_click) as listener:
        listener.join()