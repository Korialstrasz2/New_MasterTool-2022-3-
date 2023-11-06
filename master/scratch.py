import hashlib
import os
import shutil
from pathlib import Path
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

filesnew = []
filesold = []

def list_files(startpath,New = False):
    if New:
        for path in Path(startpath).rglob('*'):
            filesnew.append(path)

    else:
        for path in Path(startpath).rglob('*'):
            filesold.append(path)
            # print(path)
# You can replace 'your_directory' with your actual directory path

root = Tk()
root.withdraw()
file_path_n = askdirectory(title = "Seleziona la cartella con i file NUOVI, AGGIORNATI")
list_files(file_path_n, True)

file_path_o = askdirectory(title = "Seleziona la cartella con i file VECCHI, DA SOSTITUIRE")
list_files(file_path_o)
file_path_o = file_path_o.replace("\\","/")
file_path_n = file_path_n.replace("\\","/")


def get_file_hash_1(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def compare_and_replace_files(path1, path2):
        if os.path.isfile(path2):
            if get_file_hash_1(path1) != get_file_hash_1(path2) or path1.endswith(".exe"):
                print("SOVRASCRITTO " + path2)
                shutil.copy2(path1, path2)

filesnew_trimmed = []
filesold_trimmed = []

for new in filesnew:
    filesnew_trimmed.append(str(new).replace("WindowsPath('","").replace("')","").replace("\\","/"))
for old in filesold:
    filesold_trimmed.append(str(old).replace("WindowsPath('","").replace("')","").replace("\\","/"))

for newtrimmed in filesnew_trimmed:
    if "PG e Unici" not in newtrimmed:
        oldtrimmed = newtrimmed.replace(file_path_n,file_path_o)

        if oldtrimmed in filesold_trimmed:
            if oldtrimmed.split(file_path_o)[1] == newtrimmed.split(file_path_n)[1]:
                print(oldtrimmed)
                compare_and_replace_files(newtrimmed,oldtrimmed)
        else:
            print("SCRITTO " + newtrimmed)
            shutil.copy2(newtrimmed, oldtrimmed)