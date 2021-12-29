from tkinter import *
import temp_delete1, temp_delete2, dns_cleaner, app

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


window = Tk()
window.title("Sys Master")
window.geometry('700x200')

arrow = "--->"    

lbl = Label(window, text="Temp cleaner\t"+arrow,font=('Arial',13))
lbl.grid(column=0, row=0)
btn = Button(window, text="Run", width=8, command=temp_delete1.run)
btn.grid(column=1, row=0)
lbl = Label(window, text="%Temp% cleaner\t"+arrow,font=('Arial',13))
lbl.grid(column=0, row=1)
btn = Button(window, text="Run", width=8, command=temp_delete2.run)
btn.grid(column=1, row=1)
lbl = Label(window, text="DNS cleaner\t"+arrow,font=('Arial',13))
lbl.grid(column=0, row=2)
btn = Button(window, text="Run", width=8, command=dns_cleaner.run)
btn.grid(column=1, row=2)
lbl = Label(window, text="Disable update\t"+arrow,font=('Arial',13))
lbl.grid(column=0, row=3)
btn = Button(window, text="Run", width=8, command=dns_cleaner.run)
btn.grid(column=1, row=3)
lbl = Label(window, text="Discord\t"+arrow,font=('Arial',13))
lbl.grid(column=3, row=0)
btn = Button(window, text="Run", width=8, command=app.discord)
btn.grid(column=4, row=0)
lbl = Label(window, text="Discord with admin\t"+arrow,font=('Arial',13))
lbl.grid(column=3, row=1)
btn = Button(window, text="Run", width=8, command=app.discord_admin)
btn.grid(column=4, row=1)


window.mainloop()