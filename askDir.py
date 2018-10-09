import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askdirectory

def askDir():
    '''function for ask user witch directory should be used by program'''
    win = tk.Tk()
    win.title()
    win.withdraw()
    directory = askdirectory()
    win.destroy()
    return(directory)
