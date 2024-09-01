import threading
import io
import zipfile
import requests
import shutil
from file_structure import File_Structure
from customtkinter import *
from PIL import Image
logoimg = CTkImage(dark_image=Image.open('/home/davidd/PycharmProjects/CTkT/src/imgs/logo.png'), size=(64, 64))


def start_update(url, progress, win):
    response = requests.get(url, stream=True)

    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024
    wrote = 0

    if response.status_code == 200:
        buffer = io.BytesIO()

        if total_size == 0:
            progress.set(0.5)
            win.update_idletasks()

        for data in response.iter_content(block_size):
            wrote += len(data)
            buffer.write(data)
            if total_size > 0:
                progress.set(wrote / total_size)
                win.update_idletasks()

        with zipfile.ZipFile(buffer) as zip_ref:
            file_list = zip_ref.namelist()
            total_files = len(file_list)
            for i, file in enumerate(file_list):
                zip_ref.extract(file, "latest")
                progress.set((i + 1) / total_files)
                win.update_idletasks()

        os.mkdir('/home/davidd/PycharmProjects/CTkT/ctktu/files')

        shutil.move('/home/davidd/PycharmProjects/CTkT/src', '/home/davidd/PycharmProjects/CTkT/ctktu/files')
        shutil.move('/home/davidd/PycharmProjects/CTkT/credits.py', '/home/davidd/PycharmProjects/CTkT/ctktu/files')
        shutil.move('/home/davidd/PycharmProjects/CTkT/editor.py', '/home/davidd/PycharmProjects/CTkT/ctktu/files')
        shutil.move('/home/davidd/PycharmProjects/CTkT/get_cl.py', '/home/davidd/PycharmProjects/CTkT/ctktu/files')
        shutil.move('/home/davidd/PycharmProjects/CTkT/init.py', '/home/davidd/PycharmProjects/CTkT/ctktu/files')
        shutil.move('/home/davidd/PycharmProjects/CTkT/main.py', '/home/davidd/PycharmProjects/CTkT/ctktu/files')
        shutil.move('/home/davidd/PycharmProjects/CTkT/settings', '/home/davidd/PycharmProjects/CTkT/ctktu/files')

        shutil.move('/home/davidd/PycharmProjects/CTkT/ctktu/latest/CTkThemer-master/src', '/home/davidd/PycharmProjects/CTkT')
        shutil.move('/home/davidd/PycharmProjects/CTkT/ctktu/latest/CTkThemer-master/editor.py', '/home/davidd/PycharmProjects/CTkT')
        shutil.move('/home/davidd/PycharmProjects/CTkT/ctktu/latest/CTkThemer-master/init.py', '/home/davidd/PycharmProjects/CTkT')
        shutil.move('/home/davidd/PycharmProjects/CTkT/ctktu/latest/CTkThemer-master/main.py', '/home/davidd/PycharmProjects/CTkT')
        shutil.move('/home/davidd/PycharmProjects/CTkT/ctktu/latest/CTkThemer-master/get_cl.py', '/home/davidd/PycharmProjects/CTkT')
        shutil.move('/home/davidd/PycharmProjects/CTkT/ctktu/latest/CTkThemer-master/credits.py', '/home/davidd/PycharmProjects/CTkT')
        shutil.move('/home/davidd/PycharmProjects/CTkT/ctktu/latest/CTkThemer-master/settings', '/home/davidd/PycharmProjects/CTkT')

    else:
        print("Download failed")


def window():
    win = CTk()
    win.title('Updating CTkThemer...')
    win.attributes('-type', 'dock')
    win.geometry('400x300')

    logo = CTkLabel(win, text='', image=logoimg)
    logo.place(x=163, y=40)

    label = CTkLabel(win, text='Updating', anchor='center', justify='center', font=('System', 16, 'normal'))
    label.place(x=160, y=140)

    progressbar = CTkProgressBar(win, width=230, corner_radius=3)
    progressbar.set(0)
    progressbar.place(x=85, y=180)

    download_thread = threading.Thread(target=start_update, args=('https://github.com/DDavid701/CTkThemer/archive/refs/heads/master.zip', progressbar, win))
    download_thread.start()

    win.mainloop()

if __name__ == '__main__':
    window()