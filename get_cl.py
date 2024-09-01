import requests
from ctktu.updater import window
from os import getenv
from dotenv import load_dotenv

from src.ctkthemer.elements import changelog_display

load_dotenv('src/app.env')

version = getenv('VERSION')
change_url = 'https://pastebin.com/raw/L6ZAHfG5' # Changelog paste
ver_url    = 'https://pastebin.com/raw/VFiTkUh7' # Version paste

def get_changes(master):
    req = requests.get(change_url)

    cont = req.text
    code = req.status_code
    addr = req.url
    time = req.elapsed

    parts = cont.split('^')

    for part in parts:
        part = part.replace('[', '')
        part = part.replace(']', '')
        print(part)

        Display = changelog_display(master)
        Display.pack(pady=2)

        part_parts = part.splitlines()
        count = 0
        for part_part in part_parts:
            if part_part == "":
                print("passing")
                pass
            else:
                if count == 0:
                    entry = Display.version_entry(Display, part_part)
                    entry.pack()
                else:
                    entry = Display.entry(Display, part_part)
                    entry.pack()
                count += 1


def get_ver():
    req  = requests.get(ver_url)

    cont = req.text
    code = req.status_code
    addr = req.url
    time = req.elapsed
    print(f"ADDRESS> {addr}\n"
          f"STATUS-> {code}\n"
          f"CONTENT> {cont}\n"
          f"ELAPSED> {time}\n")

    if version == cont:
        pass
    else:
        print(f"You're version is outdated! [{cont}] is out! Your on {version}")
        print('Now updating...')
        window(cont)