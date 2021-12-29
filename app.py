import os
import subprocess
import getpass

user_name = getpass.getuser()

shortcut_dir = "c:\\Users\\"+user_name+"\\AppData\\Roaming\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk"
discord_dir = "C:\\Users\\"+user_name+"\\AppData\\Local\\Discord\\Update.exe"
steam_dir = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Steam\\Steam.lnk"
epic_dir = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Epic Games Launcher.lnk"
ubi_dir = "C:\\Users\\"+user_name+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Ubisoft\\Ubisoft Connect\\Ubisoft Connect.lnk"


def discord_admin():
    subprocess.Popen('taskkill /F /IM discord.exe', shell=True, stdin=subprocess.DEVNULL, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
    subprocess.Popen(shortcut_dir, shell=True, stdin=subprocess.DEVNULL, stdout = subprocess.PIPE, stderr= subprocess.PIPE)

def discord():
    subprocess.Popen('taskkill /F /IM discord.exe', shell=True, stdin=subprocess.DEVNULL, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
    subprocess.Popen('"%s" --processStart Discord.exe'% discord_dir, shell=True, stdin=subprocess.DEVNULL, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
    
def vol_mix():
    subprocess.Popen('C:\Windows\System32\SndVol.exe', shell=True, stdin=subprocess.DEVNULL, stdout = subprocess.PIPE, stderr= subprocess.PIPE)

def task():
    subprocess.Popen('taskmgr', shell=True, stdin=subprocess.DEVNULL, stdout = subprocess.PIPE, stderr= subprocess.PIPE)

def update():
    subprocess.Popen('net stop wuauserv', shell=True, stdin=subprocess.DEVNULL, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
    subprocess.Popen('net stop bits', shell=True, stdin=subprocess.DEVNULL, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
    subprocess.Popen('net stop dosvc', shell=True, stdin=subprocess.DEVNULL, stdout = subprocess.PIPE, stderr= subprocess.PIPE)

def mem():
    subprocess.Popen('EmptyStandbyList.exe', shell=True, stdin=subprocess.DEVNULL, stdout = subprocess.PIPE, stderr= subprocess.PIPE)