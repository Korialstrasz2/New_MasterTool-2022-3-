import Moduli.SharedData as Shared

def seleziona_cartella_shared(*args):
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory(title='Select a folder')
    Shared.path_cartella_shared = folder_selected