import os
import json
import threading
import time
from customtkinter import *
from editor import launch
from PIL import ImageTk, Image
import src.popup.project_not_compatible as notcompatible
import dotctkt

compatibility = ['1.00']

try:
    os.listdir('ctkt_projects')
except FileNotFoundError:
    print('Creating projects folder....')
    os.mkdir('ctkt_projects')

WINDOW_TITLE = 'CTkThemer v1.00'
WINDOW_RESIZE = False, False
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
CURRENT_BUTTON = 'Projects'


def get_projects():
    files = os.listdir('ctkt_projects')
    for file in files:
        display_cont = dotctkt.get(f'ctkt_projects/{file}')

        NAME = display_cont['Project Name']
        DESC = display_cont['Project Description']
        VERS = display_cont['Version']

        if VERS in compatibility:
            if DESC == '':
                display = project_display_obj(master=scrollarea_projects, projname=NAME)
                display.pack(pady=1)
            else:
                display = project_display_obj(master=scrollarea_projects, projname=NAME, description=DESC, filename=file)
                display.pack(pady=1)
        else:
            notcompatible.open_popup(NAME)

def importing_project():
    get_file = filedialog.askopenfile()
    filename = get_file.name
    file_num = filename.count('end')
    print(file_num)

    try:
        projlist = os.listdir('ctkt_projects')
        if get_file.name.split('/')[get_file.name.split("/").count('') - 1] in projlist:
            print(get_file.name.split('/')[get_file.name.split("/").count('') - 1])
        else:
            print('gurthgrtgtrgtre')
            print(get_file.name.split('/')[get_file.name.split("/").count('') - 1])
    except Exception as e:
        print(e)


class Action_Button(CTkFrame):
    def __init__(self, master, text, tab, icon, tabview):
        self.master = master
        self.text   = text
        self.tab    = tab
        self.status = 0
        super(Action_Button, self).__init__(master=self.master, height=50, width=250, corner_radius=0,)

        self.icon = CTkImage(dark_image=Image.open(icon), size=(30,30))

        self.iconlabel = CTkLabel(self, image=self.icon, text="")
        self.iconlabel.place(x=5, y=8)

        self.textlabel = CTkLabel(self, text=self.text, font=('System', 20))
        self.textlabel.place(x=40, y=8)

        self.underline = CTkFrame(self, fg_color='gray60', corner_radius=0, height=5, width=250)

        self.iconlabel.bind('<Button-1>', self.execute)
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
            self.underline.place(x=0, y=45)
            tabview.set(self.tab)
            print(self.text)
            CURRENT_BUTTON = self.text
            app.title(f'CTkThemer - {CURRENT_BUTTON}')

    def unset(self):
        self.status = 0
        self.underline.place_forget()
        self.configure(fg_color='gray20')

    def check(self):
        while True:
            time.sleep(0.1)
            if CURRENT_BUTTON == self.text:
                pass
            else:
                self.unset()

class changelog_display(CTkFrame):
    def __init__(self, master):
        super(changelog_display, self).__init__(master=master, fg_color='gray12', width=700, height=100)

class project_display_obj(CTkFrame):
    def __init__(self, master, projname, filename, description = 'no description :('):
        super(project_display_obj, self).__init__(master=master, width=700, height=70)
        self.filename = filename
        self.description_string = description
        self.c_edit_mode = False

        self.icon = CTkLabel(self, text="", image=CTkImage(dark_image=Image.open('src/placeholder.png'), size=(64,64)))
        self.icon.place(x=3, y=3)

        self.name = CTkLabel(self, text=projname, font=CTkFont(family='Roboto Regular', size=20, weight='bold'))
        self.name.place(x=72, y=2)

        self.description = CTkLabel(self, text=description, font=CTkFont(family='Roboto Regular', size=14, weight='normal'))
        self.description.place(x=72, y=26)

        self.name_entry_var = StringVar(self, projname)
        self.name_entry = CTkEntry(self, textvariable=self.name_entry_var, corner_radius=0, border_width=0, fg_color='gray14', border_color='gray25', width=150)

        self.description_entry_var = StringVar(self, description)
        self.description_entry = CTkEntry(self, textvariable=self.description_entry_var, corner_radius=0, border_width=0, fg_color='gray14', border_color='gray25', width=300)

        self.delete = CTkButton(self, text="", fg_color='gray17', hover_color='gray20', width=24, height=24, corner_radius=0, image=CTkImage(dark_image=Image.open('src/icons/mm_projects_tab/remove_project.png'), size=(12,15)), command=self.remove)
        self.delete.place(x=676, y=0)

        self.edit = CTkButton(self, text="", fg_color='gray17', hover_color='gray20', command=self.edit_mode, width=24, height=24, corner_radius=0, image=CTkImage(dark_image=Image.open('src/icons/mm_projects_tab/edit_project.png'), size=(12,12)))
        self.edit.place(x=652, y=0)

        self.save = CTkButton(self, text="", fg_color='gray17', hover_color='gray20', command=self.edit_mode, width=24, height=24, corner_radius=0, image=CTkImage(dark_image=Image.open('src/icons/mm_projects_tab/save.png'), size=(12, 12)))

        self.bind('<Button-1>', self.action_clicked)
        self.description.bind('<Button-1>', self.action_clicked)
        self.name.bind('<Button-1>', self.action_clicked)
        self.icon.bind('<Button-1>', self.action_clicked)

    def edit_mode(self):
        if self.c_edit_mode == True:
            self.c_edit_mode = False

            with open(f"ctkt_projects/{self.filename}", 'r') as file:
                file_content = file.readlines()
                print(f">{file_content}")
            self.name_entry.place_forget()
            self.description_entry.place_forget()
            self.save.place_forget()
            self.name.place(x=72, y=2)
            self.description.place(x=72, y=26)
            self.edit.place(x=652, y=0)

            self.name.configure(text=self.name_entry_var.get())
            self.description.configure(text=self.description_entry_var.get())

            file_content[1].replace(file_content[1], self.description_string)

            with open(f"ctkt_projects/{self.filename}", "w") as file:
                file.write('')
            with open(f"ctkt_projects/{self.filename}", "a") as file:
                for var in file_content:
                    file.write(var)

            self.description_string = self.description_entry_var.get()

        elif self.c_edit_mode == False:
            self.c_edit_mode = True

            self.description.place_forget()
            self.name.place_forget()
            self.name_entry.place(x=72, y=6)
            self.description_entry.place(x=72, y=36)
            self.edit.place_forget()
            self.save.place(x=652, y=0)

    def remove(self):
        os.remove(f'ctkt_projects/{self.filename}')
        self.destroy()

    def action_clicked(self, na):
        print(f'Clicked {self.filename}')
        pass

def launch_editor():
    # Launching the editor
    launch()

def check_cb():
    print(CURRENT_BUTTON)

app = CTk(fg_color='gray10')
iconpath = ImageTk.PhotoImage(file=os.path.join("src/imgs", "logo.png"))
app.wm_iconbitmap()
app.iconphoto(True, iconpath)
app.geometry(f"{str(WINDOW_WIDTH)}x{str(WINDOW_HEIGHT)}")
app.title(WINDOW_TITLE)
app.resizable(WINDOW_RESIZE[0], WINDOW_RESIZE[1])


# Sidebar
sidebar = CTkFrame(app, width=250, height=WINDOW_HEIGHT, corner_radius=0)
sidebar.place(x=0, y=0)

tabview = CTkTabview(app, fg_color='gray10', corner_radius=0, width=750, height=WINDOW_HEIGHT+36)

logo = CTkImage(dark_image=Image.open('src/imgs/banner.png'), size=(236, 68))
sb_logo = CTkLabel(sidebar, text='', image=logo)
sb_logo.place(x=0, y=0)

# Sidebar (Action_Buttons)
projects_button = Action_Button(master=sidebar, text='Projects', tab='Projects', icon='src/icons/mm_tabbuttons/project.png', tabview=tabview)
projects_button.place(x=0, y=80)

changelog_button = Action_Button(master=sidebar, text='Changelog', tab='Changelog', icon='src/icons/mm_tabbuttons/project.png', tabview=tabview)
changelog_button.place(x=0, y=130)

# Tabs
tabview.add('Projects')
tabview.add('Changelog')

tabview._segmented_button.grid_forget()
tabview.grid_configure()

tabview.place(x=250, y=-36)

# Projects
buttonframe = CTkFrame(master=tabview.tab('Projects'), width=720, height=45, fg_color='gray13', corner_radius=6)
buttonframe.place(x=15, y=15)

buttonframe_placeholder = CTkCanvas(buttonframe, width=3, height=44, background='gray16', borderwidth=-1).place(x=85, y=0)

projects_label = CTkLabel(master=buttonframe, text="Projects", font=CTkFont(family='Noto Sans', size=16, weight='bold'))
projects_label.place(x=10, y=8)

# Projects Buttons
create_project_button = CTkButton(master=buttonframe, width=70, height=44, corner_radius=0, fg_color='gray13', font=CTkFont(family='Noto Sans', size=15, weight="normal"), hover_color='gray15', text='New', image=CTkImage(dark_image=Image.open('src/icons/mm_projects_tab/create_project.png'), size=(12,14)))
create_project_button.place(x=88, y=0)

import_project_button = CTkButton(master=buttonframe, width=85, height=44, corner_radius=0, fg_color='gray13', font=CTkFont(family='Noto Sans', size=15, weight="normal"), hover_color='gray15', text='Import', image=CTkImage(dark_image=Image.open('src/icons/mm_projects_tab/import_project.png'), size=(12,14)), command=importing_project)
import_project_button.place(x=158, y=0)

project_folder_button = CTkButton(master=buttonframe, width=85, height=44, corner_radius=0, fg_color='gray13', font=CTkFont(family='Noto Sans', size=15, weight="normal"), hover_color='gray15', text='Folder', image=CTkImage(dark_image=Image.open('src/icons/mm_projects_tab/open_project_folder.png'), size=(14,14)))
project_folder_button.place(x=240, y=0)

scrollarea_projects = CTkScrollableFrame(tabview.tab('Projects'), width=700, height=505, fg_color='gray14', corner_radius=4)
scrollarea_projects.place(x=15, y=75)

# Changelog
scrollarea_changelog = CTkScrollableFrame(tabview.tab('Changelog'), width=735, height=600, fg_color='gray10', corner_radius=0)
scrollarea_changelog.place(x=0, y=0)

get_projects()

projects_button.execute()
app.mainloop()