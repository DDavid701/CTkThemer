from customtkinter import *
from src.ctkthemer.elements import *

class design_CTk(CTkBox):
    def __init__(self, master):
        self.master = master
        self.text   = 'CTk Testing'
        self.args   = 1
        super(design_CTk, self).__init__(master=master, text=self.text, args=self.args)

        self.entry = number_entry(master=self, arg='corner_radius', lvtype='radius', start=0)
        self.entry.pack(pady=3)

        self.entry2 = number_entry(master=self, arg='border_width', lvtype='border', start=0)
        self.entry2.pack(pady=3)

        self.entry3 = color_entry(master=self, arg='color', start_light='#FFFFFF', start_dark='#000000')
        self.entry3.pack(pady=3)