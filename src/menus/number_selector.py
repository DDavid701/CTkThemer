from customtkinter import *

callback = None

def number_selector(start, max):
    num = None

    def on_close():
        global num
        global callback
        num = 0
        callback = 0
        selector.quit()
        selector.destroy()

    def update_number(_num):
        numb = int(_num)
        number.set(f"{str(numb)}")

    def return_number():
        selector.quit()
        selector.destroy()

    selector = CTk(fg_color='gray10')
    selector.title('Selector')
    selector._set_appearance_mode('Dark')
    selector.protocol('WM_DELETE_WINDOW', on_close)
    selector.geometry('400x160')
    selector.resizable(False, False)

    number = StringVar(selector)
    number.set(start)

    number_slider = CTkSlider(selector, from_=0, to=int(max), number_of_steps=int(max), width=250, height=18)
    number_slider.place(x=70, y=30)
    number_slider.set(int(start))
    number_slider.configure(command=update_number)

    number_entry = CTkEntry(selector, textvariable=number, width=28, height=16, corner_radius=0, state='disabled')
    number_entry.place(x=325, y=27)

    done_button = CTkButton(selector, text='OK', command=return_number, corner_radius=0)
    done_button.place(x=130, y=70)

    selector.mainloop()
    callback = number.get()
    print(callback)
    return callback