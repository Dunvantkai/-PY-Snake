import tkinter
import random

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * ROWS
WINDOW_HEIGHT = TILE_SIZE * COLS

#GAME WINDOW
window = tkinter.Tk()
window.title("Snake")
window.resizable(True, False)

canvas = tkinter.Canvas(window, bg = "black", width = WINDOW_HEIGHT, height = WINDOW_HEIGHT, borderwidth = 0, highlightthickness = 0)
canvas.pack()
window.update

#center
window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()

window_width = window_width // 2
window_height = window_height // 2
window_width = window_width -313
window_height = window_height-313

window.geometry(f"+{window_width}+{window_height}")


window.mainloop()

