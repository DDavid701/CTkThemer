from customtkinter import *
from src.ctkthemer.elements import *

class design_CTk(CTkBox):
    def __init__(self, master, text='CTk'):
        self.master = master
        self.text   = text
        super(design_CTk, self).__init__(master=master, text='CTk')

        #entry = Number_Input(master=self)
        #entry.pack()