from customtkinter import *
from src.ctkthemer.elements import *

class design_CTk(CTkBox):
    def __init__(self, master, fgcolor):
        self.master = master
        self.text   = 'CTk'
        self.args   = 1
        super(design_CTk, self).__init__(master=master, text=self.text, args=self.args)

        self.fg_color = color_entry(self, start_dark=fgcolor[0], start_light=fgcolor[1], arg='fg_color')
        self.fg_color.pack()

class design_CTkFrame(CTkBox):
    def __init__(self, master, cornerradius, borderwidth, fgcolor, bordercolor, LV):
        self.master = master
        self.text   = 'CTkFrame'
        self.args   = 4
        super(design_CTkFrame, self).__init__(master=master, text=self.text, args=self.args)

        self.corner_radius = number_entry(self, start=cornerradius, arg='corner_radius', lvtype='radius', lv=LV)
        self.corner_radius.pack()

        self.border_width = number_entry(self, start=borderwidth, arg='border_width', lvtype='border')
        self.border_width.pack()

        self.fg_color = color_entry(self, start_dark=fgcolor[0], start_light=fgcolor[1], arg='fg_color')
        self.fg_color.pack()

        self.border_color = color_entry(self, start_dark=bordercolor[0], start_light=bordercolor[1], arg='border_color')
        self.border_color.pack()

class design_CTkButton(CTkBox):
    def __init__(self, master, cornerradius, borderwidth, fgcolor, bordercolor, textcolor, hovercolor):
        self.master = master
        self.text   = 'CTkButton'
        self.args   = 6
        super(design_CTkButton, self).__init__(master=master, text=self.text, args=self.args)

        self.corner_radius = number_entry(self, start=cornerradius, arg='corner_radius', lvtype='radius')
        self.corner_radius.pack()

        self.border_width = number_entry(self, start=borderwidth, arg='border_width', lvtype='border')
        self.border_width.pack()

        self.fg_color = color_entry(self, start_dark=fgcolor[0], start_light=fgcolor[1], arg='fg_color')
        self.fg_color.pack()

        self.hover_color = color_entry(self, start_dark=hovercolor[0], start_light=hovercolor[1], arg='hover_color')
        self.hover_color.pack()

        self.border_color = color_entry(self, start_dark=bordercolor[0], start_light=bordercolor[1], arg='border_color')
        self.border_color.pack()

        self.text_color = color_entry(self, start_dark=textcolor[0], start_light=textcolor[1], arg='text_color')
        self.text_color.pack()

class design_CTkLabel(CTkBox):
    def __init__(self, master, cornerradius, textcolor):
        self.master = master
        self.text   = 'CTkLabel'
        self.args   = 2
        super(design_CTkLabel, self).__init__(master=master, text=self.text, args=self.args)

        self.corner_radius = number_entry(self, start=cornerradius, arg='corner_radius', lvtype='radius')
        self.corner_radius.pack()

        self.text_color = color_entry(self, start_dark=textcolor[0], start_light=textcolor[1], arg='text_color')
        self.text_color.pack()

class design_CTkEntry(CTkBox):
    def __init__(self, master, cornerradius, borderwidth, fgcolor, bordercolor, textcolor, ptextcolor):
        self.master = master
        self.text   = 'CTkEntry'
        self.args   = 6
        super(design_CTkEntry, self).__init__(master=master, text=self.text, args=self.args)

        self.corner_radius = number_entry(self, start=cornerradius, arg='corner_radius', lvtype='radius')
        self.corner_radius.pack()

        self.border_width = number_entry(self, start=borderwidth, arg='border_width', lvtype='border')
        self.border_width.pack()

        self.fg_color = color_entry(self, start_dark=fgcolor[0], start_light=fgcolor[1], arg='fg_color')
        self.fg_color.pack()

        self.border_color = color_entry(self, start_dark=bordercolor[0], start_light=bordercolor[1], arg='border_color')
        self.border_color.pack()

        self.text_color = color_entry(self, start_dark=textcolor[0], start_light=textcolor[1], arg='text_color')
        self.text_color.pack()

        self.placeholdertext_color = color_entry(self, start_dark=ptextcolor[0], start_light=ptextcolor[1], arg='placeholder_text_color')
        self.placeholdertext_color.pack()

class design_CTkCheckBox(CTkBox):
    def __init__(self, master, cornerradius, borderwidth, fgcolor, bordercolor, textcolor, hovercolor, checkcolor):
        self.master = master
        self.text   = 'CTkCheckBox'
        self.args   = 7
        super(design_CTkCheckBox, self).__init__(master=master, text=self.text, args=self.args)

        self.corner_radius = number_entry(self, start=cornerradius, arg='corner_radius', lvtype='radius')
        self.corner_radius.pack()

        self.border_width = number_entry(self, start=borderwidth, arg='border_width', lvtype='border')
        self.border_width.pack()

        self.fg_color = color_entry(self, start_dark=fgcolor[0], start_light=fgcolor[1], arg='fg_color')
        self.fg_color.pack()

        self.border_color = color_entry(self, start_dark=bordercolor[0], start_light=bordercolor[1], arg='border_color')
        self.border_color.pack()

        self.hover_color = color_entry(self, start_dark=hovercolor[0], start_light=hovercolor[1], arg='hover_color')
        self.hover_color.pack()

        self.checkmark_color = color_entry(self, start_dark=checkcolor[0], start_light=checkcolor[1], arg='checkmark_color')
        self.checkmark_color.pack()

        self.text_color = color_entry(self, start_dark=textcolor[0], start_light=textcolor[1], arg='text_color')
        self.text_color.pack()

class design_CTkSwitch(CTkBox):
    def __init__(self, master, cornerradius, borderwidth, fgcolor, buttonlength, textcolor, buttonhovercolor, progresscolor, buttoncolor):
        self.master = master
        self.text   = 'CTkSwitch'
        self.args   = 8
        super(design_CTkSwitch, self).__init__(master=master, text=self.text, args=self.args)

        self.corner_radius = number_entry(self, start=cornerradius, arg='corner_radius', lvtype='radius')
        self.corner_radius.pack()

        self.border_width = number_entry(self, start=borderwidth, arg='border_width', lvtype='border')
        self.border_width.pack()

        self.button_length = number_entry(self, start=buttonlength, arg='button_length', lvtype='other')
        self.button_length.pack()

        self.fg_color = color_entry(self, start_dark=fgcolor[0], start_light=fgcolor[1], arg='fg_color')
        self.fg_color.pack()

        self.progress_color = color_entry(self, start_dark=progresscolor[0], start_light=progresscolor[1], arg='progress_color')
        self.progress_color.pack()

        self.button_color = color_entry(self, start_dark=buttoncolor[0], start_light=buttoncolor[1], arg='button_color')
        self.button_color.pack()

        self.button_hover_color = color_entry(self, start_dark=buttonhovercolor[0], start_light=buttonhovercolor[1], arg='button_hover_color')
        self.button_hover_color.pack()

        self.text_color = color_entry(self, start_dark=textcolor[0], start_light=textcolor[1], arg='text_color')
        self.text_color.pack()

class design_CTkRadioButton(CTkBox):
    def __init__(self, master, cornerradius, borderwidthchecked, borderwidthunchecked, fgcolor, bordercolor, textcolor, hovercolor,):
        self.master = master
        self.text   = 'CTkRadioButton'
        self.args   = 7
        super(design_CTkRadioButton, self).__init__(master=master, text=self.text, args=self.args)

        self.corner_radius = number_entry(self, start=cornerradius, arg='corner_radius', lvtype='radius')
        self.corner_radius.pack()

        self.border_width_checked = number_entry(self, start=borderwidthchecked, arg='border_width_checked', lvtype='border')
        self.border_width_checked.pack()

        self.border_width_unchecked = number_entry(self, start=borderwidthunchecked, arg='border_width_unchecked', lvtype='border')
        self.border_width_unchecked.pack()

        self.fg_color = color_entry(self, start_dark=fgcolor[0], start_light=fgcolor[1], arg='fg_color')
        self.fg_color.pack()

        self.border_color = color_entry(self, start_dark=bordercolor[0], start_light=bordercolor[1], arg='border_color')
        self.border_color.pack()

        self.hover_color = color_entry(self, start_dark=hovercolor[0], start_light=hovercolor[1], arg='hover_color')
        self.hover_color.pack()

        self.text_color = color_entry(self, start_dark=textcolor[0], start_light=textcolor[1], arg='text_color')
        self.text_color.pack()

class design_CTkProgressBar(CTkBox):
    def __init__(self, master, cornerradius, borderwidth, fgcolor, bordercolor, progresscolor):
        self.master = master
        self.text   = 'CTkProgressBar'
        self.args   = 5
        super(design_CTkProgressBar, self).__init__(master=master, text=self.text, args=self.args)

        self.corner_radius = number_entry(self, start=cornerradius, arg='corner_radius', lvtype='radius')
        self.corner_radius.pack()

        self.border_width = number_entry(self, start=borderwidth, arg='border_width', lvtype='border')
        self.border_width.pack()

        self.fg_color = color_entry(self, start_dark=fgcolor[0], start_light=fgcolor[1], arg='fg_color')
        self.fg_color.pack()

        self.progress_color = color_entry(self, start_dark=progresscolor[0], start_light=progresscolor[1], arg='progress_color')
        self.progress_color.pack()

        self.border_color = color_entry(self, start_dark=bordercolor[0], start_light=bordercolor[1], arg='border_color')
        self.border_color.pack()

class design_CTkSlider(CTkBox):
    def __init__(self, master, cornerradius, borderwidth, fgcolor, progresscolor, buttoncornerradius, buttonlength, buttoncolor, buttonhovercolor):
        self.master = master
        self.text   = 'CTkSlider'
        self.args   = 8
        super(design_CTkSlider, self).__init__(master=master, text=self.text, args=self.args)

        self.corner_radius = number_entry(self, start=cornerradius, arg='corner_radius', lvtype='radius')
        self.corner_radius.pack()

        self.button_corner_radius = number_entry(self, start=buttoncornerradius, arg='button_corner_radius', lvtype='radius')
        self.button_corner_radius.pack()

        self.border_width = number_entry(self, start=borderwidth, arg='border_width', lvtype='border')
        self.border_width.pack()

        self.button_length = number_entry(self, start=buttonlength, arg='button_length', lvtype='other')
        self.button_length.pack()

        self.fg_color = color_entry(self, start_dark=fgcolor[0], start_light=fgcolor[1], arg='fg_color')
        self.fg_color.pack()

        self.progress_color = color_entry(self, start_dark=progresscolor[0], start_light=progresscolor[1], arg='progress_color')
        self.progress_color.pack()

        self.button_color = color_entry(self, start_dark=buttoncolor[0], start_light=buttoncolor[1], arg='button_color')
        self.button_color.pack()

        self.button_hover_color = color_entry(self, start_dark=buttonhovercolor[0], start_light=buttonhovercolor[1], arg='button_hover_color')
        self.button_hover_color.pack()

class design_CTkOptionMenu(CTkBox):
    def __init__(self, master, cornerradius, fgcolor, textcolor, buttoncolor, buttonhovercolor):
        self.master = master
        self.text   = 'CTkOptionMenu'
        self.args   = 8
        super(design_CTkOptionMenu, self).__init__(master=master, text=self.text, args=self.args)

        self.corner_radius = number_entry(self, start=cornerradius, arg='corner_radius', lvtype='radius')
        self.corner_radius.pack()

        self.fg_color = color_entry(self, start_dark=fgcolor[0], start_light=fgcolor[1], arg='fg_color')
        self.fg_color.pack()

        self.button_color = color_entry(self, start_dark=buttoncolor[0], start_light=buttoncolor[1], arg='button_color')
        self.button_color.pack()

        self.button_hover_color = color_entry(self, start_dark=buttonhovercolor[0], start_light=buttonhovercolor[1], arg='button_hover_color')
        self.button_hover_color.pack()

        self.text_color = color_entry(self, start_dark=textcolor[0], start_light=textcolor[1], arg='text_color')
        self.text_color.pack()

class design_CTkComboBox(CTkBox):
    def __init__(self, master, cornerradius, fgcolor, textcolor, buttoncolor, buttonhovercolor, bordercolor, borderwidth):
        self.master = master
        self.text   = 'CTkComboBox'
        self.args   = 8
        super(design_CTkComboBox, self).__init__(master=master, text=self.text, args=self.args)

        self.corner_radius = number_entry(self, start=cornerradius, arg='corner_radius', lvtype='radius')
        self.corner_radius.pack()

        self.border_width = number_entry(self, start=borderwidth, arg='border_width', lvtype='border')
        self.border_width.pack()

        self.fg_color = color_entry(self, start_dark=fgcolor[0], start_light=fgcolor[1], arg='fg_color')
        self.fg_color.pack()

        self.border_color = color_entry(self, start_dark=bordercolor[0], start_light=bordercolor[1], arg='border_color')
        self.border_color.pack()

        self.button_color = color_entry(self, start_dark=buttoncolor[0], start_light=buttoncolor[1], arg='button_color')
        self.button_color.pack()

        self.button_hover_color = color_entry(self, start_dark=buttonhovercolor[0], start_light=buttonhovercolor[1], arg='button_hover_color')
        self.button_hover_color.pack()

        self.text_color = color_entry(self, start_dark=textcolor[0], start_light=textcolor[1], arg='text_color')
        self.text_color.pack()

class design_CTkScrollbar(CTkBox):
    def __init__(self, master, cornerradius, borderspacing, buttoncolor, buttonhovercolor):
        self.master = master
        self.text   = 'CTkScrollbar'
        self.args   = 5
        super(design_CTkScrollbar, self).__init__(master=master, text=self.text, args=self.args)

        self.corner_radius = number_entry(self, start=cornerradius, arg='corner_radius', lvtype='radius')
        self.corner_radius.pack()

        self.border_spacing = number_entry(self, start=borderspacing, arg='border_spacing', lvtype='other')
        self.border_spacing.pack()

        self.button_color = color_entry(self, start_dark=buttoncolor[0], start_light=buttoncolor[1], arg='button_color')
        self.button_color.pack()

        self.button_hover_color = color_entry(self, start_dark=buttonhovercolor[0], start_light=buttonhovercolor[1], arg='button_hover_color')
        self.button_hover_color.pack()

class design_CTkSegmentedButton(CTkBox):
    def __init__(self, master, cornerradius, fgcolor, textcolor, selectedcolor, selectedhovercolor, unselectedcolor, unselectedhovercolor, borderwidth):
        self.master = master
        self.text   = 'CTkSegmentedButton'
        self.args   = 8
        super(design_CTkSegmentedButton, self).__init__(master=master, text=self.text, args=self.args)

        self.corner_radius = number_entry(self, start=cornerradius, arg='corner_radius', lvtype='radius')
        self.corner_radius.pack()

        self.border_width = number_entry(self, start=borderwidth, arg='border_width', lvtype='border')
        self.border_width.pack()

        self.fg_color = color_entry(self, start_dark=fgcolor[0], start_light=fgcolor[1], arg='fg_color')
        self.fg_color.pack()

        self.selected_color = color_entry(self, start_dark=selectedcolor[0], start_light=selectedcolor[1], arg='selected_color')
        self.selected_color.pack()

        self.selected_hover_color = color_entry(self, start_dark=selectedhovercolor[0], start_light=selectedhovercolor[1], arg='selected_hover_color')
        self.selected_hover_color.pack()

        self.unselected_color = color_entry(self, start_dark=unselectedcolor[0], start_light=unselectedcolor[1], arg='unselected_color')
        self.unselected_color.pack()

        self.unselected_hover_color = color_entry(self, start_dark=unselectedhovercolor[0], start_light=unselectedhovercolor[1], arg='unselected_hover_color')
        self.unselected_hover_color.pack()

        self.text_color = color_entry(self, start_dark=textcolor[0], start_light=textcolor[1], arg='text_color')
        self.text_color.pack()

class design_DropdownMenu(CTkBox):
    def __init__(self, master, fgcolor, textcolor, hovercolor):
        self.master = master
        self.text   = 'DropdownMenu'
        self.args   = 3
        super(design_DropdownMenu, self).__init__(master=master, text=self.text, args=self.args)

        self.fg_color = color_entry(self, start_dark=fgcolor[0], start_light=fgcolor[1], arg='fg_color')
        self.fg_color.pack()

        self.hover_color = color_entry(self, start_dark=hovercolor[0], start_light=hovercolor[1], arg='hover_color')
        self.hover_color.pack()

        self.text_color = color_entry(self, start_dark=textcolor[0], start_light=textcolor[1], arg='text_color')
        self.text_color.pack()


class design_CTkFont(CTkBox):
    def __init__(self, master, size_mac, weight_mac, size_win, weight_win, size_lin, weight_lin):
        self.master = master
        self.text   = 'Fonts'
        self.args   = 3
        super(design_CTkFont, self).__init__(master=master, text=self.text, args=self.args)

        self.macosfontbox = CTkFontBox(master=self, text='MacOS')
        self.macosfontbox.pack()

        # MacOS
        self.macos_family = showbox(self, text='SF Display', arg='family')
        self.macos_family.pack()

        self.macos_size = number_entry(self, start=size_mac, arg='size', lvtype='text')
        self.macos_size._specs = {'size_w': 274, 'size_y': 65,}
        self.macos_size.pack()

        self.macos_weight = optionbox(self, arg='weight')
        self.macos_weight.optionmenu.configure(values=['normal', 'bold'])
        self.macos_weight.optionmenu.set(weight_mac)
        self.macos_weight.pack()

        self.winfontbox = CTkFontBox(master=self, text='Windows')
        self.winfontbox.pack()

        # Windows
        self.win_family = showbox(self, text='Roboto', arg='family')
        self.win_family.pack()

        self.win_size = number_entry(self, start=size_win, arg='size', lvtype='text')
        self.win_size._specs = {'size_w': 274, 'size_y': 65, }
        self.win_size.pack()

        self.win_weight = optionbox(self, arg='weight')
        self.win_weight.optionmenu.configure(values=['normal', 'bold'])
        self.win_weight.optionmenu.set(weight_win)
        self.win_weight.pack()

        self.linfontbox = CTkFontBox(master=self, text='Linux')
        self.linfontbox.pack()

        # Linux
        self.lin_family = showbox(self, text='Roboto', arg='family')
        self.lin_family.pack()

        self.lin_size = number_entry(self, start=size_lin, arg='size', lvtype='text')
        self.lin_size._specs = {'size_w': 274, 'size_y': 65, }
        self.lin_size.pack()

        self.lin_weight = optionbox(self, arg='weight')
        self.lin_weight.optionmenu.configure(values=['normal', 'bold'])
        self.lin_weight.optionmenu.set(weight_lin)
        self.lin_weight.pack()