from src.scripts.popups import *

def open_popup(project):
    popup = ErrorPopup(error='This Project is not compatible!', syn=project, full_error=f"Project '{project}' isn't compatible with this version of CTkThemer")