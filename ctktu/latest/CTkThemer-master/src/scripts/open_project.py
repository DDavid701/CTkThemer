import dotctkt as ctkt
import editor

def open_project(file, data):
    cont = ctkt.get(f'/home/davidd/PycharmProjects/CTkThemer/ctkt_projects/{file}')
    print(cont)

    editor.launch(cont['Project Name'], data, file)