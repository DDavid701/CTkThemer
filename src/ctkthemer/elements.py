from functools import partial
from src.menus.number_selector import number_selector
from customtkinter import *
from PIL import Image, ImageTk
import threading
from src.menus.color_picker import color_picker as cp

Edit_Img = CTkImage(dark_image=Image.open('src/icons/buttons/edit_icon.png'), size=(16,16))


def hex2rgb(hexcode):
    hexcode_rep = hexcode.replace('#', '')
    r = int(hexcode_rep[0:2], 16)
    g = int(hexcode_rep[2:4], 16)
    b = int(hexcode_rep[4:6], 16)
    return (str(r), str(g), str(b))

class CTkBox(CTkFrame):
    def __init__(self, text, master, args):
        self.text   = text
        self.master = master
        self.args   = args
        self._specs = {'size_w': 150,
                       'size_h': 200,}
        super(CTkBox, self).__init__(master=master, width=self._specs['size_w'], height=self._specs['size_h'], fg_color='gray10', corner_radius=0)

        self.topframe = CTkFrame(self, width=294, height=30, fg_color='gray14', corner_radius=4)
        self.topframe.pack(pady=3)

        self.boxlabel = CTkLabel(master=self.topframe, text=text, font=('Ubuntu', 20))
        self.boxlabel.place(x=5, y=1)

        self.boxlabelargs = CTkLabel(master=self.topframe, text=f"({str(self.args)})", font=('Ubuntu', 14), text_color='gray')
        self.boxlabelargs.place(x=271, y=0)


class CTkFontBox(CTkFrame):
    def __init__(self, text, master):
        self.text   = text
        self.master = master
        self._specs = {'size_w': 150,
                       'size_h': 200,}
        super(CTkFontBox, self).__init__(master=master, width=self._specs['size_w'], height=self._specs['size_h'], fg_color='gray10', corner_radius=0)

        self.topframe = CTkFrame(self, width=294, height=30, fg_color='gray14', corner_radius=4)
        self.topframe.pack(pady=3)

        self.boxlabel = CTkLabel(master=self.topframe, text=text, font=('Ubuntu', 17))
        self.boxlabel.place(x=5, y=1)

class number_entry(CTkFrame):
    def __init__(self, master, arg, lvtype, start, lv=None):
        self.numselector_open = False
        self.master   = master
        self.arg      = arg
        self.lvtype   = lvtype
        self.maxnum   = 0
        self.start_at = 0
        self.lv       = lv
        self._specs   = {'size_w': 294,
                         'size_y': 65,}
        super(number_entry, self).__init__(master=master, width=self._specs['size_w'], height=self._specs['size_y'], fg_color='gray14', corner_radius=4)

        self.value = StringVar()
        self.value.set(str(start))

        self.label = CTkLabel(self, text=self.arg, font=('Ubuntu', 14), text_color='gray')
        self.label.place(x=6, y=0)

        self.liveview = CTkFrame(self, width=20, height=20, fg_color='white')
        self.liveview.place(x=7, y=34)

        if lvtype == 'border':
            self.liveview.configure(border_color='gray', border_width=int(start), corner_radius=0)
            self.maxnum = 10
        elif lvtype == 'radius':
            self.liveview.configure(corner_radius=int(start))
            self.maxnum = 15
        elif lvtype == 'text':
            self.liveview.place_forget()
            self.liveview = CTkLabel(self, text='Aa')
            self.liveview.place(x=220, y=28)
            self.liveview.configure(font=('System', int(start)))
            self.start_at = 1
            self.maxnum = 24
        elif lvtype == 'other':
            self.liveview.place_forget()
            self.maxnum = 10

        self.entry = CTkEntry(self, corner_radius=0, textvariable=self.value, state='disabled')
        self.entry.place(x=32, y=30)

        self.select_number_button = CTkButton(self, text='', image=Edit_Img, width=28, height=28, corner_radius=0, command=partial(self.set_value, lvtype,), fg_color='gray30', hover_color='gray25')
        self.select_number_button.place(x=175, y=30)

    def set_value(self, lv_type):
        if self.numselector_open == False:
            self.numselector_open = True
            print(lv_type)
            get_num = number_selector(self.entry.get(), max=self.maxnum, start_at=self.start_at, liveview=self.lv)
            self.value.set(f"{get_num}")
            self.numselector_open = False
            if lv_type == 'radius':
                self.liveview.configure(corner_radius=int(get_num))
            elif lv_type == 'border':
                self.liveview.configure(border_width=int(get_num))
            elif lv_type == 'text':
                self.liveview.configure(font=('System', int(get_num)))
            else:
                pass
        elif self.numselector_open == True:
            pass

class color_entry(CTkFrame):

    class entry_class(CTkEntry):
        def __init__(self, master, default, defaulthex, y):
            self.defaultval = default
            self.y_unchanged = int(y)
            self.y = int(y) + 4
            self.colselector_open = False
            self.value = StringVar()
            self.value.set(defaulthex)
            self.liveview = CTkFrame(master, width=20, height=20, fg_color=defaulthex)
            self.liveview.place(x=7, y=self.y)
            self.action_button = CTkButton(master, text='', image=Edit_Img, width=28, height=28, corner_radius=0, command=self.set_value, fg_color='gray30', hover_color='gray25')
            self.action_button.place(x=175, y=self.y_unchanged)
            super(color_entry.entry_class, self).__init__(master=master, corner_radius=0, textvariable=self.value, state='disabled')

        def set_value(self):
            if self.colselector_open == False:
                self.colselector_open = True
                color = cp(startval=self.defaultval)
                self.value.set(f"{color[1]}")
                self.liveview.configure(fg_color=color[1])
                self.colselector_open = False
                print(f'DEFAULTVAL: {color}')
                self.defaultval = color[0]
            else:
                print('Error: window is already opened.')
                pass

    def __init__(self, master, arg, start_light, start_dark):
        self.colselector_open = False
        self.master = master
        self.arg    = arg
        self.start_l = hex2rgb(start_light)
        self.start_d = hex2rgb(start_dark)
        self._specs = {'size_w': 294,
                       'size_y': 95,}
        super(color_entry, self).__init__(master=master, width=self._specs['size_w'], height=self._specs['size_y'], fg_color='gray14', corner_radius=4)

        self.label = CTkLabel(self, text=self.arg, font=('Ubuntu', 14), text_color='gray')
        self.label.place(x=6, y=0)

        self.entry_light = self.entry_class(self, default=self.start_l, y=30, defaulthex=start_light)
        self.entry_light.place(x=32, y=30)

        self.entry_dark = self.entry_class(self, default=self.start_d, y=60, defaulthex=start_dark)
        self.entry_dark.place(x=32, y=60)

class showbox(CTkFrame):
    def __init__(self, master, arg, text):
        self.numselector_open = False
        self.master = master
        self.arg    = arg
        self.text   = text
        self.maxnum = 0
        self._specs = {'size_w': 294,
                       'size_y': 65,}
        super(showbox, self).__init__(master=master, width=self._specs['size_w'], height=self._specs['size_y'], fg_color='gray14', corner_radius=4)

        var = StringVar(self)
        var.set(self.text)

        self.label = CTkLabel(self, text=self.arg, font=('Ubuntu', 14), text_color='gray')
        self.label.place(x=6, y=0)

        self.show = CTkEntry(self, textvariable=var, fg_color='gray18', border_width=0, state='disabled', corner_radius=0)
        self.show.place(x=32, y=30)

class optionbox(CTkFrame):
    def __init__(self, master, arg):
        self.numselector_open = False
        self.master = master
        self.arg    = arg
        self.maxnum = 0
        self._specs = {'size_w': 294,
                       'size_y': 65,}
        super(optionbox, self).__init__(master=master, width=self._specs['size_w'], height=self._specs['size_y'], fg_color='gray14', corner_radius=4)

        self.label = CTkLabel(self, text=self.arg, font=('Ubuntu', 14), text_color='gray')
        self.label.place(x=6, y=0)

        self.optionmenu = CTkOptionMenu(self, fg_color='gray18', corner_radius=0, button_color='gray22', button_hover_color='gray17')
        self.optionmenu.place(x=32, y=30)

class settings_switch_option_display(CTkFrame):
    def __init__(self, master, text, slot, start):
        self.slot = slot
        super(settings_switch_option_display, self).__init__(master=master, width=800, height=40, corner_radius=0, fg_color='gray9')

        self.text = CTkLabel(self, text=text, font=('Roboto', 16))
        self.text.place(x=7, y=6)

        self.switch = CTkSwitch(self, text='', command=self.change_setting)
        self.switch.place(x=695, y=8)

        print(start)
        type(start)
        if start == 'True':
            self.switch.toggle()
        else:
            pass

        self.bind('<Button-1>', self.switch.toggle)
        self.text.bind('<Button-1>', self.switch.toggle)

        self.pack()

    def change_setting(self):
        with open('settings', 'r') as f:
            settings = f.readlines()

        new_settings = []
        count        = 0
        for setting in settings:
            if count == self.slot:
                if self.switch.get() == 1:
                    _local_var = True
                    new_settings.append(str(_local_var) + "\n")
                else:
                    _local_var = False
                    new_settings.append(str(_local_var) + "\n")
            else:
                new_settings.append(str(setting))
            count += 1

        with open('settings', 'w') as f:
            f.write("")

        with open('settings', 'a') as f:
            for setting in new_settings:
                print(setting)
                f.write(f"{str(setting)}")


class settings_optionmenu_option_display(CTkFrame):
    def __init__(self, master, text, slot, start):
        self.slot = slot
        super(settings_optionmenu_option_display, self).__init__(master=master, width=800, height=40, corner_radius=0, fg_color='gray9')

        self.text = CTkLabel(self, text=text, font=('Roboto', 16))
        self.text.place(x=7, y=6)

        self.optionmenu = CTkOptionMenu(self, command=self.change_setting, corner_radius=0, fg_color='gray18', button_color='gray22', button_hover_color='gray15')
        self.optionmenu.place(x=590, y=8)

        self.optionmenu.set(start)

       # self.bind('<Button-1>', self.optionmenu._dropdown_menu.)
       # self.text.bind('<Button-1>', self.optionmenu._dropdown_menu.open)

        self.pack()

    def change_setting(self, selection):
        with open('settings', 'r') as f:
            settings = f.readlines()

        new_settings = []
        count        = 0
        for setting in settings:
            if count == self.slot:
                new_settings.append(str(selection) + "\n")
            else:
                new_settings.append(str(setting))
            count += 1

        with open('settings', 'w') as f:
            f.write("")

        with open('settings', 'a') as f:
            for setting in new_settings:
                print(setting)
                f.write(f"{str(setting)}")