from tkinter import *
import tkinter.messagebox
from PIL import ImageTk,Image
import sys

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.grid()

canvas = tkinter.Canvas(window, height=900, width=900)
image = Image.open(".\Pictures\dss.jpg")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.place(x=450, y=250, anchor=CENTER)


class GameGUI(object):

    def __init__(self, window,):
        self.window = window

        self.lbl = Label(window, text="Hexagon", font=("Ariak Bold", 50), fg="White", bg='Black')
        self.lbl.place(x=450, y=150, anchor=CENTER)

        self.txt1 = Label(window, text="ИГРА НАЧАЛАСЬ!", font=("Ariak Bold", 50), fg="White", bg='Black')
        self.txt2 = Label(window, text="Нажмите ENTER для продолжения", font=("Ariak Bold", 20), fg="White", bg='Black')

        self.GameButton = Button(window, text="Начать играть", fg="White", bg='Black', font=("Ariak Bold", 15), width=12, height=1, command=self.NewGame)

        self.SettingButton = Button(window, text="Настройки", fg="White", bg='Black', font=("Ariak Bold", 15), width=10, height=1, command=self.Setting)

        self.SettingSoundButton = Button(window, text='Настройка звука', fg="White", bg='Black', font=("Ariak Bold", 15), width=15, height=1, command=self.Sound)

        self.SettingLanguageButton = Button(window, text='Настройка звука', fg="White", bg='Black', font=("Ariak Bold", 15), width=15, height=1, command=self.Language)

        self.ExitButton = Button(window, text="Выход", fg="White", bg='Black', font=("Ariak Bold", 15), width=8, height=1,command=self.Exit)

        self.ReturnMenu = Button(window, text="Вернуться", fg="White", bg='Black', font=("Ariak Bold", 15), width=8, height=1, command=self.MainMenu)

        self.MainMenu()

    def MainMenu(self):
        self.GameButton.place(x=450, y=250, anchor=CENTER)
        self.SettingButton.place(x=450, y=295, anchor=CENTER)
        self.ExitButton.place(x=450, y=340, anchor=CENTER)
        self.SettingSoundButton.place(x=9999, y=9999, anchor=CENTER)
        self.SettingLanguageButton.place(x=9999, y=9999, anchor=CENTER)
        self.ReturnMenu.place(x=9999, y=9999, anchor=CENTER)


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
        self.ReturnMenu.place(x=80, y=450, anchor=CENTER)

    def Sound(self):
        self.RemoveAll()
        self.ReturnMenu.place(x=80, y=450, anchor=CENTER)

    def Language(self):
        self.RemoveAll()
        self.ReturnMenu.place(x=80, y=450, anchor=CENTER)

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