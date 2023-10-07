import os
import csv
def split_name(name):
    name_parts = name.lower().split()
    return name_parts[-1]+''.join(part[0].upper() for part in name_parts[:-1])

def createUsers(name,passwd,ou, domain):
    account = split_name(name)
    command = f'dsadd user "CN={account},OU={ou},OU=QTM_CTY,{domain}" -pwd "{passwd}"'
    print(command)
    os.system(command)

def changePasswd(account, passwd, ou, domain):
    command = f'dsmod user "CN={account},ou={ou},OU=QTM_CTY,{domain}" -pwd "{passwd}"'
    print(command)
    os.system(command)

def createOU(ou,domain):
    command1 = f'dsadd ou "OU={ou},OU=QTM_CTY,{domain}"'
    print(command1)
    os.system(command1)

def createProfileAndHomeDir(account, ou, domain):
    ip_server = input('Nhap ip server: ')
    nameFolder = input('Nhap ten thu muc muon tao: ')
    passwd = input('Nhap mat khau moi: ')
    cmdMkdir = f'mkdir C:\\{nameFolder}'
    os.system(cmdMkdir)
    cmdshare = f'net share {nameFolder}= C:\\{nameFolder}'
    print(cmdshare)
    os.system(cmdshare)
    path_profile = f'-profile \\{ip_server}\\profiles\\{account}'
    command2 = f'dsmod user "CN={account},OU={ou},OU=QTM_CTY,{domain}" {path_profile}'
    print(command2)
    os.system(command2)

def delUser(account, ou, domain):
    command = f'dsrm user "CN={account}",OU={ou},OU=QTM_CTY,{domain}"'
    print(command)
    os.system(command)

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

def read_csv_file(file_path):
    user_data = []
    try: 
        with open(file_path, newline='', encoding='utf8') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for column in csvreader:
                username = column[0]
                ou = column[1]
                passwd = column[2]
                user_data.append({'Ten nguoi dung ': username, 'OU': ou, 'Password': passwd})
            return user_data
    except Exception as e:
        print(e)
        return None

domain = 'dc=quocvm,dc=com'

while True:
    print('Tao ou cha(QTM_CTY): [0]')
    print('Tao user: [1]')
    print('Cap nhat mat khau: [2]')
    print('Tao profile va homedir cho user: [3]')
    print('Xoa user: [4]')
    print('Cai dat dich vu web: [5]')
    print('cat dat dich vu Telent: [6]')
    print('Doc file csv: [7]')


    chon = int(input('Chon 1 so: '))
    if chon == 0:
        ou = 'QTM_CTY'
        createOU(ou,domain)
    if chon == 1:
        name = input('Nhap ten nguoi dung: ')
        ou = input('Nhap ou cho user: ')
        passwd = input('Nhap mat khau cho user: ')
        createUsers(name,passwd,ou,domain)
    elif chon == 2:
        account = input('nhap ten user: ')
        passwd = input('Nhap mat khau moi: ')
        ou = input('Nhap ou cho user: ')
        changePasswd(account,passwd,ou,domain)
    elif chon == 3:
        account = input('Nhap user: ')
        ou = input('Nhap ou cho user: ')
        createProfileAndHomeDir(account, ou, domain)
    elif chon == 5:
        install_service_web()
    elif chon == 6:
        install_telnet_service()
    elif chon == 7:
        user_data =read_csv_file('DATASERVER.csv')
        if user_data:
            for user in user_data:
                print(user[0], user[1], user[2])
        input()
		
