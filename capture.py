from PIL import ImageGrab
from  mediapipeee import Iris
from draw import draw
import tkinter
import time

root = tkinter.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


canvas = draw(screen_width, screen_height, 100)
canvas.update()
while (True):
    image = ImageGrab.grab()
    coords = Iris.draw(image)

    if len(coords) == 0:
        canvas.master.geometry(f"+{screen_width}+{screen_height}")
        canvas.update()
    else:
        height = int(coords[1] * screen_width - coords[0] * screen_width) // 4
        lendth = int(coords[1]*screen_width - coords[0]*screen_width) + height
        lag = lendth//8
        canvas.config(width=lendth, height=height)
        x = int(coords[0]*screen_width) - lag
        y = int(coords[2]*screen_height) - lag
        canvas.master.geometry(f"+{x}+{y}")
        canvas.update()
        time.sleep(0.01)
