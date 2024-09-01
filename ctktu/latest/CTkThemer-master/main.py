import os
import json
import threading
import time
from customtkinter import *
from editor import launch
from src.ctkthemer.elements import settings_switch_option_display, settings_optionmenu_option_display
from PIL import ImageTk, Image
import src.menus.create_project
import src.scripts.open_project
import src.popup.project_not_compatible as notcompatible
import src.popup.project_file_wrongformat as wrongformat
import dotctkt

compatibility       = [ '1.00' ]
loaded_projects     = []
loaded_projects_obj = []

try:
    os.listdir('ctkt_projects')
except FileNotFoundError:
    print('Creating projects folder....')
    os.mkdir('ctkt_projects')

WINDOW_TITLE = 'CTkThemer - Loading...'
WINDOW_RESIZE = False, False
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
CURRENT_BUTTON = 'Projects'


def get_projects():
    global loaded_projects
    files = os.listdir('ctkt_projects')
    for file in files:
        display_cont = dotctkt.get(f'ctkt_projects/{file}')

        required_data = ['CTk', 'CTkFrame', 'CTkButton', 'CTkLabel', 'CTkEntry', 'CTkCheckBox', 'CTkSwitch', 'CTkRadioButton', 'CTkProgressBar', 'CTkSlider', 'CTkOptionMenu', 'CTkComboBox', 'Scrollbar', 'CTkSegmentedButton', 'DropdownMenu', 'MacOS', 'Windows', 'Linux']

        NAME = display_cont['Project Name']
        DESC = display_cont['Project Description']
        VERS = display_cont['Version']


        count    = 0
        projdata = {}
        try:
            for arg in required_data:
                argdata = display_cont[arg]

                projdata[arg] = argdata

                print('DATA: ' + argdata)
                count += 1
            print('projdata:' + str(projdata))

            if VERS in compatibility:
                if DESC == '':
                    if file in loaded_projects:
                        pass
                    else:
                        display = project_display_obj(master=scrollarea_projects, projname=NAME)
                        display.pack(pady=1)
                        loaded_projects.append(file)
                else:
                    if file in loaded_projects:
                        pass
                    else:
                        display = project_display_obj(master=scrollarea_projects, projname=NAME, description=DESC,
                                                      filename=file, data=projdata)
                        display.pack(pady=1)
                        loaded_projects.append(file)
                        loaded_projects_obj.append(display)
            else:
                notcompatible.open_popup(NAME)
        except Exception as e:
            print(e)
            pass

def importing_project():
    get_file = filedialog.askopenfile()
    filepath       = get_file.name
    filepath_parts = filepath.split('/')
    filename       = filepath_parts[len(filepath_parts) - 1]
    file_content   = get_file.readlines()

    if str(filename).endswith('.ctkt'):
        try:
            all_projects = os.listdir('ctkt_projects')
            if filename in all_projects:
                print('Project already exists')
                pass
            else:
                with open(f'ctkt_projects/{filename}', 'a') as file:
                    curnum = 0
                    print(type(file_content))
                    print(file_content)
                    print(len(file_content))
                    for i in range(len(file_content)):
                        file.write(file_content[curnum])
                        curnum += 1
                get_projects()
        except Exception as e:
            print(f"An error occured whilst importing the project. ({e})")
    else:
        t___format = str(filename).split('.')
        wrongformat.open_popup(format=t___format[len(t___format) - 1])

class Action_Button(CTkFrame):
    def __init__(self, master, text, tab, icon, tabview):
        self.master = master
        self.text   = text
        self.tab    = tab
        self.status = 0
        super(Action_Button, self).__init__(master=self.master, height=50, width=250, corner_radius=0,)

        print(f"{self} {text}, {tab}")

        self.icon = CTkImage(dark_image=Image.open(icon), size=(30,30))

        self.iconlabel = CTkLabel(self, image=self.icon, text="")
        self.iconlabel.place(x=5, y=8)

        self.textlabel = CTkLabel(self, text=self.text, font=('System', 20))
        self.textlabel.place(x=40, y=8)

        self.underline = CTkFrame(self, fg_color='gray60', corner_radius=0, height=5, width=250)

        self.iconlabel.bind('<Button-1>', self.execute)
        self.textlabel.bind('<Button-1>', self.execute)
        self.bind('<Button-1>', self.execute)

    def execute(self, *args):
        global CURRENT_BUTTON
        print('lol')
        if self.status == 0:
            for butt in action_buttons:
                butt.unset()
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

class changelog_display(CTkFrame):
    def __init__(self, master):
        super(changelog_display, self).__init__(master=master, fg_color='gray12', width=700, height=100)

class project_display_obj(CTkFrame):
    def __init__(self, master, projname, filename, description = 'no description :(', data = {}):
        super(project_display_obj, self).__init__(master=master, width=700, height=70)
        self.filename = filename
        self.description_string = description
        self.c_edit_mode = False
        self.data        = data

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

            print('DEBUG:' + str(file_content))

            file_content.pop(0)
            file_content.pop(0)
            print(file_content)

            new_file_cont = []
            new_file_cont.append(self.name_entry_var.get())
            new_file_cont.append(self.description_entry_var.get())
            for _var in file_content:
                _var = _var.replace('\n', '')
                new_file_cont.append(_var)

            with open(f"ctkt_projects/{self.filename}", "w") as file:
                file.write('')
            with open(f"ctkt_projects/{self.filename}", "a") as file:
                print(new_file_cont)
                for var in new_file_cont:
                    file.write(f"{var}\n")

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
        src.scripts.open_project.open_project(self.filename, self.data)
        print('refreshing')
        for proj in loaded_projects_obj:
            proj.destroy()
        app.mainloop()


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

themes_button = Action_Button(master=sidebar, text='Themes', tab='Themes', icon='src/icons/mm_tabbuttons/project.png', tabview=tabview)
themes_button.place(x=0, y=130)

settings_button = Action_Button(master=sidebar, text='Settings', tab='Settings', icon='src/icons/mm_tabbuttons/project.png', tabview=tabview)
settings_button.place(x=0, y=180)

changelog_button = Action_Button(master=sidebar, text='Changelog', tab='Changelog', icon='src/icons/mm_tabbuttons/project.png', tabview=tabview)
changelog_button.place(x=0, y=230)

action_buttons = [projects_button, themes_button, settings_button, changelog_button]

# Tabs
tabview.add('Projects')
tabview.add('Themes')
tabview.add('Settings')
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

def use_createproject():
    status = src.menus.create_project._open()
    print("LOL>"+str(status))
    if status == 1:
        get_projects()
    else:
        pass

def open_projectfolder():
    os.system('dolphin /home/davidd/PycharmProjects/CTkThemer/ctkt_projects')

# Projects Buttons
create_project_button = CTkButton(master=buttonframe, width=70, height=44, corner_radius=0, fg_color='gray13', font=CTkFont(family='Noto Sans', size=15, weight="normal"), hover_color='gray15', text='New', image=CTkImage(dark_image=Image.open('src/icons/mm_projects_tab/create_project.png'), size=(12,14)), command=use_createproject)
create_project_button.place(x=88, y=0)

import_project_button = CTkButton(master=buttonframe, width=85, height=44, corner_radius=0, fg_color='gray13', font=CTkFont(family='Noto Sans', size=15, weight="normal"), hover_color='gray15', text='Import', image=CTkImage(dark_image=Image.open('src/icons/mm_projects_tab/import_project.png'), size=(12,14)), command=importing_project)
import_project_button.place(x=158, y=0)

project_folder_button = CTkButton(master=buttonframe, width=85, height=44, corner_radius=0, fg_color='gray13', font=CTkFont(family='Noto Sans', size=15, weight="normal"), hover_color='gray15', text='Folder', image=CTkImage(dark_image=Image.open('src/icons/mm_projects_tab/open_project_folder.png'), size=(14,14)), command=open_projectfolder)
project_folder_button.place(x=240, y=0)

scrollarea_projects = CTkScrollableFrame(tabview.tab('Projects'), width=700, height=505, fg_color='gray14', corner_radius=4)
scrollarea_projects.place(x=15, y=75)

# Changelog
scrollarea_changelog = CTkScrollableFrame(tabview.tab('Changelog'), width=735, height=600, fg_color='gray10', corner_radius=0)
scrollarea_changelog.place(x=0, y=0)

# Settings
scrollarea_Settings = CTkScrollableFrame(tabview.tab('Settings'), width=735, height=600, fg_color='gray10', corner_radius=0)
scrollarea_Settings.place(x=0, y=0)

# Settings [Options]
with open('settings', 'r') as f:
    settings = f.readlines()
test_settingsoption = settings_switch_option_display(scrollarea_Settings, text='Use Discord rpc', slot=0, start=settings[0].replace('\n', ''))
test2_settingsoption = settings_switch_option_display(scrollarea_Settings, text='Use Lmao ;)', slot=1, start=settings[1].replace('\n', ''))
test3_settingsoption = settings_switch_option_display(scrollarea_Settings, text='Yo mei', slot=2, start=settings[2].replace('\n', ''))

test_optionmenu_settingsoption = settings_optionmenu_option_display(scrollarea_Settings, text='????', slot=3, start=settings[3].replace('\n', ''))
test_optionmenu_settingsoption.optionmenu.configure(values=['test1', 'test2', 'test3'])

test4_settingsoption = settings_switch_option_display(scrollarea_Settings, text='ambatta busssszzzzsss', slot=4, start=settings[4].replace('\n', ''))

projects_button.execute()
get_projects()
app.mainloop()