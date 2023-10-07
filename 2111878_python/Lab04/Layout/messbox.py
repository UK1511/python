from tkinter import *
from tkinter import messagebox


def on_close():
    thoat = messagebox.askyesno(
        "Thông báo", "Bạn có thực sự muốn thoát?", icon=messagebox.QUESTION)
    if thoat:
        root.destroy()


root = Tk()
root.protocol('WM_DELETE_WINDOW', on_close)

root.mainloop()
