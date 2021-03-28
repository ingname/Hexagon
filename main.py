from tkinter import *

def clicked():
    lbl.configure(text="Я же просил")

window = Tk()
window.title("Hexagon")
window.geometry('900x500')
window.iconbitmap('F:\game\Учеба\Практика\Git\Hexagon\ico\ico.ico')

lbl = Label(window, text="Hexagon", font=("Ariak Bold", 50))
# Font шрифт, число размер.
lbl.grid(column=0, row=0)
# Местоположение
btn1 = Button(window, text="Начать играть", fg="black", command=clicked)
btn2 = Button(window, text="Настройки", fg="Black")
btn3 = Button(window, text="Выход", fg="Black", command=window.destroy)
# Кнопка
btn1.grid(column=0, row=1)
btn2.grid(column=0, row=2)
btn3.grid(column=0, row=3)

window.mainloop()

