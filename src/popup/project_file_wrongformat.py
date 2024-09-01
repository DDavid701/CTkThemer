from src.scripts.popups import *

def open_popup(format):
    popup = ErrorPopup(error=f'This file format is not supported!\n(.{format})', full_error=f"The file format '.{format}' is not supported by CTkThemer!'")