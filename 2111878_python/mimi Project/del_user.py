import tkinter as tk 
import os

def delUser(account, ou, domain):
    command = f'dsrm user "CN={account}",OU={ou},OU=QTM_CTY,{domain}"'
    print(command)
    os.system(command)

def del_user_form():
    del_user_form = tk.Tk()
    del_user_form.title("Delete user")
    del_user_form.geometry('300x200')
    del_user_form.configure(background="#336699")
    
    def executed():
        account = user_entry.get()
        ou = ou_entry.get()
        domain = domain_entry.get()
        try: 
            if account and ou and domain:
                delUser(account, ou, domain)
                result_label.configure(text=f'xóa thành công {account}')
        except OSError:
            result_label.configure(text='lỗi nhập')
    user_label = tk.Label(del_user_form, text="Nhập username")
    user_label.place(x=10, y=20)
    user_entry = tk.Entry(del_user_form)
    user_entry.place(x=135, y=20)
    
    ou_label = tk.Label(del_user_form, text= 'Nhập ou')
    ou_label.place(x=10, y=50)
    ou_entry = tk.Entry(del_user_form)
    ou_entry.place(x=135, y=50)
    
    domain_label = tk.Label(del_user_form, text="Nhập tên miền:")
    domain_label.place(x= 10, y= 80)
    domain_entry = tk.Entry(del_user_form)
    domain_entry.insert(tk.END,'.com')
    domain_entry.place(x= 135, y= 80)
    
    create = tk.Button(del_user_form, text= "Tạo user", command = executed)
    create.place(x=121, y= 150)

    result_label = tk.Label(del_user_form, text="", background="#336699")
    result_label.place(x=80, y= 180)
    
    del_user_form.mainloop()
    
    
if __name__ == "__main__":
    del_user_form()