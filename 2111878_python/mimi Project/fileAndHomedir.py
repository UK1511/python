import tkinter as tk
import os

def createProfileAndHomeDir(account, ou, domain, ip_server, nameFolder):
    cmdMkdir = f'mkdir C:\\{nameFolder}'
    os.system(cmdMkdir)
    cmdshare = f'net share {nameFolder}= C:\\{nameFolder}'
    print(cmdshare)
    os.system(cmdshare)
    path_profile = f'-profile \\{ip_server}\\profiles\\{account}'
    command2 = f'dsmod user "CN={account},OU={ou},OU=QTM_CTY,dc={domain},dc=com" {path_profile}'
    print(command2)
    os.system(command2)


    
def Profile_And_Homedir_form():
    homedir_form =tk.Tk()
    homedir_form.title('Create Profile and Homedir')
    homedir_form.geometry('300x250')
    homedir_form.configure(background="#9966FF")

    def executed():
        account = user_entry.get()
        ou = ou_entry.get()
        domain = domain_entry.get().split('.')
        ip = ip_server_entry.get()
        nameFolder = nameFolder_entry.get()
        try:
            if account and ou and domain and ip and nameFolder:
                createProfileAndHomeDir(account,ou,domain[0],ip,nameFolder)
                result_label.config(text=f'Đã tạo thành công homedir và profile cho {account}')
        except OSError:
            result_label.config(text='Lỗi nhập')
    
    ip_server_label = tk.Label(homedir_form, text= "IP server")
    ip_server_label.place(x=10, y=20)
    ip_server_entry = tk.Entry(homedir_form)
    ip_server_entry.place(x=140, y=20)

    nameFolder_label = tk.Label(homedir_form, text='Tên thư mục muốn tạo')
    nameFolder_label.place(x=10, y=140)
    nameFolder_entry = tk.Entry(homedir_form)
    nameFolder_entry.place(x=140, y=140)
    
    user_label = tk.Label(homedir_form, text='Nhập vào user name')
    user_label.place(x=10, y=50)
    user_entry = tk.Entry(homedir_form)
    user_entry.place(x=140, y=50)
    
    ou_label = tk.Label(homedir_form, text="Nhập OU")
    ou_label.place(x=10, y= 80)
    ou_entry = tk.Entry(homedir_form)
    ou_entry.place(x=140, y=80)
    
    domain_label = tk.Label(homedir_form, text="Nhập tên miền")
    domain_label.place(x= 10, y= 110)
    domain_entry = tk.Entry(homedir_form, )
    domain_entry.insert(tk.END,'.com')
    domain_entry.place(x=140, y=110)

    create = tk.Button(homedir_form, text= "Create", command = executed)
    create.place(x=121, y= 170)

    result_label = tk.Label(homedir_form, text="", background="#9966FF")
    result_label.place(x=80, y= 210)
    
    homedir_form.mainloop()
    
    
    
if __name__ == "__main__":
    Profile_And_Homedir_form()