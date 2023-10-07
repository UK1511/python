from tkinter import *
from PIL import Image, ImageTk
from tkinter import Tk, Label, BOTH, RIGHT, RAISED
from tkinter.ttk import Frame, Style, Button
from tkinter import messagebox


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Thêm button")
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

        # quit thì thoát chương trình, self.destroy = this.close()
        closeButton = Button(self, text="Close", command=self.quit)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT)

        Style().configure("TFrame", bg="#333")

        bard = Image.open("Layout/img/Huy.jpg")
        bard = bard.resize((100, 100), Image.ANTIALIAS)
        bardejov = ImageTk.PhotoImage(bard)
        lable1 = Label(self, image=bardejov)
        lable1.image = bardejov
        lable1.place(x=20, y=20)


def on_close():
    thoat = messagebox.askyesno(
        "Thông báo", "Bạn có thực sự muốn thoát?", icon=messagebox.QUESTION)
    if thoat:
        root.destroy()


root = Tk()
root.geometry("300x200+300+300")
app = Example(root)
root.protocol('WM_DELETE_WINDOW', on_close)  # Đóng khi nhấn dấu x (close)
root.mainloop()
