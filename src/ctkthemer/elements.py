from customtkinter import *

class CTkBox(CTkFrame):
    def __init__(self, text, master):
        self.text   = text
        self.master = master
        self._specs = {'size_w': 150,
                       'size_h': 200,}
        super(CTkBox, self).__init__(master=master, width=self._specs['size_w'], height=self._specs['size_h'], fg_color='red', corner_radius=5)

        self.topframe = CTkFrame(self, width=290, height=30, fg_color='green', corner_radius=4)
        self.topframe.pack(pady=4)
        self.boxlabel = CTkLabel(master=self.topframe, text=text, font=('System', 20))._font
        self.boxlabel.place(x=0, y=0)




class Number_Input(CTkFrame):
    def __init__(self, master):
        self.master = master
        self._specs = {'size_w': 150,
                       'size_y': 200,}
        super(Number_Input, self).__init__(master=master, width=self._specs['size_w'], height=self._specs['size_y'])
        self.button = CTkButton(self, text="Button :)").place(x=0, y=0)


    def vars(self):
        print(self.master)