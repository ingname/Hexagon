from tkinter import *
import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk,Image
import sys
from threading import Thread
from playsound import playsound

def music():playsound('Sound/Big_Slinker.mp3') #функция которая будет играть музыка
Thread(target = music, daemon=True).start() #Запускается функция в отдельном потоке


window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.grid()

canvas = tkinter.Canvas(window, height=900, width=900)
image = Image.open(".\Pictures\dss.jpg")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.place(x=450, y=250, anchor=CENTER)

class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
            self['background'] = self['activebackground']

    def on_leave(self, e):
            self['background'] = self.defaultBackground


class GameGUI(object):


    def __init__(self, window):
        self.window = window

        self.lbl = Label(window, text="Hexagon", font=("Ariak Bold", 50), fg="White", bg='Black')
        self.lbl.place(x=450, y=150, anchor=CENTER)

        self.txt1 = Label(window, text="ИГРА НАЧАЛАСЬ!", font=("Ariak Bold", 50), fg="White", bg='Black')
        self.txt2 = Label(window, text="Нажмите ENTER для продолжения", font=("Ariak Bold", 20), fg="White", bg='Black')

        self.GameButton = HoverButton(window, text="Начать играть", fg="White", bg='Black', font=("Ariak Bold", 15), width=12, height=1, activebackground='gray', command=self.NewGame)

        self.SettingButton = HoverButton(window, text="Настройки", fg="White", bg='Black', font=("Ariak Bold", 15), width=10, height=1,activebackground='gray', command=self.Setting)

        self.SettingSoundButton = HoverButton(window, text='Настройка звука', fg="White", bg='Black', font=("Ariak Bold", 15), width=15, height=1,activebackground='gray', command=self.Sound)

        self.SettingLanguageButton = HoverButton(window, text='Настройка языка', fg="White", bg='Black', font=("Ariak Bold", 15), width=15, height=1,activebackground='gray', command=self.Language)

        self.ExitButton = HoverButton(window, text="Выход", fg="White", bg='Black', font=("Ariak Bold", 15), width=8, height=1, activebackground='gray', command=self.Exit)

        self.ReturnMenu1 = HoverButton(window, text="Вернуться", fg="White", bg='Black', font=("Ariak Bold", 15), width=8, height=1, activebackground='gray', command=self.MainMenu)

        self.ReturnMenu2 = HoverButton(window, text="Вернуться", fg="White", bg='Black', font=("Ariak Bold", 15), width=8, height=1, activebackground='gray', command=self.Setting)

        self.MainMenu()





    def MainMenu(self):
        self.GameButton.place(x=450, y=250, anchor=CENTER)
        self.SettingButton.place(x=450, y=295, anchor=CENTER)
        self.ExitButton.place(x=450, y=340, anchor=CENTER)
        self.SettingSoundButton.place(x=9999, y=9999, anchor=CENTER)
        self.SettingLanguageButton.place(x=9999, y=9999, anchor=CENTER)
        self.ReturnMenu1.place(x=9999, y=9999, anchor=CENTER)
        self.ReturnMenu2.place(x=9999, y=9999, anchor=CENTER)


    def NewGame(self):
        self.RemoveAll()
        self.lbl.place(x=9999, y=9999, anchor=CENTER)
        self.txt1.place(x=450, y=250, anchor=CENTER)
        self.txt2.place(x=450, y=300, anchor=CENTER)
        #Функция начала игры

    def Setting(self):
        self.RemoveAll()
        self.SettingSoundButton.place(x=450, y=250, anchor=CENTER)
        self.SettingLanguageButton.place(x=450, y=295, anchor=CENTER)
        self.ReturnMenu1.place(x=80, y=450, anchor=CENTER)
        self.ReturnMenu2.place(x=9999, y=9999, anchor=CENTER)

    def Sound(self):
        self.RemoveAll()
        self.ReturnMenu2.place(x=80, y=450, anchor=CENTER)

    def Language(self):
        self.RemoveAll()
        self.ReturnMenu2.place(x=80, y=450, anchor=CENTER)

    def RemoveAll(self):
        self.GameButton.place(x=9999, y=9999, anchor=CENTER)
        self.SettingButton.place(x=9999, y=9999, anchor=CENTER)
        self.ExitButton.place(x=9999, y=9999, anchor=CENTER)
        self.SettingSoundButton.place(x=9999, y=9999, anchor=CENTER)
        self.SettingLanguageButton.place(x=9999, y=9999, anchor=CENTER)

    def Exit(self):
        self.window.quit
        sys.exit(0)


if __name__ == '__main__':
    window.title("Hexagon")
    window.geometry('900x500')
    window.iconbitmap('.\ico\ico.ico')
    GameGUI = GameGUI(window)
    window.mainloop()