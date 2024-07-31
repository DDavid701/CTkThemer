from customtkinter import *
from PIL import Image
from clipboard import copy

class ErrorPopup(CTkToplevel):
    def __init__(self, error, syn, full_error):
        super(ErrorPopup, self).__init__()

        self.fullerror = full_error

        self.geometry('300x200')
        self.title('CTkThemer - Error')
        self.resizable(FALSE, FALSE)

        self.frame = CTkFrame(master=self, width=300, height=120, fg_color='gray16', corner_radius=0)
        self.frame.place(y=30)

        self.img = CTkLabel(self.frame, text='', image=CTkImage(dark_image=Image.open('src/icons/error_popup/icon.png'), size=(32, 32)))
        self.img.place(x=130, y=8)

        self.error = CTkLabel(self.frame, text=error, text_color='coral')
        self.error.place(x=60, y=47)

        self.synt = CTkLabel(self.frame, text=f'({syn})')
        self.synt.place(x=110, y=67)

        self.button_one = CTkButton(self, text='Copy', font=CTkFont(family='Roboto', weight='normal', size=12), corner_radius=0, fg_color='gray16', hover_color='gray22', command=self.save)
        self.button_one.place(x=9, y=150)

        self.button_two = CTkButton(self, text='OK', font=CTkFont(family='Roboto', weight='normal', size=12), corner_radius=0, fg_color='gray16', hover_color='gray22', command=self.destroy)
        self.button_two.place(x=151, y=150)

    def save(self):
        copy(self.fullerror)