import customtkinter
from customtkinter import *
from pyautogui import position as mousepos
from src.ctkthemer.elements import *
from src.ctkthemer.designs import *
from src.ctkthemer.liveview import Liveview as LV
from src.templates.manage import load_template
import discordrpc
from PIL import ImageTk
from platform import system
PLATFORM = system()

settings = []
with open('settings', 'r') as f:
    cont = f.readlines()
for setting in cont:
    setting = setting.replace('\n', '')
    settings.append(setting)

# Later be configurable in settings
print(f'RPC lul: {settings[0]}')
use_rpc = settings[0]
print(f'RPC: {use_rpc}')

def rpc_manager():
    global rpc, use_rpc
    try:
        rpc = discordrpc.RPC(app_id=1261015521013530696)
        rpc.set_activity(
            state='In the Main Menu',
            small_image="logo",
        )
    except Exception:
        use_rpc = 'False'
        print("Couldn't connect to discord.")
        pass

if use_rpc == 'True':
    rpc_manager()

WINDOW_TITLE = 'CTkThemer - None'
WINDOW_RESIZE = True, True
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 640

def launch(projname, projdata, filename):
    offset = (0,0)
    print(f'following data is given: {projdata}')

    # Extracting Data
    data_CTk = str(projdata['CTk']).split(',')

    data_CTkFrame = str(projdata['CTkFrame']).split('|')
    fgcol = data_CTkFrame[2].split(',')
    bcol  = data_CTkFrame[3].split(',')
    data_CTkFrame = (data_CTkFrame[0], data_CTkFrame[1], (fgcol[0], fgcol[1]), (bcol[0], bcol[1]))

    data_CTkButton = str(projdata['CTkButton']).split('|')
    fgcol = data_CTkButton[2].split(',')
    hcol  = data_CTkButton[3].split(',')
    bcol  = data_CTkButton[4].split(',')
    tcol  = data_CTkButton[5].split(',')
    data_CTkButton = (data_CTkButton[0], data_CTkButton[1], (fgcol[0], fgcol[1]), (hcol[0], hcol[1]), (bcol[0], bcol[1]), (tcol[0], tcol[1]))

    data_CTkLabel = str(projdata['CTkLabel']).split('|')
    fgcol = data_CTkLabel[1].split(',')
    data_CTkLabel = (data_CTkLabel[0], (fgcol[0], fgcol[1]))

    data_CTkEntry = str(projdata['CTkEntry']).split('|')
    fgcol = data_CTkEntry[2].split(',')
    ptcol = data_CTkEntry[3].split(',')
    bcol = data_CTkEntry[4].split(',')
    tcol = data_CTkEntry[5].split(',')
    data_CTkEntry = (
    data_CTkEntry[0], data_CTkEntry[1], (fgcol[0], fgcol[1]), (ptcol[0], ptcol[1]), (bcol[0], bcol[1]),
    (tcol[0], tcol[1]))

    data_CTkCheckBox = str(projdata['CTkCheckBox']).split('|')
    fgcol = data_CTkCheckBox[2].split(',')
    bcol = data_CTkCheckBox[3].split(',')
    hcol = data_CTkCheckBox[4].split(',')
    chcol = data_CTkCheckBox[5].split(',')
    tcol = data_CTkCheckBox[6].split(',')
    data_CTkCheckBox = (
        data_CTkCheckBox[0], data_CTkCheckBox[1], (fgcol[0], fgcol[1]), (bcol[0], bcol[1]), (hcol[0], hcol[1]),
        (chcol[0], chcol[1]), (tcol[0], tcol[1]))

    data_CTkSwitch = str(projdata['CTkSwitch']).split('|')
    fgcol  = data_CTkSwitch[3].split(',')
    pcol   = data_CTkSwitch[4].split(',')
    bcol   = data_CTkSwitch[5].split(',')
    bhcol  = data_CTkSwitch[6].split(',')
    tcol   = data_CTkSwitch[7].split(',')
    data_CTkSwitch = (data_CTkSwitch[0], data_CTkSwitch[1], data_CTkSwitch[2], (fgcol[0], fgcol[1]), (pcol[0], pcol[1]), (bcol[0], bcol[1]), (bhcol[0], bhcol[1]), (tcol[0], tcol[1]))

    data_CTkRadioButton = str(projdata['CTkRadioButton']).split('|')
    fgcol   = data_CTkRadioButton[3].split(',')
    bcol    = data_CTkRadioButton[4].split(',')
    hcol    = data_CTkRadioButton[5].split(',')
    tcol    = data_CTkRadioButton[6].split(',')
    data_CTkRadioButton = (data_CTkRadioButton[0], data_CTkRadioButton[1], data_CTkRadioButton[2], (fgcol[0], fgcol[1]), (bcol[0], bcol[1]), (hcol[0], hcol[1]), (tcol[0], tcol[1]))

    data_CTkProgressBar = str(projdata['CTkProgressBar']).split('|')
    fgcol   = data_CTkProgressBar[2].split(',')
    pcol    = data_CTkProgressBar[3].split(',')
    bcol    = data_CTkProgressBar[4].split(',')
    data_CTkProgressBar = (data_CTkProgressBar[0], data_CTkProgressBar[1], (fgcol[0], fgcol[1]), (pcol[0], pcol[1]), (bcol[0], bcol[1]))

    data_CTkSlider = str(projdata['CTkSlider']).split('|')
    fgcol   = data_CTkSlider[4].split(',')
    pcol    = data_CTkSlider[5].split(',')
    bcol    = data_CTkSlider[6].split(',')
    bhcol   = data_CTkSlider[7].split(',')
    data_CTkSlider = (data_CTkSlider[0], data_CTkSlider[1], data_CTkSlider[2], data_CTkSlider[3], (fgcol[0], fgcol[1]), (pcol[0], pcol[1]), (bcol[0], bcol[1]), (bhcol[0], bhcol[1]))

    data_CTkOptionMenu = str(projdata['CTkOptionMenu']).split('|')
    fgcol  = data_CTkOptionMenu[1].split(',')
    bcol   = data_CTkOptionMenu[2].split(',')
    bhcol  = data_CTkOptionMenu[3].split(',')
    tcol   = data_CTkOptionMenu[4].split(',')
    data_CTkOptionMenu = (data_CTkOptionMenu[0], (fgcol[0], fgcol[1]), (bcol[0], bcol[1]), (bhcol[0], bhcol[1]), (tcol[0], tcol[1]))

    data_CTkComboBox = str(projdata['CTkComboBox']).split('|')
    fgcol  = data_CTkComboBox[2].split(',')
    bcol   = data_CTkComboBox[3].split(',')
    butcol = data_CTkComboBox[4].split(',')
    bhcol  = data_CTkComboBox[5].split(',')
    tcol   = data_CTkComboBox[6].split(',')
    data_CTkComboBox = (data_CTkComboBox[0], data_CTkComboBox[1], (fgcol[0], fgcol[1]), (bcol[0], bcol[1]), (butcol[0], butcol[1]), (bhcol[0], bhcol[1]), (tcol[0], tcol[1]))

    data_CTkScrollbar = str(projdata['Scrollbar']).split('|')
    bcol  = data_CTkScrollbar[2].split(',')
    bhcol = data_CTkScrollbar[3].split(',')
    data_CTkScrollbar = (data_CTkScrollbar[0], data_CTkScrollbar[1], (bcol[0], bcol[1]), (bhcol[0], bhcol[1]))

    data_CTkSegmentedButton = str(projdata['CTkSegmentedButton']).split('|')
    fgcol    = data_CTkSegmentedButton[2].split(',')
    scol     = data_CTkSegmentedButton[3].split(',')
    shcol    = data_CTkSegmentedButton[4].split(',')
    uscol    = data_CTkSegmentedButton[5].split(',')
    ushcol   = data_CTkSegmentedButton[6].split(',')
    tcol     = data_CTkSegmentedButton[7].split(',')
    data_CTkSegmentedButton = (data_CTkSegmentedButton[0], data_CTkSegmentedButton[1], (fgcol[0], fgcol[1]), (scol[0], scol[1]), (shcol[0], shcol[1]), (uscol[0], uscol[1]), (ushcol[0], ushcol[1]), (tcol[0], tcol[1]))

    data_DropdownMenu = str(projdata['DropdownMenu']).split('|')
    fgcol  = data_DropdownMenu[0].split(',')
    hcol   = data_DropdownMenu[1].split(',')
    tcol   = data_DropdownMenu[2].split(',')
    data_DropdownMenu = ((fgcol[0], fgcol[1]), (hcol[0], hcol[1]), (tcol[0], tcol[1]))

    MacOS_Font = str(projdata['MacOS']).split('|')
    MacOS_Data = (MacOS_Font[0], MacOS_Font[1], MacOS_Font[2])

    Windows_Font = str(projdata['Windows']).split('|')
    Windows_Data = (Windows_Font[0], Windows_Font[1], Windows_Font[2])

    Linux_Font = str(projdata['Linux']).split('|')
    Linux_Data = (Linux_Font[0], Linux_Font[1], Linux_Font[2])

    WINDOW_TITLE = f'CTkThemer - {projname}'
    app = CTkToplevel(fg_color='gray10')
    iconpath = ImageTk.PhotoImage(file=os.path.join("src/imgs", "logo.png"))
    app.wm_iconbitmap()

    if PLATFORM == 'Linux':
        app.wm_attributes("-type", "dock")
    else:
        app.overrideredirect(True)

    app.iconphoto(True, iconpath)
    app.geometry(f"{str(WINDOW_WIDTH)}x{str(WINDOW_HEIGHT)}")
    app.title(WINDOW_TITLE)
    app.resizable(WINDOW_RESIZE[0], WINDOW_RESIZE[1])

    def start_move(event):
        app.x = event.x
        app.y = event.y

    def stop_move(event):
        app.x = None
        app.y = None

    def on_move(event):
        deltax = event.x - app.x
        deltay = event.y - app.y
        x = app.winfo_x() + deltax
        y = app.winfo_y() + deltay
        app.geometry(f"+{x}+{y}")

    titlebar = CTkFrame(app, height=40, width=WINDOW_WIDTH, fg_color='gray6',  corner_radius=0)
    titlebar.place(x=0, y=0)

    titlebar.bind('<ButtonPress-1>', start_move)
    titlebar.bind('<ButtonRelease-1>', stop_move)
    titlebar.bind('<B1-Motion>', on_move)


    def close_window():
        app.destroy()

    def toggle():
        app.state('zoomed')

    def minimize():
        app.overrideredirect(False)
        app.state('withdrawn')
        app.state('iconic')

    def un_minimize():
        app.overrideredirect(True)
        app.wm_deiconify()
        app.deiconify()

    def save_project():
        def save():
            print('Saving project...')
            dCTk                 = f"{CTkDesign.fg_color.entry_dark.get()},{CTkDesign.fg_color.entry_light.get()}\n"
            dCTkFrame            = f"{CTkFrameDesign.corner_radius.entry.get()}|{CTkFrameDesign.border_width.entry.get()}|{CTkFrameDesign.fg_color.entry_dark.get()},{CTkFrameDesign.fg_color.entry_light.get()}|{CTkFrameDesign.border_color.entry_dark.get()},{CTkFrameDesign.border_color.entry_light.get()}\n"
            dCTkButton           = f"{CTkButtonDesign.corner_radius.entry.get()}|{CTkButtonDesign.border_width.entry.get()}|{CTkButtonDesign.fg_color.entry_dark.get()},{CTkButtonDesign.fg_color.entry_light.get()}|{CTkButtonDesign.hover_color.entry_dark.get()},{CTkButtonDesign.hover_color.entry_light.get()}|{CTkButtonDesign.border_color.entry_dark.get()},{CTkButtonDesign.border_color.entry_light.get()}|{CTkButtonDesign.text_color.entry_dark.get()},{CTkButtonDesign.text_color.entry_light.get()}\n"
            dCTkLabel            = f"{CTkLabelDesign.corner_radius.entry.get()}|{CTkLabelDesign.text_color.entry_dark.get()},{CTkLabelDesign.text_color.entry_light.get()}\n"
            dCTkEntry            = f"{CTkEntryDesign.corner_radius.entry.get()}|{CTkEntryDesign.border_width.entry.get()}|{CTkEntryDesign.fg_color.entry_dark.get()},{CTkEntryDesign.fg_color.entry_light.get()}|{CTkEntryDesign.border_color.entry_dark.get()},{CTkEntryDesign.border_color.entry_light.get()}|{CTkEntryDesign.text_color.entry_dark.get()},{CTkEntryDesign.text_color.entry_light.get()}|{CTkEntryDesign.placeholdertext_color.entry_dark.get()},{CTkEntryDesign.placeholdertext_color.entry_light.get()}\n"
            dCTkCheckBox         = f"{CTkCheckBoxDesign.corner_radius.entry.get()}|{CTkCheckBoxDesign.border_width.entry.get()}|{CTkCheckBoxDesign.fg_color.entry_dark.get()},{CTkCheckBoxDesign.fg_color.entry_light.get()}|{CTkCheckBoxDesign.border_color.entry_dark.get()},{CTkCheckBoxDesign.border_color.entry_light.get()}|{CTkCheckBoxDesign.hover_color.entry_dark.get()},{CTkCheckBoxDesign.hover_color.entry_light.get()}|{CTkCheckBoxDesign.checkmark_color.entry_dark.get()},{CTkCheckBoxDesign.checkmark_color.entry_light.get()}|{CTkCheckBoxDesign.text_color.entry_dark.get()},{CTkCheckBoxDesign.text_color.entry_light.get()}\n"
            dCTkSwitch           = f"{CTkSwitchDesign.corner_radius.entry.get()}|{CTkSwitchDesign.border_width.entry.get()}|{CTkSwitchDesign.button_length.entry.get()}|{CTkSwitchDesign.fg_color.entry_dark.get()},{CTkSwitchDesign.fg_color.entry_light.get()}|{CTkSwitchDesign.progress_color.entry_dark.get()},{CTkSwitchDesign.progress_color.entry_light.get()}|{CTkSwitchDesign.button_color.entry_dark.get()},{CTkSwitchDesign.button_color.entry_light.get()}|{CTkSwitchDesign.button_hover_color.entry_dark.get()},{CTkSwitchDesign.button_hover_color.entry_light.get()}|{CTkSwitchDesign.text_color.entry_dark.get()},{CTkSwitchDesign.text_color.entry_light.get()}\n"
            dCTkRadioButton      = f"{CTkRadioButtonDesign.corner_radius.entry.get()}|{CTkRadioButtonDesign.border_width_checked.entry.get()}|{CTkRadioButtonDesign.border_width_unchecked.entry.get()}|{CTkRadioButtonDesign.fg_color.entry_dark.get()},{CTkRadioButtonDesign.fg_color.entry_light.get()}|{CTkRadioButtonDesign.border_color.entry_dark.get()},{CTkRadioButtonDesign.border_color.entry_light.get()}|{CTkRadioButtonDesign.hover_color.entry_dark.get()},{CTkRadioButtonDesign.hover_color.entry_light.get()}|{CTkRadioButtonDesign.text_color.entry_dark.get()},{CTkRadioButtonDesign.text_color.entry_light.get()}\n"
            dCTkProgressBar      = f"{CTkProgressBarDesign.corner_radius.entry.get()}|{CTkProgressBarDesign.border_width.entry.get()}|{CTkProgressBarDesign.fg_color.entry_dark.get()},{CTkProgressBarDesign.fg_color.entry_light.get()}|{CTkProgressBarDesign.progress_color.entry_dark.get()},{CTkProgressBarDesign.progress_color.entry_light.get()}|{CTkProgressBarDesign.border_color.entry_dark.get()},{CTkProgressBarDesign.border_color.entry_light.get()}\n"
            dCTkSlider           = f"{CTkSliderDesign.corner_radius.entry.get()}|{CTkSliderDesign.button_corner_radius.entry.get()}|{CTkSliderDesign.border_width.entry.get()}|{CTkSliderDesign.button_length.entry.get()}|{CTkSliderDesign.fg_color.entry_dark.get()},{CTkSliderDesign.fg_color.entry_light.get()}|{CTkSliderDesign.progress_color.entry_dark.get()},{CTkSliderDesign.progress_color.entry_light.get()}|{CTkSliderDesign.button_color.entry_dark.get()},{CTkSliderDesign.button_color.entry_light.get()}|{CTkSliderDesign.button_hover_color.entry_dark.get()},{CTkSliderDesign.button_hover_color.entry_light.get()}\n"
            dCTkOptionMenu       = f"{CTkOptionMenuDesign.corner_radius.entry.get()}|{CTkOptionMenuDesign.fg_color.entry_dark.get()},{CTkOptionMenuDesign.fg_color.entry_light.get()}|{CTkOptionMenuDesign.button_color.entry_dark.get()},{CTkOptionMenuDesign.button_color.entry_light.get()}|{CTkOptionMenuDesign.button_hover_color.entry_dark.get()},{CTkOptionMenuDesign.button_hover_color.entry_light.get()}|{CTkOptionMenuDesign.text_color.entry_dark.get()},{CTkOptionMenuDesign.text_color.entry_light.get()}\n"
            dCTkComboBox         = f"{CTkComboBoxDesign.corner_radius.entry.get()}|{CTkComboBoxDesign.border_width.entry.get()}|{CTkComboBoxDesign.fg_color.entry_dark.get()},{CTkComboBoxDesign.fg_color.entry_light.get()}|{CTkComboBoxDesign.border_color.entry_dark.get()},{CTkComboBoxDesign.border_color.entry_light.get()}|{CTkComboBoxDesign.button_color.entry_dark.get()},{CTkComboBoxDesign.button_color.entry_light.get()}|{CTkComboBoxDesign.button_hover_color.entry_dark.get()},{CTkComboBoxDesign.button_hover_color.entry_light.get()}|{CTkComboBoxDesign.text_color.entry_dark.get()},{CTkComboBoxDesign.text_color.entry_light.get()}\n"
            dCTkScrollbar        = f"{CTkScrollbarDesign.corner_radius.entry.get()}|{CTkScrollbarDesign.border_spacing.entry.get()}|{CTkScrollbarDesign.button_color.entry_dark.get()},{CTkScrollbarDesign.button_color.entry_light.get()}|{CTkScrollbarDesign.button_hover_color.entry_dark.get()},{CTkScrollbarDesign.button_hover_color.entry_light.get()}\n"
            dCTkSegmentedButton  = f"{CTkSegmentedButtonDesign.corner_radius.entry.get()}|{CTkSegmentedButtonDesign.border_width.entry.get()}|{CTkSegmentedButtonDesign.fg_color.entry_dark.get()},{CTkSegmentedButtonDesign.fg_color.entry_light.get()}|{CTkSegmentedButtonDesign.selected_color.entry_dark.get()},{CTkSegmentedButtonDesign.selected_color.entry_dark.get()}|{CTkSegmentedButtonDesign.selected_hover_color.entry_dark.get()},{CTkSegmentedButtonDesign.selected_hover_color.entry_light.get()}|{CTkSegmentedButtonDesign.unselected_color.entry_dark.get()},{CTkSegmentedButtonDesign.unselected_color.entry_light.get()}|{CTkSegmentedButtonDesign.unselected_hover_color.entry_dark.get()},{CTkSegmentedButtonDesign.unselected_hover_color.entry_light.get()}|{CTkSegmentedButtonDesign.text_color.entry_dark.get()},{CTkSegmentedButtonDesign.text_color.entry_light.get()}\n"
            dDropdownMenu        = f"{DropdownMenuDesign.fg_color.entry_dark.get()},{DropdownMenuDesign.fg_color.entry_light.get()}|{DropdownMenuDesign.hover_color.entry_dark.get()},{DropdownMenuDesign.hover_color.entry_light.get()}|{DropdownMenuDesign.text_color.entry_dark.get()},{DropdownMenuDesign.text_color.entry_light.get()}\n"

            fMacOS               = f"SF Display|{FontDesign.macos_size.entry.get()}|{FontDesign.macos_weight.optionmenu.get()}\n"
            fWindows             = f"Roboto|{FontDesign.win_size.entry.get()}|{FontDesign.win_weight.optionmenu.get()}\n"
            fLinux               = f"Roboto|{FontDesign.lin_size.entry.get()}|{FontDesign.lin_weight.optionmenu.get()}\n"

            with open(f'ctkt_projects/{filename}', 'r') as f:
                curfile_cont = f.readlines()

            with open(f'ctkt_projects/{filename}', 'w') as f:
                f.write("")
                f.write(f"{curfile_cont[0]}{curfile_cont[1]}{curfile_cont[2]}{curfile_cont[3]}{dCTk}{dCTkFrame}{dCTkButton}{dCTkLabel}{dCTkEntry}{dCTkCheckBox}{dCTkSwitch}{dCTkRadioButton}{dCTkProgressBar}{dCTkSlider}{dCTkOptionMenu}{dCTkComboBox}{dCTkScrollbar}{dCTkSegmentedButton}{dDropdownMenu}{fMacOS}{fWindows}{fLinux}")

        def saq():
            save()
            app.destroy()
            win.destroy()

        def s():
            save()
            win.destroy()

        win = CTkToplevel(fg_color='gray8')
        win.wm_attributes('-type', 'dock')
        win.title('Save Project')
        win.geometry('300x150')

        button_save = CTkButton(win, text='Save', command=s, fg_color='gray20', hover_color='gray15', width=180, corner_radius=0)
        button_save.place(x=60, y=30)

        button_saveaquit = CTkButton(win, text='Save and Quit', command=saq, fg_color='gray20', hover_color='gray15', width=180, corner_radius=0)
        button_saveaquit.place(x=60, y=60)

        button_cancel = CTkButton(win, text='Cancel', command=win.destroy, fg_color='gray20', hover_color='gray15', width=180, corner_radius=0)
        button_cancel.place(x=60, y=90)


        win.mainloop()

    def generate_json():

        def generate():
            generated_json = f"""*  
  "CTk": *  
    "fg_color": ["{CTkDesign.fg_color.entry_light.get()}", "{CTkDesign.fg_color.entry_dark.get()}"] 
  !, 
  "CTkToplevel": *  
    "fg_color": ["{CTkDesign.fg_color.entry_light.get()}", "{CTkDesign.fg_color.entry_dark.get()}"]
  !,
  "CTkFrame": *  
    "corner_radius": {CTkFrameDesign.corner_radius.entry.get()}, 
    "border_width": {CTkFrameDesign.border_width.entry.get()},  
    "fg_color": ["{CTkFrameDesign.fg_color.entry_light.get()}", "{CTkFrameDesign.fg_color.entry_dark.get()}"], 
    "top_fg_color": ["{CTkFrameDesign.fg_color.entry_light.get()}", "{CTkFrameDesign.fg_color.entry_dark.get()}"],
    "border_color": ["{CTkFrameDesign.border_color.entry_light.get()}", "{CTkFrameDesign.border_color.entry_dark.get()}"]  
  !,  
  "CTkButton": *  
    "corner_radius": {CTkButtonDesign.corner_radius.entry.get()},  
    "border_width": {CTkButtonDesign.border_width.entry.get()},  
    "fg_color": ["{CTkButtonDesign.fg_color.entry_light.get()}", "{CTkButtonDesign.fg_color.entry_dark.get()}"],  
    "hover_color": ["{CTkButtonDesign.hover_color.entry_light.get()}", "{CTkButtonDesign.hover_color.entry_dark.get()}"],  
    "border_color": ["{CTkButtonDesign.border_color.entry_light.get()}", "{CTkButtonDesign.border_color.entry_dark.get()}"],  
    "text_color": ["{CTkButtonDesign.text_color.entry_light.get()}", "{CTkButtonDesign.text_color.entry_dark.get()}"],  
    "text_color_disabled": ["gray74", "gray60"]  
  !,  
  "CTkLabel": *  
    "corner_radius": {CTkLabelDesign.corner_radius.entry.get()},  
    "fg_color": "transparent",  
    "text_color": ["{CTkLabelDesign.text_color.entry_light.get()}", "{CTkLabelDesign.text_color.entry_dark.get()}"]  
  !,  
  "CTkEntry": *  
    "corner_radius": {CTkEntryDesign.corner_radius.entry.get()},  
    "border_width": {CTkEntryDesign.border_width.entry.get()},  
    "fg_color": ["{CTkEntryDesign.fg_color.entry_light.get()}", "{CTkEntryDesign.fg_color.entry_dark.get()}"],  
    "border_color": ["{CTkEntryDesign.border_color.entry_light.get()}", "{CTkEntryDesign.border_color.entry_dark.get()}"],  
    "text_color":["{CTkEntryDesign.text_color.entry_light.get()}", "{CTkEntryDesign.text_color.entry_dark.get()}"],  
    "placeholder_text_color": ["{CTkEntryDesign.placeholdertext_color.entry_light.get()}", "{CTkEntryDesign.placeholdertext_color.entry_dark.get()}"]  
  !,  
  "CTkCheckBox": *  
    "corner_radius": {CTkCheckBoxDesign.corner_radius.entry.get()},  
    "border_width": {CTkCheckBoxDesign.border_width.entry.get()},  
    "fg_color": ["{CTkCheckBoxDesign.fg_color.entry_light.get()}", "{CTkCheckBoxDesign.fg_color.entry_dark.get()}"],  
    "border_color": ["{CTkCheckBoxDesign.border_color.entry_light.get()}", "{CTkCheckBoxDesign.border_color.entry_dark.get()}"],  
    "hover_color": ["{CTkCheckBoxDesign.hover_color.entry_light.get()}", "{CTkCheckBoxDesign.hover_color.entry_dark.get()}"],  
    "checkmark_color": ["{CTkCheckBoxDesign.checkmark_color.entry_light.get()}", "{CTkCheckBoxDesign.checkmark_color.entry_dark.get()}"],  
    "text_color": ["{CTkCheckBoxDesign.text_color.entry_light.get()}", "{CTkCheckBoxDesign.text_color.entry_dark.get()}"],  
    "text_color_disabled": ["gray60", "gray45"]  
  !,  
  "CTkSwitch": *  
    "corner_radius": {CTkSwitchDesign.corner_radius.entry.get()},  
    "border_width": {CTkSwitchDesign.border_width.entry.get()},  
    "button_length": {CTkSwitchDesign.button_length.entry.get()},  
    "fg_color": ["{CTkSwitchDesign.fg_color.entry_light.get()}", "{CTkSwitchDesign.fg_color.entry_dark.get()}"],  
    "progress_color": ["{CTkSwitchDesign.progress_color.entry_light.get()}", "{CTkSwitchDesign.progress_color.entry_dark.get()}"],  
    "button_color": ["{CTkSwitchDesign.button_color.entry_light.get()}", "{CTkSwitchDesign.button_color.entry_dark.get()}"],  
    "button_hover_color": ["{CTkSwitchDesign.button_hover_color.entry_light.get()}", "{CTkSwitchDesign.button_hover_color.entry_dark.get()}"],  
    "text_color": ["{CTkSwitchDesign.text_color.entry_light.get()}", "{CTkSwitchDesign.text_color.entry_dark.get()}"],  
    "text_color_disabled": ["gray60", "gray45"]  
  !,  
  "CTkRadioButton": *  
    "corner_radius": {CTkRadioButtonDesign.corner_radius.entry.get()},  
    "border_width_checked": {CTkRadioButtonDesign.border_width_checked.entry.get()},  
    "border_width_unchecked": {CTkRadioButtonDesign.border_width_unchecked.entry.get()},  
    "fg_color": ["{CTkRadioButtonDesign.fg_color.entry_light.get()}", "{CTkRadioButtonDesign.fg_color.entry_dark.get()}"],  
    "border_color": ["{CTkRadioButtonDesign.border_color.entry_light.get()}", "{CTkRadioButtonDesign.border_color.entry_dark.get()}"],  
    "hover_color": ["{CTkRadioButtonDesign.hover_color.entry_light.get()}", "{CTkRadioButtonDesign.hover_color.entry_dark.get()}"],  
    "text_color": ["{CTkRadioButtonDesign.text_color.entry_light.get()}", "{CTkRadioButtonDesign.text_color.entry_dark}"],  
    "text_color_disabled": ["gray60", "gray45"]  
  !,  
  "CTkProgressBar": *  
    "corner_radius": {CTkProgressBarDesign.corner_radius.entry.get()},  
    "border_width": {CTkProgressBarDesign.border_width.entry.get()},  
    "fg_color": ["{CTkProgressBarDesign.fg_color.entry_light.get()}", "{CTkProgressBarDesign.fg_color.entry_dark.get()}"],  
    "progress_color": ["{CTkProgressBarDesign.progress_color.entry_light.get()}", "{CTkProgressBarDesign.progress_color.entry_dark.get()}"],  
    "border_color": ["{CTkProgressBarDesign.border_color.entry_light.get()}", "{CTkProgressBarDesign.border_color.entry_dark.get()}"]  
  !,  
  "CTkSlider": *  
    "corner_radius": {CTkSliderDesign.corner_radius.entry.get()},  
    "button_corner_radius": {CTkSliderDesign.button_corner_radius.entry.get()},  
    "border_width": {CTkSliderDesign.border_width.entry.get()},  
    "button_length": {CTkSliderDesign.button_length.entry.get()},  
    "fg_color": ["{CTkSliderDesign.fg_color.entry_light.get()}", "{CTkSliderDesign.fg_color.entry_dark.get()}"],  
    "progress_color": ["{CTkSliderDesign.progress_color.entry_light.get()}", "#{CTkSliderDesign.progress_color.entry_dark.get()}"],  
    "button_color": ["{CTkSliderDesign.button_color.entry_light.get()}", "{CTkSliderDesign.button_color.entry_dark.get()}"],  
    "button_hover_color": ["{CTkSliderDesign.button_hover_color.entry_light.get()}", "{CTkSliderDesign.button_hover_color.entry_dark.get()}"]  
  !,  
  "CTkOptionMenu": *  
    "corner_radius": {CTkOptionMenuDesign.corner_radius.entry.get()},  
    "fg_color": ["{CTkOptionMenuDesign.fg_color.entry_light.get()}", "{CTkOptionMenuDesign.fg_color.entry_dark.get()}"],  
    "button_color": ["{CTkOptionMenuDesign.button_color.entry_light.get()}", "{CTkOptionMenuDesign.button_color.entry_dark.get()}"],  
    "button_hover_color": ["{CTkOptionMenuDesign.button_hover_color.entry_light.get()}", "{CTkOptionMenuDesign.button_hover_color.entry_dark.get()}"],  
    "text_color": ["{CTkOptionMenuDesign.text_color.entry_light.get()}", "{CTkOptionMenuDesign.text_color.entry_dark.get()}"],  
    "text_color_disabled": ["gray74", "gray60"]  
  !,  
  "CTkComboBox": *  
    "corner_radius": {CTkComboBoxDesign.corner_radius.entry.get()},  
    "border_width": {CTkComboBoxDesign.border_width.entry.get()},  
    "fg_color": ["{CTkComboBoxDesign.fg_color.entry_light.get()}", "{CTkComboBoxDesign.fg_color.entry_dark.get()}"],  
    "border_color": ["{CTkComboBoxDesign.border_color.entry_light.get()}", "{CTkComboBoxDesign.border_color.entry_dark.get()}"],  
    "button_color": ["{CTkComboBoxDesign.button_color.entry_light.get()}", "{CTkComboBoxDesign.button_color.entry_dark.get()}"],  
    "button_hover_color": ["{CTkComboBoxDesign.button_hover_color.entry_light.get()}", "{CTkComboBoxDesign.button_hover_color.entry_dark.get()}"],  
    "text_color": ["{CTkComboBoxDesign.text_color.entry_light.get()}", "{CTkComboBoxDesign.text_color.entry_dark.get()}"],  
    "text_color_disabled": ["gray50", "gray45"]  
  !,  
  "CTkScrollbar": *  
    "corner_radius": {CTkScrollbarDesign.corner_radius.entry.get()}],  
    "border_spacing": {CTkScrollbarDesign.border_spacing.entry.get()},  
    "fg_color": "transparent",  
    "button_color": ["{CTkScrollbarDesign.button_color.entry_light.get()}", "{CTkScrollbarDesign.button_color.entry_dark.get()}"],  
    "button_hover_color": ["{CTkScrollbarDesign.button_hover_color.entry_light.get()}", "{CTkScrollbarDesign.button_hover_color.entry_dark.get()}"]  
  !,  
  "CTkSegmentedButton": *  
    "corner_radius": {CTkSegmentedButtonDesign.corner_radius.entry.get()},  
    "border_width": {CTkSegmentedButtonDesign.border_width.entry.get()},  
    "fg_color": ["{CTkSegmentedButtonDesign.fg_color.entry_light.get()}", "{CTkSegmentedButtonDesign.fg_color.entry_dark.get()}"],  
    "selected_color": ["{CTkSegmentedButtonDesign.selected_color.entry_light.get()}", "{CTkSegmentedButtonDesign.selected_color.entry_dark.get()}"],  
    "selected_hover_color": ["{CTkSegmentedButtonDesign.selected_hover_color.entry_light.get()}", "{CTkSegmentedButtonDesign.selected_hover_color.entry_dark.get()}"],  
    "unselected_color": ["{CTkSegmentedButtonDesign.unselected_color.entry_light.get()}", "{CTkSegmentedButtonDesign.unselected_color.entry_dark.get()}"],  
    "unselected_hover_color": ["{CTkSegmentedButtonDesign.unselected_hover_color.entry_light.get()}", "{CTkSegmentedButtonDesign.unselected_hover_color.entry_dark.get()}"],  
    "text_color": ["{CTkSegmentedButtonDesign.text_color.entry_light.get()}", "{CTkSegmentedButtonDesign.text_color.entry_light.get()}"],  
    "text_color_disabled": ["gray74", "gray60"]  
  !,  
  "CTkTextbox": *  
    "corner_radius": 6,  
    "border_width": 0,  
    "fg_color": ["#F9F9FA", "#1D1E1E"],  
    "border_color": ["#979DA2", "#565B5E"],  
    "text_color":["gray10", "#DCE4EE"],  
    "scrollbar_button_color": ["gray55", "gray41"],  
    "scrollbar_button_hover_color": ["gray40", "gray53"]  
  !,  
  "CTkScrollableFrame": *  
    "label_fg_color": ["gray78", "gray23"]  
  !,  
  "DropdownMenu": *  
    "fg_color": ["{DropdownMenuDesign.fg_color.entry_light.get()}", "{DropdownMenuDesign.fg_color.entry_dark.get()}"],  
    "hover_color": ["{DropdownMenuDesign.hover_color.entry_light.get()}", "{DropdownMenuDesign.hover_color.entry_dark.get()}"],  
    "text_color": ["{DropdownMenuDesign.text_color.entry_light.get()}", "{DropdownMenuDesign.text_color.entry_dark.get()}"]  
  !,  
  "CTkFont": *  
    "macOS": *  
      "family": "SF Display",  
      "size": {FontDesign.macos_size.entry.get()},  
      "weight": "{FontDesign.macos_weight.optionmenu.get()}"  
    !,  
    "Windows": *  
      "family": "Roboto",  
      "size": {FontDesign.win_size.entry.get()},  
      "weight": "{FontDesign.win_weight.optionmenu.get()}"  
    !,  
    "Linux": *  
      "family": "Roboto",  
      "size": {FontDesign.lin_size.entry.get()},  
      "weight": "{FontDesign.lin_weight.optionmenu.get()}"  
    !  
  !  
!"""
            generated_json = generated_json.replace('*', '{')
            generated_json = generated_json.replace('!', '}')
            print(generated_json)
            name = entry_filename.get()
            win.destroy()
            path = filedialog.asksaveasfilename(title='Save Json file', defaultextension='.json', initialfile=f'{name}.json', confirmoverwrite=True)
            with open(path, 'w') as file:
                file.write(generated_json)

        win = CTkToplevel(fg_color='gray8')
        win.wm_attributes('-type', 'dock')
        win.title('Generate Json')
        win.geometry('320x150')

        entry_filename = CTkEntry(win, placeholder_text='Filename *extension is automatically added*', width=310, corner_radius=0, fg_color='gray5', border_width=0)
        entry_filename.place(x=5, y=5)

        image_frame = CTkFrame(win, fg_color='gray6', corner_radius=0, width=310, height=85)
        image_frame.place(x=5, y=35)

        cancel_button = CTkButton(win, text='Cancel', command=win.destroy, fg_color='gray10', hover_color='gray5', width=160, corner_radius=0)
        cancel_button.place(x=0, y=122)

        generate_button = CTkButton(win, text='Generate', command=generate, fg_color='gray10', hover_color='gray5', width=160, corner_radius=0)
        generate_button.place(x=160, y=122)

        win.mainloop()

    app.protocol('WM_TAKE_FOCUS', un_minimize)


    logo = CTkButton(titlebar, text='', image=CTkImage(dark_image=Image.open('src/imgs/logo.png'), size=(28,28)), width=40, height=40, corner_radius=0, fg_color='gray6', hover_color='gray8')
    logo.place(x=0, y=0)

    save_button = CTkButton(titlebar, text='', image=CTkImage(dark_image=Image.open('src/icons/titlebar/save.png'), size=(18, 20)), width=40, height=40, corner_radius=0, fg_color='gray6', hover_color='gray8', command=save_project)
    save_button.place(x=40, y=0)

    generate_button = CTkButton(titlebar, text='', image=CTkImage(dark_image=Image.open('src/icons/titlebar/generate.png'), size=(20, 20)), width=40, height=40, corner_radius=0, fg_color='gray6', hover_color='gray8', command=generate_json)
    generate_button.place(x=80, y=0)

    close_button = CTkButton(titlebar, text='', image=CTkImage(dark_image=Image.open('src/icons/titlebar/close.png'), size=(16,16)), width=40, height=40, fg_color='gray6', hover_color='gray8', corner_radius=0, command=close_window)
    close_button.place(x=960, y=0)

    window_toggle = CTkButton(titlebar, text='', image=CTkImage(dark_image=Image.open('src/icons/titlebar/fullscreen.png'), size=(15, 17)), width=40, height=40, fg_color='gray6', hover_color='gray8', corner_radius=0, command=toggle)
    window_toggle.place(x=920, y=0)

    minimize_button = CTkButton(titlebar, text='', image=CTkImage(dark_image=Image.open('src/icons/titlebar/minimize.png'), size=(16, 16)), width=40, height=40, fg_color='gray6', hover_color='gray8', corner_radius=0, command=minimize)
    minimize_button.place(x=880, y=0)

    if PLATFORM == 'Linux':
        minimize_button.configure(state='disabled')

    sidebar = CTkScrollableFrame(master=app, width=300, height=int(WINDOW_HEIGHT - 40), fg_color='gray7', corner_radius=0)
    sidebar._scrollbar.configure(corner_radius=1000, width=16, button_color='gray24', button_hover_color='gray20')
    sidebar.place(x=0, y=40)

    if use_rpc == True:
        rpc.set_activity(
            state=f'working on {projname}',
            small_image="logo",
        )

    Liveview = LV(master=app)
    Liveview.place(x=327, y=50)

    CTkDesign = design_CTk(master=sidebar, fgcolor=(data_CTk[0], data_CTk[1]))
    CTkDesign.pack(fill='both', pady=0)

    CTkFrameDesign = design_CTkFrame(master=sidebar, cornerradius=data_CTkFrame[0], borderwidth=data_CTkFrame[1], fgcolor=data_CTkFrame[2], bordercolor=data_CTkFrame[3], LV=Liveview)
    CTkFrameDesign.pack(fill='both', pady=0)

    CTkButtonDesign = design_CTkButton(master=sidebar, cornerradius=data_CTkButton[0], borderwidth=data_CTkButton[1], fgcolor=data_CTkButton[2], hovercolor=data_CTkButton[3], bordercolor=data_CTkButton[4], textcolor=data_CTkButton[5])
    CTkButtonDesign.pack(fill='both', pady=0)

    CTkLabelDesign = design_CTkLabel(master=sidebar, cornerradius=data_CTkLabel[0], textcolor=data_CTkLabel[1])
    CTkLabelDesign.pack(fill='both', pady=0)

    CTkEntryDesign = design_CTkEntry(master=sidebar, cornerradius=data_CTkEntry[0], borderwidth=data_CTkEntry[1], fgcolor=data_CTkEntry[2], ptextcolor=data_CTkEntry[3], bordercolor=data_CTkEntry[4], textcolor=data_CTkEntry[5])
    CTkEntryDesign.pack(fill='both', pady=0)

    CTkCheckBoxDesign = design_CTkCheckBox(master=sidebar, cornerradius=data_CTkCheckBox[0], borderwidth=data_CTkCheckBox[1], fgcolor=data_CTkCheckBox[2], bordercolor=data_CTkCheckBox[3], hovercolor=data_CTkCheckBox[4], checkcolor=data_CTkCheckBox[5], textcolor=data_CTkCheckBox[6])
    CTkCheckBoxDesign.pack(fill='both', pady=0)

    CTkSwitchDesign = design_CTkSwitch(master=sidebar, cornerradius=data_CTkSwitch[0], borderwidth=data_CTkSwitch[1], buttonlength=data_CTkSwitch[2], fgcolor=data_CTkSwitch[3], progresscolor=data_CTkSwitch[4], buttoncolor=data_CTkSwitch[5], buttonhovercolor=data_CTkSwitch[6], textcolor=data_CTkSwitch[7])
    CTkSwitchDesign.pack(fill='both', pady=0)

    CTkRadioButtonDesign = design_CTkRadioButton(master=sidebar, cornerradius=data_CTkRadioButton[0], borderwidthchecked=data_CTkRadioButton[1], borderwidthunchecked=data_CTkRadioButton[2], fgcolor=data_CTkRadioButton[3], bordercolor=data_CTkRadioButton[4], hovercolor=data_CTkRadioButton[5], textcolor=data_CTkRadioButton[6])
    CTkRadioButtonDesign.pack(fill='both', pady=0)

    CTkProgressBarDesign = design_CTkProgressBar(master=sidebar, cornerradius=data_CTkProgressBar[0], borderwidth=data_CTkProgressBar[1], fgcolor=data_CTkProgressBar[2], progresscolor=data_CTkProgressBar[3], bordercolor=data_CTkProgressBar[4])
    CTkProgressBarDesign.pack(fill='both', pady=0)

    CTkSliderDesign = design_CTkSlider(master=sidebar, cornerradius=data_CTkSlider[0], buttoncornerradius=data_CTkSlider[1], borderwidth=data_CTkSlider[2], buttonlength=data_CTkSlider[3], fgcolor=data_CTkSlider[4], progresscolor=data_CTkSlider[5], buttoncolor=data_CTkSlider[6], buttonhovercolor=data_CTkSlider[7])
    CTkSliderDesign.pack(fill='both', pady=0)

    CTkOptionMenuDesign = design_CTkOptionMenu(master=sidebar, cornerradius=data_CTkOptionMenu[0], fgcolor=data_CTkOptionMenu[1], buttoncolor=data_CTkOptionMenu[2], buttonhovercolor=data_CTkOptionMenu[3], textcolor=data_CTkOptionMenu[4])
    CTkOptionMenuDesign.pack(fill='both', pady=0)

    CTkComboBoxDesign = design_CTkComboBox(master=sidebar, cornerradius=data_CTkComboBox[0], borderwidth=data_CTkComboBox[1], fgcolor=data_CTkComboBox[2], bordercolor=data_CTkComboBox[3], buttoncolor=data_CTkComboBox[4], buttonhovercolor=data_CTkComboBox[5], textcolor=data_CTkComboBox[6])
    CTkComboBoxDesign.pack(fill='both', pady=0)

    CTkScrollbarDesign = design_CTkScrollbar(master=sidebar, cornerradius=data_CTkScrollbar[0], borderspacing=data_CTkScrollbar[1], buttoncolor=data_CTkScrollbar[2], buttonhovercolor=data_CTkScrollbar[3])
    CTkScrollbarDesign.pack(fill='both', pady=0)

    CTkSegmentedButtonDesign = design_CTkSegmentedButton(master=sidebar, cornerradius=data_CTkSegmentedButton[0], borderwidth=data_CTkSegmentedButton[1], fgcolor=data_CTkSegmentedButton[2], selectedcolor=data_CTkSegmentedButton[3], selectedhovercolor=data_CTkSegmentedButton[4], unselectedcolor=data_CTkSegmentedButton[5], unselectedhovercolor=data_CTkSegmentedButton[6], textcolor=data_CTkSegmentedButton[7])
    CTkSegmentedButtonDesign.pack(fill='both', pady=0)

    DropdownMenuDesign = design_DropdownMenu(master=sidebar, fgcolor=data_DropdownMenu[0], hovercolor=data_DropdownMenu[1], textcolor=data_DropdownMenu[2])
    DropdownMenuDesign.pack(fill='both', pady=0)

    FontDesign = design_CTkFont(master=sidebar,
                                size_mac=int(MacOS_Data[1]), weight_mac=MacOS_Data[2],
                                size_win=int(Windows_Data[1]), weight_win=Windows_Data[2],
                                size_lin=int(Linux_Data[1]), weight_lin=Linux_Data[2],
                                )
    FontDesign.pack(fill='both', pady=0)

    app.mainloop()

if __name__ == '__main__':
    launch('Lol', {}, "lmao.ctkt")