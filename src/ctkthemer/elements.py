import time
from functools import partial
from threading import Thread
from src.ctkthemer.liveview import Liveview
from src.menus.number_selector import number_selector
from customtkinter import *
from PIL import Image, ImageTk
import threading
import webbrowser
from src.menus.color_picker import color_picker as cp

Edit_Img = CTkImage(dark_image=Image.open('src/icons/buttons/edit_icon.png'), size=(16,16))
Github_Img = CTkImage(dark_image=Image.open('src/icons/mm_changelog/github.png'), size=(16,16))


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
    def __init__(self, master, arg, lvtype, start, lv=None, other_type=None):
        self.numselector_open = False
        self.master   = master
        self.arg      = arg
        self.lvtype   = lvtype
        self.maxnum   = 0
        self.start_at = 0
        self.lv       = lv
        self.specific = other_type
        self._specs   = {'size_w': 294,
                         'size_y': 65,}
        super(number_entry, self).__init__(master=master, width=self._specs['size_w'], height=self._specs['size_y'], fg_color='gray14', corner_radius=4)

        self.value = StringVar()
        self.value.set(str(start))

        self.label = CTkLabel(self, text=self.arg, font=('Ubuntu', 14), text_color='gray')
        self.label.place(x=6, y=0)

        self.liveview = CTkFrame(self, width=20, height=20, fg_color='white')
        self.liveview.place(x=7, y=34)

        if other_type == None:
            if lvtype == 'border':
                self.liveview.configure(border_color='gray', border_width=int(start), corner_radius=0)
                self.lv.configure(border_width=int(start))
                self.maxnum = 10
            elif lvtype == 'radius':
                self.liveview.configure(corner_radius=int(start))
                self.lv.configure(corner_radius=int(start))
                self.maxnum = 15
            elif lvtype == 'text':
                self.liveview.place_forget()
                self.liveview = CTkLabel(self, text='Aa')
                self.liveview.place(x=220, y=28)
                self.liveview.configure(font=('System', int(start)))
                self.lv.configure(font=('System', (int(start))))
                self.start_at = 1
                self.maxnum = 24
            elif lvtype == 'other':
                self.liveview.place_forget()
                self.maxnum = 10
        else:
            if other_type == "border_width_checked":
                self.liveview.configure(border_color='gray', border_width=int(start), corner_radius=0)
                self.lv.configure(border_width_checked=int(start))
                self.maxnum = 10
            elif other_type == "border_width_unchecked":
                self.liveview.configure(border_color='gray', border_width=int(start), corner_radius=0)
                self.lv.configure(border_width_unchecked=int(start))
                self.maxnum = 10
            elif other_type == "button_length":
                self.liveview.place_forget()
                self.lv.configure(button_length=int(start))
                self.maxnum = 10
            elif other_type == "button_corner_radius":
                self.liveview.configure(corner_radius=int(start))
                self.lv.configure(corner_radius=int(start))
                self.maxnum = 15
            elif other_type == "border_spacing":
                self.liveview.place_forget()
                self.lv.configure(border_spacing=int(start))
                self.maxnum = 15

        self.entry = CTkEntry(self, corner_radius=0, textvariable=self.value, state='disabled')
        self.entry.place(x=32, y=30)

        self.select_number_button = CTkButton(self, text='', image=Edit_Img, width=28, height=28, corner_radius=0, command=partial(self.set_value, lvtype,), fg_color='gray30', hover_color='gray25')
        self.select_number_button.place(x=175, y=30)

    def set_value(self, lv_type):
        if self.numselector_open == False:
            self.numselector_open = True
            print(lv_type)
            if self.specific == None:
                get_num = number_selector(self.entry.get(), max=self.maxnum, start_at=self.start_at, liveview=self.lv, lvtype=lv_type)
            else:
                get_num = number_selector(self.entry.get(), max=self.maxnum, start_at=self.start_at, liveview=self.lv, lvtype=lv_type, othertype=self.specific)
            self.value.set(f"{get_num}")
            self.numselector_open = False

            if self.specific == None:
                if lv_type == 'radius':
                    self.liveview.configure(corner_radius=int(get_num))
                elif lv_type == 'border':
                    self.liveview.configure(border_width=int(get_num))
                elif lv_type == 'text':
                    self.liveview.configure(font=('System', int(get_num)))
                else:
                    pass
            else:
                if self.specific == 'border_width_checked':
                    self.liveview.configure(border_width=int(get_num))
                elif self.specific == 'border_width_unchecked':
                    self.liveview.configure(border_width=int(get_num))
                elif self.specific == 'button_length':
                    pass
                elif self.specific == 'button_corner_radius':
                    self.liveview.configure(corner_radius=int(get_num))
                elif self.specific == 'border_spacing':
                    pass

        elif self.numselector_open == True:
            pass

class color_entry(CTkFrame):

    class entry_class(CTkEntry):
        def __init__(self, master, default, defaulthex, y, type, LV, arg, light, dark, main):
            self.defaultval = default
            self.type   = type
            self.LV     = LV
            self.arg    = arg
            self.main   = main
            self.y_unchanged = int(y)
            self.y = int(y) + 4
            self.colselector_open = False
            self.value = StringVar()
            self.value.set(defaulthex)
            self.liveview = CTkFrame(master, width=20, height=20, fg_color=defaulthex)
            self.liveview.place(x=7, y=self.y)
            super(color_entry.entry_class, self).__init__(master=master, corner_radius=0, textvariable=self.value, state='disabled')

            self.action_button = CTkButton(master, text='', image=Edit_Img, width=28, height=28, corner_radius=0, command=self.set_value, fg_color='gray30', hover_color='gray25')
            self.action_button.place(x=175, y=self.y_unchanged)

            self.light = light
            self.dark = dark

        def set_value(self):
            if self.colselector_open == False:
                self.colselector_open = True
                color = cp(startval=self.defaultval)
                self.value.set(f"{color[1]}")
                self.liveview.configure(fg_color=color[1])
                self.colselector_open = False
                print(f'DEFAULTVAL: {color}')
                self.defaultval = color[0]

                if isinstance(self.LV, list):
                    for LV in self.LV:
                        if self.type == "Light":
                            if self.arg == 'fg_color':
                                self.main.light = color[1]
                                LV.configure(fg_color=(self.main.dark, color[1]))
                            elif self.arg == 'border_color':
                                self.main.light = color[1]
                                LV.configure(border_color=(self.main.dark, color[1]))
                            elif self.arg == 'hover_color':
                                self.main.light = color[1]
                                LV.configure(hover_color=(self.main.dark, color[1]))
                            elif self.arg == 'text_color':
                                self.main.light = color[1]
                                LV.configure(text_color=(self.main.dark, color[1]))
                            elif self.arg == 'placeholder_text_color':
                                self.main.light = color[1]
                                LV.configure(placeholder_text_color=(self.main.dark, color[1]))
                            elif self.arg == 'checkmark_color':
                                self.main.light = color[1]
                                LV.configure(checkmark_color=(self.main.dark, color[1]))
                            elif self.arg == 'progress_color':
                                self.main.light = color[1]
                                LV.configure(progress_color=(self.main.dark, color[1]))
                            elif self.arg == 'button_color':
                                self.main.light = color[1]
                                LV.configure(button_color=(self.main.dark, color[1]))
                            elif self.arg == 'button_hover_color':
                                self.main.light = color[1]
                                LV.configure(button_hover_color=(self.main.dark, color[1]))
                            elif self.arg == 'selected_color':
                                self.main.light = color[1]
                                LV.configure(selected_color=(self.main.dark, color[1]))
                            elif self.arg == 'selected_hover_color':
                                self.main.light = color[1]
                                LV.configure(selected_hover_color=(self.main.dark, color[1]))
                            elif self.arg == 'unselected_color':
                                self.main.light = color[1]
                                LV.configure(unselected_color=(self.main.dark, color[1]))
                            elif self.arg == 'unselected_hover_color':
                                self.main.light = color[1]
                                LV.configure(unselected_hover_color=(self.main.dark, color[1]))
                        elif self.type == "Dark":
                            if self.arg == 'fg_color':
                                self.main.dark = color[1]
                                LV.configure(fg_color=(color[1], self.main.light))
                            elif self.arg == 'border_color':
                                self.main.dark = color[1]
                                LV.configure(border_color=(color[1], self.main.light))
                            elif self.arg == 'hover_color':
                                self.main.dark = color[1]
                                LV.configure(hover_color=(color[1], self.main.light))
                            elif self.arg == 'text_color':
                                self.main.dark = color[1]
                                LV.configure(text_color=(color[1], self.main.light))
                            elif self.arg == 'placeholder_text_color':
                                self.main.dark = color[1]
                                LV.configure(placeholder_text_color=(color[1], self.main.light))
                            elif self.arg == 'checkmark_color':
                                self.main.dark = color[1]
                                LV.configure(checkmark_color=(color[1], self.main.light))
                            elif self.arg == 'progress_color':
                                self.main.dark = color[1]
                                LV.configure(progress_color=(color[1], self.main.light))
                            elif self.arg == 'button_color':
                                self.main.dark = color[1]
                                LV.configure(button_color=(color[1], self.main.light))
                            elif self.arg == 'button_hover_color':
                                self.main.dark = color[1]
                                LV.configure(button_hover_color=(color[1], self.main.light))
                            elif self.arg == 'selected_color':
                                self.main.dark = color[1]
                                LV.configure(selected_color=(color[1], self.main.light))
                            elif self.arg == 'selected_hover_color':
                                self.main.dark = color[1]
                                LV.configure(selected_hover_color=(color[1], self.main.light))
                            elif self.arg == 'unselected_color':
                                self.main.dark = color[1]
                                LV.configure(unselected_color=(color[1], self.main.light))
                            elif self.arg == 'unselected_hover_color':
                                self.main.dark = color[1]
                                LV.configure(unselected_hover_color=(color[1], self.main.light))
                else:
                    if self.type == "Light":
                        if self.arg == 'fg_color':
                            self.main.light = color[1]
                            self.LV.configure(fg_color=(self.main.dark, color[1]))
                        elif self.arg == 'border_color':
                            self.main.light = color[1]
                            self.LV.configure(border_color=(self.main.dark, color[1]))
                        elif self.arg == 'hover_color':
                            self.main.light = color[1]
                            self.LV.configure(hover_color=(self.main.dark, color[1]))
                        elif self.arg == 'text_color':
                            self.main.light = color[1]
                            self.LV.configure(text_color=(self.main.dark, color[1]))
                        elif self.arg == 'placeholder_text_color':
                            self.main.light = color[1]
                            self.LV.configure(placeholder_text_color=(self.main.dark, color[1]))
                        elif self.arg == 'checkmark_color':
                            self.main.light = color[1]
                            self.LV.configure(checkmark_color=(self.main.dark, color[1]))
                        elif self.arg == 'progress_color':
                            self.main.light = color[1]
                            self.LV.configure(progress_color=(self.main.dark, color[1]))
                        elif self.arg == 'button_color':
                            self.main.light = color[1]
                            self.LV.configure(button_color=(self.main.dark, color[1]))
                        elif self.arg == 'button_hover_color':
                            self.main.light = color[1]
                            self.LV.configure(button_hover_color=(self.main.dark, color[1]))
                        elif self.arg == 'selected_color':
                            self.main.light = color[1]
                            self.LV.configure(selected_color=(self.main.dark, color[1]))
                        elif self.arg == 'selected_hover_color':
                            self.main.light = color[1]
                            self.LV.configure(selected_hover_color=(self.main.dark, color[1]))
                        elif self.arg == 'unselected_color':
                            self.main.light = color[1]
                            self.LV.configure(unselected_color=(self.main.dark, color[1]))
                        elif self.arg == 'unselected_hover_color':
                            self.main.light = color[1]
                            self.LV.configure(unselected_hover_color=(self.main.dark, color[1]))
                    elif self.type == "Dark":
                        if self.arg == 'fg_color':
                            self.main.dark = color[1]
                            self.LV.configure(fg_color=(color[1], self.main.light))
                        elif self.arg == 'border_color':
                            self.main.dark = color[1]
                            self.LV.configure(border_color=(color[1], self.main.light))
                        elif self.arg == 'hover_color':
                            self.main.dark = color[1]
                            self.LV.configure(hover_color=(color[1], self.main.light))
                        elif self.arg == 'text_color':
                            self.main.dark = color[1]
                            self.LV.configure(text_color=(color[1], self.main.light))
                        elif self.arg == 'placeholder_text_color':
                            self.main.dark = color[1]
                            self.LV.configure(placeholder_text_color=(color[1], self.main.light))
                        elif self.arg == 'checkmark_color':
                            self.main.dark = color[1]
                            self.LV.configure(checkmark_color=(color[1], self.main.light))
                        elif self.arg == 'progress_color':
                            self.main.dark = color[1]
                            self.LV.configure(progress_color=(color[1], self.main.light))
                        elif self.arg == 'button_color':
                            self.main.dark = color[1]
                            self.LV.configure(button_color=(color[1], self.main.light))
                        elif self.arg == 'button_hover_color':
                            self.main.dark = color[1]
                            self.LV.configure(button_hover_color=(color[1], self.main.light))
                        elif self.arg == 'selected_color':
                            self.main.dark = color[1]
                            self.LV.configure(selected_color=(color[1], self.main.light))
                        elif self.arg == 'selected_hover_color':
                            self.main.dark = color[1]
                            self.LV.configure(selected_hover_color=(color[1], self.main.light))
                        elif self.arg == 'unselected_color':
                            self.main.dark = color[1]
                            self.LV.configure(unselected_color=(color[1], self.main.light))
                        elif self.arg == 'unselected_hover_color':
                            self.main.dark = color[1]
                            self.LV.configure(unselected_hover_color=(color[1], self.main.light))

                print(self.dark, self.light)

            else:
                print('Error: window is already opened.')
                pass

    def __init__(self, master, arg, start_light, start_dark, LV=None):
        self.colselector_open = False
        self.master   = master
        self.arg      = arg
        self.LV       = LV
        self.start_l  = hex2rgb(start_light)
        self.start_d  = hex2rgb(start_dark)
        self._specs   = {'size_w': 294,
                         'size_y': 95,}

        self.light    = start_light
        self.dark     = start_dark

        super(color_entry, self).__init__(master=master, width=self._specs['size_w'], height=self._specs['size_y'], fg_color='gray14', corner_radius=4)

        self.label = CTkLabel(self, text=self.arg, font=('Ubuntu', 14), text_color='gray')
        self.label.place(x=6, y=0)

        self.entry_light = self.entry_class(self, default=self.start_l, y=30, defaulthex=start_light, type='Light', LV=self.LV, arg=self.arg, light=self.light, dark=self.dark, main=self)
        self.entry_light.place(x=32, y=30)

        self.entry_dark = self.entry_class(self, default=self.start_d, y=60, defaulthex=start_dark, type='Dark', LV=self.LV, arg=self.arg, light=self.light, dark=self.dark, main=self)
        self.entry_dark.place(x=32, y=60)

        if isinstance(LV, list):
            for self.lv in LV:
                if self.arg == 'fg_color':
                    self.lv.configure(fg_color=(self.dark, self.light))
                elif self.arg == 'border_color':
                    self.lv.configure(border_color=(self.dark, self.light))
                elif self.arg == 'hover_color':
                    self.lv.configure(hover_color=(self.dark, self.light))
                elif self.arg == 'text_color':
                    self.lv.configure(text_color=(self.dark, self.light))
                elif self.arg == 'placeholder_text_color':
                    self.lv.configure(placeholder_text_color=(self.dark, self.light))
                elif self.arg == 'checkmark_color':
                    self.lv.configure(checkmark_color=(self.dark, self.light))
                elif self.arg == 'progress_color':
                    self.lv.configure(progress_color=(self.dark, self.light))
                elif self.arg == 'button_color':
                    self.lv.configure(button_color=(self.dark, self.light))
                elif self.arg == 'button_hover_color':
                    self.lv.configure(button_hover_color=(self.dark, self.light))
                elif self.arg == 'selected_color':
                    self.lv.configure(selected_color=(self.dark, self.light))
                elif self.arg == 'selected_hover_color':
                    self.lv.configure(selected_hover_color=(self.dark, self.light))
                elif self.arg == 'unselected_color':
                    self.lv.configure(unselected_color=(self.dark, self.light))
                elif self.arg == 'unselected_hover_color':
                    self.lv.configure(unselected_hover_color=(self.dark, self.light))
        else:
            if self.arg == 'fg_color':
                self.LV.configure(fg_color=(self.dark, self.light))
            elif self.arg == 'border_color':
                self.LV.configure(border_color=(self.dark, self.light))
            elif self.arg == 'hover_color':
                self.LV.configure(hover_color=(self.dark, self.light))
            elif self.arg == 'text_color':
                self.LV.configure(text_color=(self.dark, self.light))
            elif self.arg == 'placeholder_text_color':
                self.LV.configure(placeholder_text_color=(self.dark, self.light))
            elif self.arg == 'checkmark_color':
                self.LV.configure(checkmark_color=(self.dark, self.light))
            elif self.arg == 'progress_color':
                self.LV.configure(progress_color=(self.dark, self.light))
            elif self.arg == 'button_color':
                self.LV.configure(button_color=(self.dark, self.light))
            elif self.arg == 'button_hover_color':
                self.LV.configure(button_hover_color=(self.dark, self.light))
            elif self.arg == 'selected_color':
                self.LV.configure(selected_color=(self.dark, self.light))
            elif self.arg == 'selected_hover_color':
                self.LV.configure(selected_hover_color=(self.dark, self.light))
            elif self.arg == 'unselected_color':
                self.LV.configure(unselected_color=(self.dark, self.light))
            elif self.arg == 'unselected_hover_color':
                self.LV.configure(unselected_hover_color=(self.dark, self.light))

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
    def __init__(self, master, arg, LV, cursize):
        self.numselector_open = False
        self.master = master
        self.arg    = arg
        self.maxnum = 0
        self.LV     = LV
        self._specs = {'size_w': 294,
                       'size_y': 65,}
        self.cursize = 15
        super(optionbox, self).__init__(master=master, width=self._specs['size_w'], height=self._specs['size_y'], fg_color='gray14', corner_radius=4)

        self.label = CTkLabel(self, text=self.arg, font=('Ubuntu', 14), text_color='gray')
        self.label.place(x=6, y=0)

        self.optionmenu = CTkOptionMenu(self, fg_color='gray18', corner_radius=0, button_color='gray22', button_hover_color='gray17')
        self.optionmenu.place(x=32, y=30)

        self.refthread = Thread(target=self.refresh)
        self.refthread.start()

    def refresh(self):
        while True:
            time.sleep(2)
            if self.optionmenu.get() == "normal":
                self.LV.configure(font=("Roboto", int(self.cursize), "normal"))
            elif self.optionmenu.get() == "bold":
                self.LV.configure(font=("Roboto", int(self.cursize), "bold"))

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

class changelog_display(CTkFrame):

    class entry(CTkFrame):
        def __init__(self, master, text):
            super(changelog_display.entry, self).__init__(master=master, fg_color='gray11', width=728, height=20)
            cont = CTkLabel(self, text=text, font=('System', 14, 'normal'))
            cont.place(x=7, y=-2)

    class version_entry(CTkFrame):
        def __init__(self, master, text):
            self.text = text
            super(changelog_display.version_entry, self).__init__(master=master, fg_color='gray11', width=728, height=30)
            cont = CTkLabel(self, text=text, font=('System', 20, 'bold'))
            cont.place(x=7, y=-1)

            githubbutton = CTkButton(self, text="", width=24, height=24, image=Github_Img, fg_color='gray11', hover_color='gray14', corner_radius=0, command=self.action)
            githubbutton.place(x=703, y=0)

        def action(self):
            webbrowser.open(f'https://github.com/DDavid701/CTkThemer/tree/{self.text}')

    def __init__(self, master):
        super(changelog_display, self).__init__(master=master, width=728, fg_color='gray11')