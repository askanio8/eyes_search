import tkinter


def draw(x, y, lenght):
    #x = x - lenght//8
    #lenght = lenght + lenght//4

    canvas = tkinter.Canvas(width=lenght, height=lenght//3, bg='black')
    canvas.master.overrideredirect(True)
    canvas.master.geometry(f"+{x}+{y-lenght//6}")
    #label.master.lift()
    canvas.master.wm_attributes("-topmost", True)
    canvas.master.wm_attributes("-disabled", True)
    canvas.master.wm_attributes("-transparentcolor", "white")
    canvas.pack()
    return canvas
