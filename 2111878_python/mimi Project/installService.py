import os
import tkinter as tk 


def install_service_web():
	cmd = "powershell.exe Install-windowsFeature - name Web-Server -IncludeManagermenttools"
	try:
		print(cmd)
		os.system(cmd)
	except Exception as e:
		print(e)

def install_telnet_service():
    command = 'dism /online /Enable-Feature /FeatureName:TelnetClient'
    try:
        print(command)
        os.system(command)
    except Exception as e:
        print(e)


def install_Service_form():
    install_Service_form = tk.Tk()
    install_Service_form.geometry('300x200')
    install_Service_form.title('Install Service for server')
    install_Service_form.configure(background= "#FF9999")
    
    web_button = tk.Button(install_Service_form, text= 'install web service',command=install_service_web)
    web_button.place(relx=0.5,rely=0.25,anchor=tk.CENTER)
    
    telnet_button = tk.Button(install_Service_form, text="install telnet service",command=install_telnet_service)
    telnet_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    result_label = tk.Label(install_Service_form, text="", background="#FF9999")
    result_label.place(x=80, y= 210)
    
    install_Service_form.mainloop()
    
    
if __name__ == "__main__":
    install_Service_form()