import tkinter as tk
import os
def createOU(ou,domain):
    command1 = f'dsadd ou "OU={ou},dc={domain},dc=com"'
    print(command1)
    os.system(command1)

def executed():
    ou = ou_entry.get()
    domain_name = domain_entry.get()
    
    try:
        if ou and domain_name:
            createOU(ou,domain_name)
            result_label.config(text=f"đã tạo ou {ou} thành công!!!")
        else:
            result_label.config(text="Yêu cầu nhập lại thông tin!!!")
    except OSError:
        result_label.config(text="Lỗi nhập domain hoặc OU")
window = tk.Tk()
window.title("create User")
window.geometry("300x200")
window.configure(background="#40E0D0")

ou_label = tk.Label(window, text="Nhập OU:")
ou_label.place(x=10, y= 20)
ou_entry = tk.Entry(window)
ou_entry.place(x=110, y=20)

domain_label = tk.Label(window, text="Nhập tên miền:")
domain_label.place(x= 10, y= 50)
domain_entry = tk.Entry(window)
domain_entry.place(x= 110, y= 50)

create = tk.Button(window, text= "Tạo user", command = executed)
create.place(x=121, y= 80)

result_label = tk.Label(window, text="", background="#66CDAA")
result_label.place(x=80, y= 110)
window.mainloop()


