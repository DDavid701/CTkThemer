from customtkinter import *
from PIL import Image
import time
import threading

CURRENT_BUTTON = 'Projects'
to_return = 0

class Action_Button(CTkFrame):
    def __init__(self, master, text, tab, icon, tabview):
        self.master = master
        self.text   = text
        self.tab    = tab
        self.status = 0
        super(Action_Button, self).__init__(master=self.master, height=30, width=140, corner_radius=0,)

        self.textlabel = CTkLabel(self, text=self.text, font=('System', 16))
        self.textlabel.place(x=5, y=1)

        self.textlabel.bind('<Button-1>', self.execute)
        self.bind('<Button-1>', self.execute)

        self.checkthrd = threading.Thread(target=self.check)
        self.checkthrd.start()

    def execute(self, *args):
        global CURRENT_BUTTON
        print('lol')
        if self.status == 0:
            print('0')
            self.status = 1
            self.configure(fg_color='gray24')
            tabview.set(self.tab)
            print(self.text)
            CURRENT_BUTTON = self.text

    def unset(self):
        self.status = 0
        self.configure(fg_color='gray20')

    def check(self):
        while True:
            time.sleep(0.1)
            if CURRENT_BUTTON == self.text:
                pass
            else:
                self.unset()

def _open():
    global tabview, win
    win = CTk()
    win.geometry('500x300')
    win.resizable(False, False)
    win.title('CTkThemer - Create Project')

    sidebar = CTkFrame(win, width=140, height=300, corner_radius=0, fg_color='gray11')
    sidebar.place(x=0,y=0)

    sidebar_shadow = CTkFrame(win, width=6, height=300, fg_color='gray12', corner_radius=0)
    sidebar_shadow.place(x=140)

    tabview = CTkTabview(win, width=356, height=337, fg_color='gray14', corner_radius=0)

    tabview.add('defaultblue')
    defaultbluetab = tabview.tab('defaultblue')

    # Standard (Tab)

    def create_defaultblue():
        global to_return
        global to_returne
        Name        = Name_Entry.get()
        Description = Description_Entry.get()
        Icon        = Icon_Filepath.get()
        if Name == '':
            print('No name set.')
        else:
            if Icon == '':
                Icon = 'default'
            if Description == '':
                Description = 'no description :('

            try:
                with open(f'ctkt_projects/{Name}.ctkt', "a") as file:
                    file.write(f"{Name}\n")
                    file.write(f"{Description}\n")
                    file.write(f"{Icon}\n")
                    file.write('1.00\n')
                    with open(f'src/templates/default_blue', 'r') as template:
                        template_cont = template.read()
                    file.write(template_cont)
                to_return = 1
                print(f"TORETURNE = {to_return}")
                win.quit()
            except Exception as e:
                print(e)

    def on_close():
        win.quit()

    win.protocol('WM_DELETE_WINDOW', on_close)

    Name_Entry = CTkEntry(defaultbluetab, placeholder_text='Project Name', fg_color='gray10', border_width=0, corner_radius=0)
    Name_Entry.place(x=10, y=10)

    Description_Entry = CTkEntry(defaultbluetab, fg_color='gray10', placeholder_text='Project Description', border_width=0, corner_radius=0, width=190)
    Description_Entry.place(x=155, y=10)

    Icon_Filepath = CTkEntry(defaultbluetab, fg_color='gray10', placeholder_text='Icon Filepath *optional*', border_width=0, corner_radius=0, width=335)
    Icon_Filepath.place(x=10, y=45)

    defaultblue_Done_Button = CTkButton(defaultbluetab, fg_color='gray11', hover_color='gray18', text='Done', command=create_defaultblue, corner_radius=0)
    defaultblue_Done_Button.place(x=215, y=273)

    # Sidebar (Action_Buttons)
    defaultblue_button = Action_Button(master=sidebar, text='Default Blue', tab='defaultblue', icon='/home/davidd/PycharmProjects/CTkThemer/src/icons/mm_tabbuttons/project.png', tabview=tabview)
    defaultblue_button.place(x=0, y=0)

    tabview._segmented_button.grid_forget()
    tabview.grid_configure()
    tabview.place(x=145, y=-36)


    defaultblue_button.execute()
    win.mainloop()
    win.destroy()
    print(f'TORETURN = {to_return}')
    return to_return

if __name__ == '__main__':
    _open()