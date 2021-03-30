from tkinter import *

def play():
    lbl.configure(text="Игра началась", font=("Ariak Bold", 50))
    lbl.place(x = 450, y = 200, anchor=CENTER)
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    exite = Button(window, text="Выход", fg="Black", font=("Ariak Bold", 15), width=8,height=1, command=window.destroy)
    exite.place(x = 60, y = 30, anchor=CENTER)
def setting():
    lbl.configure(text="Настройки", font=("Ariak Bold", 50))
    lbl.place(x = 450, y = 150, anchor=CENTER)
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    exite = Button(window, text="Вернуться", fg="Black", font=("Ariak Bold", 15), width=8,height=1)
    exite.place(x = 60, y = 30, anchor=CENTER)

window = Tk()
window.title("Hexagon")
window.geometry('900x500')
window.iconbitmap('F:\game\Учеба\Практика\Git\Hexagon\ico\ico.ico')

lbl = Label(window, text="Hexagon", font=("Ariak Bold", 50))
# Font шрифт, число размер.
lbl.place(x=450, y=150, anchor=CENTER)
# Местоположение
btn1 = Button(window, text="Начать играть", fg="black", font=("Ariak Bold", 15), width=12, height=1, command=play)
btn2 = Button(window, text="Настройки", fg="Black", font=("Ariak Bold", 15), width=10, height=1, command=setting)
btn3 = Button(window, text="Выход", fg="Black", font=("Ariak Bold", 15), width=8, height=1, command=window.destroy)

# Кнопка
btn1.place(x=450, y=250, anchor=CENTER)
btn2.place(x=450, y=295, anchor=CENTER)
btn3.place(x=450, y=340, anchor=CENTER)

window.mainloop()