from customtkinter import *

class Liveview(CTkFrame):
    def __init__(self, master):
        self.master     = master
        self.appearance = 'Dark'
        super(Liveview, self).__init__(master=self.master, border_width=5, border_color='gray7',  width=660, height=580)

        change_appearance_button = CTkButton(self, text='Change appearance', command=self.change_appearance, corner_radius=0, fg_color='gray8', hover_color='gray9')
        change_appearance_button.place(x=4, y=4)

        # CTkFrame
        Frame = CTkFrame(self, width=128, height=128)
        Frame.place(x=10, y=40)

        # CTkButton
        Button = CTkButton(self)
        Button.place(x=10, y=175)

        # CTkLabel
        Label = CTkLabel(self)
        Label.place(x=10, y=210)

        # CTkEntry
        Entry = CTkEntry(self)
        Entry.place(x=10, y=240)

        # CTkCheckbox
        Checkbox = CTkCheckBox(self)
        Checkbox.place(x=10, y=275)

        # CTkSwitch
        Switch = CTkSwitch(self)
        Switch.place(x=10, y=310)

        # CTkRadiobutton
        Radiobutton = CTkRadioButton(self)
        Radiobutton.place(x=10, y=340)

        # CTkProgressbar
        Progressbar = CTkProgressBar(self)
        Progressbar.place(x=10, y=370)

        # CTkSlider
        Slider = CTkSlider(self)
        Slider.place(x=10, y=390)

        # CTkOptionmenu
        Optionmenu = CTkOptionMenu(self)
        Optionmenu.place(x=10, y=415)

        # CTkCombobox
        Combobox = CTkComboBox(self)
        Combobox.place(x=10, y=450)

        # CTkScrollbar
        Scrollbar = CTkScrollbar(self)
        Scrollbar.place(x=180, y=40)

        # CTkSegmentedbutton
        Segmentedbutton = CTkSegmentedButton(self)
        Segmentedbutton.place(x=10, y=485)

        # CTkTextbox
        Textbox = CTkTextbox(self, width=96, height=96)
        Textbox.place(x=180, y=250)

    def change_appearance(self):
        if self.appearance == 'Dark':
            self._set_appearance_mode('Light')
            self.appearance = 'Light'
        elif self.appearance == 'Light':
            self._set_appearance_mode('Dark')
            self.appearance = 'Dark'
        else:
            print(f"Error occured whilst changing appearance mode.")