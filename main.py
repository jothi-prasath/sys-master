from tkinter import *
import temp_delete1, temp_delete2, dns_cleaner, app
import webbrowser
import emoji

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


window = Tk()
window.title("Sys Master")
window.geometry('500x210')
menubar = Menu(window)

def callback(url):
    webbrowser.open_new(url)

def open_popup():
   top= Toplevel(window)
   top.geometry("280x100")
   top.title("About")
   heart_emoji = emoji.emojize(":red_heart:")
   lbl = Label(top, text= "Made by Jothi Prasath", font=("Segoe UI", 15))
   lbl.grid(column=0, row=0)
   lbl = Label(top, text= heart_emoji, font=("Segoe UI", 15,),fg='red')
   lbl.grid(column=1, row=0)
   link1 = Label(top, text="Github", fg="blue", cursor="hand2")
   link1.grid(column=0, row=1)
   link1.bind("<Button-1>", lambda e: callback("https://github.com/jothi-prasath/"))

menubar.add_command(label="About", command=open_popup)


lbl = Label(window, text="Temp cleaner",font=('Arial',12))
lbl.grid(column=0, row=0)
btn = Button(window, text="Run", width=8, command=temp_delete1.run)
btn.grid(column=1, row=0)
lbl = Label(window, text="%Temp% cleaner",font=('Arial',12))
lbl.grid(column=0, row=1)
btn = Button(window, text="Run", width=8, command=temp_delete2.run)
btn.grid(column=1, row=1)
lbl = Label(window, text="DNS cleaner",font=('Arial',12))
lbl.grid(column=0, row=2)
btn = Button(window, text="Run", width=8, command=dns_cleaner.run)
btn.grid(column=1, row=2)
lbl = Label(window, text="Disable update",font=('Arial',12))
lbl.grid(column=0, row=3)
btn = Button(window, text="Run", width=8, command=app.update)
btn.grid(column=1, row=3)
lbl = Label(window, text="memory clean",font=('Arial',12))
lbl.grid(column=0, row=4)
btn = Button(window, text="Run", width=8, command=app.mem)
btn.grid(column=1, row=4)
lbl = Label(window, text="Discord",justify=LEFT ,font=('Arial',12))
lbl.grid(column=3, row=0)
btn = Button(window, text="Run", width=8, command=app.discord)
btn.grid(column=4, row=0)
lbl = Label(window, text="Discord with admin",font=('Arial',12))
lbl.grid(column=3, row=1)
btn = Button(window, text="Run", width=8, command=app.discord_admin)
btn.grid(column=4, row=1)
lbl = Label(window, text="Volume master",font=('Arial',12))
lbl.grid(column=3, row=2)
btn = Button(window, text="Run", width=8, command=app.vol_mix)
btn.grid(column=4, row=2)
lbl = Label(window, text="Task Manager",font=('Arial',12))
lbl.grid(column=3, row=3)
btn = Button(window, text="Run", width=8, command=app.task)
btn.grid(column=4, row=3)

window.config(menu=menubar)
window.mainloop()