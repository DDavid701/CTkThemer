from functools import partial
from src.menus.number_selector import number_selector
from customtkinter import *
from PIL import Image, ImageTk
import threading
from src.menus.color_picker import color_picker as cp

Edit_Img = CTkImage(dark_image=Image.open('src/icons/buttons/edit_icon.png'), size=(16,16))

class CTkBox(CTkFrame):
    def __init__(self, text, master, args):
        self.text   = text
        self.master = master
        self.args   = args
        self._specs = {'size_w': 150,
                       'size_h': 200,}
        super(CTkBox, self).__init__(master=master, width=self._specs['size_w'], height=self._specs['size_h'], fg_color='gray10', corner_radius=5)

        self.topframe = CTkFrame(self, width=294, height=30, fg_color='gray14', corner_radius=4)
        self.topframe.pack(pady=3)

        self.boxlabel = CTkLabel(master=self.topframe, text=text, font=('Ubuntu', 20))
        self.boxlabel.place(x=5, y=1)

        self.boxlabelargs = CTkLabel(master=self.topframe, text=f"({str(self.args)})", font=('Ubuntu', 14), text_color='gray')
        self.boxlabelargs.place(x=271, y=0)




class number_entry(CTkFrame):
    def __init__(self, master, arg, lvtype, start):
        self.numselector_open = False
        self.master = master
        self.arg    = arg
        self.lvtype = lvtype
        self.maxnum = 0
        self._specs = {'size_w': 294,
                       'size_y': 65,}
        super(number_entry, self).__init__(master=master, width=self._specs['size_w'], height=self._specs['size_y'], fg_color='gray14', corner_radius=4)

        self.value = StringVar()
        self.value.set(str(start))

        self.label = CTkLabel(self, text=self.arg, font=('Ubuntu', 14), text_color='gray')
        self.label.place(x=6, y=0)

        self.liveview = CTkFrame(self, width=20, height=20, fg_color='white')
        self.liveview.place(x=7, y=34)

        if lvtype == 'border':
            self.liveview.configure(border_color='gray', border_width=0, corner_radius=0)
            self.maxnum = 10
        elif lvtype == 'radius':
            self.liveview.configure(corner_radius=int(start))
            self.maxnum = 15

        self.entry = CTkEntry(self, corner_radius=0, textvariable=self.value, state='disabled')
        self.entry.place(x=32, y=30)

        self.select_number_button = CTkButton(self, text='', image=Edit_Img, width=28, height=28, corner_radius=0, command=partial(self.set_value, lvtype,), fg_color='gray30', hover_color='gray25')
        self.select_number_button.place(x=175, y=30)

    def set_value(self, lv_type):
        if self.numselector_open == False:
            self.numselector_open = True
            print(lv_type)
            get_num = number_selector(self.entry.get(), max=self.maxnum)
            self.value.set(f"{get_num}")
            self.numselector_open = False
            if lv_type == 'radius':
                self.liveview.configure(corner_radius=int(get_num))
            elif lv_type == 'border':
                self.liveview.configure(border_width=int(get_num))
            else:
                pass
        elif self.numselector_open == True:
            pass

    def get(self):
        return self.entry.get()

class color_entry(CTkFrame):

    class entry_class(CTkEntry):
        def __init__(self, master, default, y):
            self.y_unchanged = int(y)
            self.y = int(y) + 4
            self.colselector_open = False
            self.value = StringVar()
            self.value.set(default)
            self.liveview = CTkFrame(master, width=20, height=20, fg_color=default)
            self.liveview.place(x=7, y=self.y)
            self.action_button = CTkButton(master, text='', image=Edit_Img, width=28, height=28, corner_radius=0, command=self.set_value, fg_color='gray30', hover_color='gray25')
            self.action_button.place(x=175, y=self.y_unchanged)
            super(color_entry.entry_class, self).__init__(master=master, corner_radius=0, textvariable=self.value, state='disabled')

        def set_value(self):
            if self.colselector_open == False:
                self.colselector_open = True
                color = cp()
                self.value.set(f"{color[1]}")
                self.liveview.configure(fg_color=color[1])
                self.colselector_open = False
            else:
                print('Error: window is already opened.')
                pass

        def get(self):
            return self.get()

    def __init__(self, master, arg, start_light, start_dark):
        self.colselector_open = False
        self.master = master
        self.arg    = arg
        self._specs = {'size_w': 294,
                       'size_y': 95,}
        super(color_entry, self).__init__(master=master, width=self._specs['size_w'], height=self._specs['size_y'], fg_color='gray14', corner_radius=4)

        self.label = CTkLabel(self, text=self.arg, font=('Ubuntu', 14), text_color='gray')
        self.label.place(x=6, y=0)

        self.entry_light = self.entry_class(self, default=str(start_light), y=30)
        self.entry_light.place(x=32, y=30)

        self.entry_dark = self.entry_class(self, default=str(start_dark), y=60)
        self.entry_dark.place(x=32, y=60)