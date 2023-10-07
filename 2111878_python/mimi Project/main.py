import create_user
import change_passwd
import create_ou
import tkinter as tk




def open_Mainform():
    root = tk.Tk()
    root.title("Main Form")
    root.geometry("500x250")
    def open_form():
        selection = int(entry_open_selection.get())
        if selection == 1:
            root.withdraw()
            create_user.createuser_form()
        elif selection == 2:
            return None

    label_open_selection = tk.Label(root, text= '''
nhập một số để mở chức năng
   1: tạo user
   2: tạo ou
   3: đổi mk
   4: xóa user''').place(x=10, y=20)
    entry_open_selection = tk.Entry(root)
    entry_open_selection.place(x=40, y=120)
    open_button = tk.Button(root, text="Mở Form Create User", command=open_form)
    open_button.place(x= 40, y=150) 
    root.mainloop()
    
if __name__ == "__main__":
    open_Mainform()