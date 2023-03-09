import os
import subprocess as sp

paths={
    'notepad':"C:\Program Files\Notepad++\notepad++.exe" ,
    'discord':"C:\Users\gurna\AppData\Local\Discord\app-1.0.9011\Discord.exe",
    'calculator':"C:\Windows\System32\calc.exe",
    'code editor':"C:\Users\gurna\AppData\Local\Programs\Microsoft VS Code\Code.exe"
}

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])

def open_editor():
    os.startfile(paths['code editor'])

def open_cmd():
    os.system('start cmd')

def open_calc():
    os.startfile(paths['calculator'])