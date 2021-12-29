import os
import subprocess
def run():
    del_dir = 'c:\\windows\\temp'
    pObj = subprocess.Popen('rmdir /S /Q %s' % del_dir, shell=True, stdin=subprocess.DEVNULL, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
    # recreate the deleted parent dir in case it get deleted
    rTup = pObj.communicate()
    rCod = pObj.returncode
    print(del_dir)
    if rCod == 0:
        print ('Success: Cleaned Windows Temp Folder')
    else:
        print ('Fail: Unable to Clean Windows Temp Folder')