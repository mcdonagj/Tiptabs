from tkinter import *


class itcGUI:

    top = Tk()

    def __init__(self, title):
        self.top.title(title)
        self.top.resizable(False, False)
        self.top.geometry('400x400')
        self.top.mainloop()




