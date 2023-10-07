import tkinter as tk
import os
def changePasswd(account, passwd, ou, domain):
    command = f'dsmod user "CN={account},ou={ou},OU=QTM_CTY,{domain}" -pwd "{passwd}"'
    print(command)
    os.system(command)

def change_passwd_form():
    window = tk.Tk()
    window.configure(background="#99CC66")
    window.geometry("500x400")
    window.title('Change password')
    
    def executed():
        account = user_entry.get()
        passwd = passwd_entry.get()
        ou = ou_entry.get()
        domain_NU = domain_entry.get().split('.')
        domain = f'dc={domain_NU[0]},dc=com'
        command = f'dsmod user "CN={account},ou={ou},OU=QTM_CTY,{domain}" -pwd "{passwd}"'
        try: 
            if account and passwd and ou and domain:
                changePasswd(account, passwd, ou, domain)
                result_label.config(text=command)
        except OSError:
            result_label.config(text='Lỗi nhập')
            
            
    user_label = tk.Label(window, text ="Nhập tài khoản user:")
    user_label.place(x=10, y=20)
    user_entry = tk.Entry(window)
    user_entry.place(x=132, y=20)

    passwd_label = tk.Label(window, text="nhập mật khẩu mới:")
    passwd_label.place(x=10, y=50)
    passwd_entry = tk.Entry(window, show= "*")
    passwd_entry.place(x=132, y=50)

    ou_label =tk.Label(window, text="Nhập ou:")
    ou_label.place(x=10, y=80)
    ou_entry = tk.Entry(window)
    ou_entry.place(x=132, y=80)

    domain_label = tk.Label(window, text="Nhập domain:")
    domain_label.place(x=10, y=110)
    domain_entry = tk.Entry()
    domain_entry.insert(tk.END,'.com')
    domain_entry.place(x=132, y=110)
    
    create = tk.Button(window, text= "Change", command = executed)
    create.place(x=121, y= 150)

    result_label = tk.Label(window, text="", background="#99CC66")
    result_label.place(x=10, y= 180)
    
    window.mainloop()

if __name__ == "__main__":
    change_passwd_form()