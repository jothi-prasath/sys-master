from tkinter import *
import temp_delete1, temp_delete2, dns_cleaner, app

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


window = Tk()
window.title("Sys Master")
window.geometry('600x250')

arrow = "--->"    

lbl = Label(window, text="Temp cleaner\t",font=('Arial',12)).grid(column=0, row=0)
btn = Button(window, text="Run", width=8, command=temp_delete1.run)
btn.grid(column=1, row=0)
lbl = Label(window, text="%Temp% cleaner\t",font=('Arial',12))
lbl.grid(column=0, row=1)
btn = Button(window, text="Run", width=8, command=temp_delete2.run)
btn.grid(column=1, row=1)
lbl = Label(window, text="DNS cleaner\t",font=('Arial',12))
lbl.grid(column=0, row=2)
btn = Button(window, text="Run", width=8, command=dns_cleaner.run)
btn.grid(column=1, row=2)
lbl = Label(window, text="Disable update\t",font=('Arial',12))
lbl.grid(column=0, row=3)
btn = Button(window, text="Run", width=8, command=app.update)
btn.grid(column=1, row=3)
lbl = Label(window, text="Task Manager\t",font=('Arial',12))
lbl.grid(column=0, row=4)
btn = Button(window, text="Run", width=8, command=app.task)
btn.grid(column=1, row=4)
lbl = Label(window, text="Discord\t",font=('Arial',12))
lbl.grid(column=3, row=0)
btn = Button(window, text="Run", width=8, command=app.discord)
btn.grid(column=4, row=0)
lbl = Label(window, text="Discord with admin\t",font=('Arial',12))
lbl.grid(column=3, row=1)
btn = Button(window, text="Run", width=8, command=app.discord_admin)
btn.grid(column=4, row=1)
lbl = Label(window, text="Volume master\t",font=('Arial',12))
lbl.grid(column=3, row=2)
btn = Button(window, text="Run", width=8, command=app.vol_mix)
btn.grid(column=4, row=2)
lbl = Label(window, text="Steam\t",font=('Arial',12))
lbl.grid(column=3, row=3)
btn = Button(window, text="Run", width=8, command=app.steam)
btn.grid(column=4, row=3)
lbl = Label(window, text="Epic games\t",font=('Arial',12))
lbl.grid(column=3, row=4)
btn = Button(window, text="Run", width=8, command=app.epic)
btn.grid(column=4, row=4)
lbl = Label(window, text="Uplay\t",font=('Arial',12))
lbl.grid(column=3, row=5)
btn = Button(window, text="Run", width=8, command=app.ubi)
btn.grid(column=4, row=5)


window.mainloop()