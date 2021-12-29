import os
import subprocess
def run():
    pObj = subprocess.Popen('ipconfig /flushdns', shell=True, stdin=subprocess.DEVNULL, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
    # recreate the deleted parent dir in case it get deleted
    rTup = pObj.communicate()
    rCod = pObj.returncode
    if rCod == 0:
        print ("Success: Cleaned DNS")
    else:
        print ("Fail: Unable to Clean DNS")