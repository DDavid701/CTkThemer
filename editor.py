from customtkinter import *
from src.ctkthemer.elements import *
from src.ctkthemer.designs import *
from src.ctkthemer.liveview import Liveview as LV
from src.templates.manage import load_template
import discordrpc
from PIL import ImageTk

# Later be configurable in settings
use_rpc = False

def rpc_manager():
    global rpc, use_rpc
    try:
        rpc = discordrpc.RPC(app_id=1261015521013530696)
        rpc.set_activity(
            state='In the Main Menu',
            small_image="logo",
        )
    except Exception:
        use_rpc = False
        print("Couldn't connect to discord.")
        pass

if use_rpc == True:
    rpc_manager()

WINDOW_TITLE = 'CTkThemer'
WINDOW_RESIZE = False, False
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

def launch():
    app = CTk(fg_color='gray10')
    iconpath = ImageTk.PhotoImage(file=os.path.join("src/imgs", "logo.png"))
    app.wm_iconbitmap()
    app.iconphoto(True, iconpath)
    app.geometry(f"{str(WINDOW_WIDTH)}x{str(WINDOW_HEIGHT)}")
    app.title(WINDOW_TITLE)
    app.resizable(WINDOW_RESIZE[0], WINDOW_RESIZE[1])

    sidebar = CTkScrollableFrame(master=app, width=300, height=int(WINDOW_HEIGHT - 10), fg_color='gray8')
    sidebar._scrollbar.configure(corner_radius=1000, width=16, button_color='gray24', button_hover_color='gray20')
    sidebar.place(x=0, y=0)

    if use_rpc == True:
        rpc.set_activity(
            state='working on %project%',
            small_image="logo",
        )

    CTkDesign = design_CTk(master=sidebar)
    CTkDesign.pack(fill='both')

    Liveview = LV(master=app)
    Liveview.place(x=330, y=10)

    app.mainloop()