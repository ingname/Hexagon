from tkinter import *
import pygame
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
        self.SettingSoundButton.place(x=999, y=999, anchor=CENTER)
        self.SettingLanguageButton.place(x=999, y=999, anchor=CENTER)
        self.ReturnMenu.place(x=999, y=999, anchor=CENTER)


    def NewGame(self):
        self.RemoveAll()
        #Функция начала игры

    def Setting(self):
        self.RemoveAll()
        self.SettingSoundButton.place(x=450, y=250, anchor=CENTER)
        self.SettingLanguageButton.place(x=450, y=295, anchor=CENTER)
        self.ReturnMenu.place(x=80, y=450, anchor=CENTER)

    def Sound(self):
        self.ReturnMenu.place(x=80, y=450, anchor=CENTER)

    def Language(self):
        self.ReturnMenu.place(x=80, y=450, anchor=CENTER)

    def RemoveAll(self):
        self.GameButton.place(x=999, y=999, anchor=CENTER)
        self.SettingButton.place(x=999, y=999, anchor=CENTER)
        self.ExitButton.place(x=999, y=999, anchor=CENTER)

    def Exit(self):
        self.window.quit
        sys.exit(0)




if __name__ == '__main__':
    window.title("Hexagon")
    window.geometry('900x500')
    window.iconbitmap('.\ico\ico.ico')
    GameGUI = GameGUI(window)
    window.mainloop()