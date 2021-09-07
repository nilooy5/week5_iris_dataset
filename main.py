import io_data_module as io
from tkinter import *

dataSet = io.read_multi_dim_data("iris.data")

tk_window = Tk()

c = Canvas(tk_window, bg="white", height=400, width=400)
radius = 1.5
spread = 50

for x, y, z, w, cls in dataSet:
    c.create_oval(x * spread - radius, y * spread - radius, x * spread + radius, y * spread + radius, outline="red", fill="red")

c.pack()
tk_window.mainloop()