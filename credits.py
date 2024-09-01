from customtkinter import *
from PIL import Image


class Credits(CTkScrollableFrame):
    class category(CTkFrame):
        def __init__(self, master, name):
            super(Credits.category, self).__init__(master=master, width=300, height=30, fg_color='gray8', corner_radius=0)

            self.label = CTkLabel(self, text=name, font=CTkFont(family='Roboto', size=16, weight='bold'))
            self.label._canvas.configure(height=20)
            self.label.grid()

    class entry(CTkFrame):
        def __init__(self, master, name):
            super(Credits.entry, self).__init__(master=master, width=300, height=30, fg_color='gray8', corner_radius=0)

            self.label = CTkLabel(self, text=name, font=CTkFont(family='Roboto', size=12, weight='normal'))
            self.label._canvas.configure(height=16)
            self.label.grid()

    class placeholder(CTkFrame):
        def __init__(self, master):
            super(Credits.placeholder, self).__init__(master=master, width=300, height=30, fg_color='gray8', corner_radius=0)

    def __init__(self, master):
        super(Credits, self).__init__(master=master, fg_color='gray8', width=350, height=220, corner_radius=0)
        self.bind('<Button-4>', self.scroll_up)
        self.bind('<Button-5>', self.scroll_down)
        self._scrollbar.bind('<Button-4>', self.scroll_up)
        self._scrollbar.bind('<Button-5>', self.scroll_down)


        # Dev (Category)
        dev = self.category(self, name="Developer")
        dev.pack(pady=3)
        dev.bind('<Button-4>', self.scroll_up)
        dev.bind('<Button-5>', self.scroll_down)

        _1 = self.entry(self, name="DDavid701")
        _1.pack()
        _1.bind('<Button-4>', self.scroll_up)
        _1.bind('<Button-5>', self.scroll_down)

        placeholder = self.placeholder(self)
        placeholder.pack()
        placeholder.bind('<Button-4>', self.scroll_up)
        placeholder.bind('<Button-5>', self.scroll_down)

        # UI (Category)
        ui = self.category(self, name="User Interface")
        ui.pack(pady=3)
        ui.bind('<Button-4>', self.scroll_up)
        ui.bind('<Button-5>', self.scroll_down)

        # Ui Entries
        _1 = self.entry(self, name="DDavid701")
        _1.bind('<Button-4>', self.scroll_up)
        _1.bind('<Button-5>', self.scroll_down)
        _1.pack()

        placeholder = self.placeholder(self)
        placeholder.pack()
        placeholder.bind('<Button-4>', self.scroll_up)
        placeholder.bind('<Button-5>', self.scroll_down)

        # Thanks (Category)
        thx = self.category(self, name="Thanks to")
        thx.pack(pady=3)
        thx.bind('<Button-4>', self.scroll_up)
        thx.bind('<Button-5>', self.scroll_down)

        # Thanks Entries
        _1 = self.entry(self, name="Font Awesome for the Icons")
        _1.bind('<Button-4>', self.scroll_up)
        _1.bind('<Button-5>', self.scroll_down)
        _1.pack()

    def scroll_up(self, none):
        cur = self._parent_canvas.yview()
        print(f"cur_up: {cur}")
        self._parent_canvas.yview_moveto(cur[0] + 0.1)

    def scroll_down(self, none):
        cur = self._parent_canvas.yview()
        print(f"cur_down: {cur}")
        self._parent_canvas.yview_moveto(cur[0] - 0.1)


def open_credits():
    win = CTkToplevel()
    win.geometry("400x220")
    win.attributes('-type', 'dock')
    win.title('CTkThemer - Credits')

    def close_window():
        win.destroy()

    win.protocol('WM_DELETE_WINDOW', close_window)

    sidebar = CTkFrame(win, width=37, height=220, corner_radius=0, fg_color='gray6')
    sidebar.place(x=0, y=0)

    close_button = CTkButton(sidebar, text='', image=CTkImage(dark_image=Image.open('src/icons/titlebar/close.png'), size=(14, 14)), width=37, height=37, fg_color='gray6', hover_color='gray8', corner_radius=0, command=close_window)
    close_button.place(x=0, y=0)

    credits_frame = Credits(master=win)
    credits_frame.place(x=35, y=0)

    win.mainloop()

if __name__ == '__main__':
    open_credits()