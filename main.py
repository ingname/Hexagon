from tkinter import *


window = Tk()
window.title("Hexagon")
window.geometry('900x500')

lbl = Label(window, text="menu:", font=("Ariak Bold", 50))
# Font шрифт, число размер.
lbl.grid(column=0, row=0)
# Местоположение
btn = Button(window, text="Не нажимать!", fg="red")
# Кнопка
btn.grid(column=0, row=1)


window.mainloop()
