from src.scripts.popups import *

def open_popup(format):
    popup = ErrorPopup(error='This file format is not supported!', syn=f'.{format}', full_error=f"The file format '.{format}' is not supported by CTkThemer!'")