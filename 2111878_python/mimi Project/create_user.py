
import tkinter as tk
import os
import subprocess
from unidecode import unidecode
def split_name(name):
    name_parts = name.lower().split()
    return unidecode(name_parts[-1])+''.join(part[0].upper() for part in name_parts[:-1])

def user_exists(account, ou, domain):
    command = f'dsquery user -name {account} -OU {ou},dc={domain},dc=com'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return process.returncode == 0

def createuser_form():
    
    def createUsers(name,passwd,ou, domain):
        account = split_name(name)
        command = f'dsadd user "CN={account},OU={ou},dc={domain},dc=com" -pwd "{passwd}"'
        if user_exists(account, ou, domain):
            result_label.config(text=f"Người dùng {account} đã tồn tại!")
        else:
            try: 
                process = subprocess.Popen(command,stdout = subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
                output, error = process.communicate()
                if process.returncode == 0:
                    result_label.config(text=f'người dùng {account} đã được tạo!')
                else:
                    result_label.config(text= f'lỗi: {error.decode("utf-8")}')
            except Exception as e:
                result_label.config(text = f'lỗi: {str(e)}')
    def executed():
        user_name = name_entry.get()
        new_name = split_name(user_name)
        passwd = passwd_entry.get()
        ou = ou_entry.get()
        domain_name =domain_entry.get().split('.')
        if user_name and passwd and ou and domain_name:
            createUsers(user_name, passwd, ou, domain_name[0])
        else:
            result_label.config(text="Hãy điền đầy đủ thông tin!")
        
        
    create_user_form =tk.Tk()
    create_user_form.title("Create User")
    create_user_form.geometry("300x200")
    create_user_form.configure(background="#66CDAA")
    name_label= tk.Label(create_user_form, text = "Nhập tên: ")
    name_label.place(x=10, y= 20)
    name_entry = tk.Entry(create_user_form)
    name_entry.place(x=135, y= 20)


    passwd_label = tk.Label(create_user_form, text="Nhập mật khẩu: ")
    passwd_label.place(x= 10, y= 50)
    passwd_entry = tk.Entry(create_user_form)
    passwd_entry.place(x=135, y=50)

    ou_label = tk.Label(create_user_form, text="Nhập OU:")
    ou_label.place(x=10, y= 80)
    ou_entry = tk.Entry(create_user_form)
    ou_entry.place(x=135, y=80)

    domain_label = tk.Label(create_user_form, text="Nhập tên miền:")
    domain_label.place(x= 10, y= 110)
    domain_entry = tk.Entry(create_user_form)
    domain_entry.insert(tk.END,'.com')
    domain_entry.place(x= 135, y= 110)

    create = tk.Button(create_user_form, text= "Tạo user", command = executed)
    create.place(x=121, y= 150)

    result_label = tk.Label(create_user_form, text="", background="#66CDAA")
    result_label.place(x=10, y= 180)

    create_user_form.mainloop()

if __name__ == "__main__":
    createuser_form()


