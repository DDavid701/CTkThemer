from customtkinter import *
from src.ctkthemer.elements import *
from src.ctkthemer.designs import *

WINDOW_TITLE  = 'CTkThemer'
WINDOW_RESIZE = False, False
WINDOW_WIDTH  = 1000
WINDOW_HEIGHT = 600

app = CTk(fg_color='gray10')
app.geometry(f"{str(WINDOW_WIDTH)}x{str(WINDOW_HEIGHT)}")
app.title(WINDOW_TITLE)
app.resizable(WINDOW_RESIZE[0], WINDOW_RESIZE[1])

Sidebar = CTkScrollableFrame(master=app, width=300, height=int(WINDOW_HEIGHT - 10), fg_color='gray14')

Sidebar._scrollbar.configure(corner_radius=1000, width=16, button_color='gray24', button_hover_color='gray20')

Sidebar.place(x=0, y=0)

CTkDesign = design_CTk(master=Sidebar)
CTkDesign.pack(fill='both')

test = CTkBox(master=app, text='Hallo')
test.place(x=400, y=50)

TEST = Number_Input(master=Sidebar)
TEST.pack()

app.mainloop()