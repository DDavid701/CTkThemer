from customtkinter import *

class Liveview(CTkFrame):
    def __init__(self, master):
        self.master     = master
        self.appearance = 'Dark'
        super(Liveview, self).__init__(master=self.master, border_width=5, border_color='gray7',  width=660, height=580)

        change_appearance_button = CTkButton(self, text='Change appearance', command=self.change_appearance, corner_radius=0, fg_color='gray8', hover_color='gray9')
        change_appearance_button.place(x=4, y=4)

        # CTkFrame
        self.Frame = CTkFrame(self, width=128, height=128)
        self.Frame.place(x=10, y=40)

        # CTkButton
        self.Button = CTkButton(self)
        self.Button.place(x=10, y=175)

        # CTkLabel
        self.Label = CTkLabel(self)
        self.Label.place(x=10, y=210)

        # CTkEntry
        self.Entry = CTkEntry(self)
        self.Entry.place(x=10, y=240)

        # CTkCheckbox
        self.Checkbox = CTkCheckBox(self)
        self.Checkbox.place(x=10, y=275)

        # CTkSwitch
        self.Switch = CTkSwitch(self)
        self.Switch.place(x=10, y=310)

        # CTkRadiobutton
        self.Radiobutton = CTkRadioButton(self)
        self.Radiobutton.place(x=10, y=340)

        # CTkProgressbar
        self.Progressbar = CTkProgressBar(self)
        self.Progressbar.place(x=10, y=370)

        # CTkSlider
        self.Slider = CTkSlider(self)
        self.Slider.place(x=10, y=390)

        # CTkOptionmenu
        self.Optionmenu = CTkOptionMenu(self)
        self.Optionmenu.place(x=10, y=415)

        # CTkCombobox
        self.Combobox = CTkComboBox(self)
        self.Combobox.place(x=10, y=450)

        # CTkScrollbar
        self.Scrollbar = CTkScrollbar(self)
        self.Scrollbar.place(x=180, y=40)

        # CTkSegmentedbutton
        self.Segmentedbutton = CTkSegmentedButton(self)
        self.Segmentedbutton.place(x=10, y=485)

        # CTkTextbox
        self.Textbox = CTkTextbox(self, width=96, height=96)
        self.Textbox.place(x=180, y=250)

    def change_appearance(self):
        if self.appearance == 'Dark':
            self._set_appearance_mode('Light')
            self.appearance = 'Light'
            self.update()
        elif self.appearance == 'Light':
            self._set_appearance_mode('Dark')
            self.appearance = 'Dark'
            self.update()
        else:
            print(f"Error occured whilst changing appearance mode.")