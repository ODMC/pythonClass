from tkinter import *

window = Tk()
window.title("JUGUETERIA")
window.minsize(width=300, height=300)
table=Canvas(width=200, height=200)

input = Entry(width=10)
input.grid(column=1, row=1)
window.mainloop()