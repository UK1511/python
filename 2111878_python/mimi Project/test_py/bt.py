import os
import csv
from unidecode import unidecode

def split_name(name):
    name_parts = name.lower().split()
    return unidecode(name_parts[-1])+''.join(part[0].upper() for part in name_parts[:-1])

def createUsers(name,passwd,ou, domain):
    account = split_name(name)
    command = f'dsadd user "CN={account},OU={ou},OU=QTM_CTY,dc={domain},dc=com" -pwd "{passwd}"'
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
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                 if len(row) >= 3:
                      user = {
                           'user' : row[0],
                           'ou' : row[1],
                           'passwd' : row[2]
                      }
                      user_data.append(user)
            return user_data
    except Exception as e:
        print(e)
        return None

def RemoteDesktop(account):
    command = f'net localgroup "Remote Desktop Users "{account} /add' 
    os.system(command)

def Copyfile(source_path, des_path):
    try:
        os.system(f'copy "{source_path}" "{des_path}"')
        print(f'Đã sao chép "{source_path}" to "{des_path}"')  
    except Exception as e:
        print(e)
        return None

def deploy_foxit(installed_path):
    try: 
        os.system(f'{installed_path} /S')
        print('foxit Reader đã được cài đặt thành công!')
    except Exception as e:
        print(e)



domain = 'dc=quocvm,dc=com'

while True:
    print('''
        Nhấn 0 để tắt 
        Nhấn 1 để tạo OU cha (QTM_CTY) (BẮT BUỘC!!!)
        Nhấp 2 để tạo user
        nhấp 3 để cập nhật mật khẩu 
        nhấn 4 để tạo profile và homedir cho một user nhập từ bàn phím
        Nhấn 5 để xóa một user 
        Nhấn 6 để cài dịch vụ web và telnet cho server
        Nhấn 7 để đọc file csv
        Nhấn 8 để tạo OU từ file csv
        Nhấn 9 để tạo tất cả user từ file csv
        Nhấn 10 để tạo profile cho tất cả user tron file csv
        Nhấn 11 để đổi tất cả mật khẩu của các user đã tạo thành QTM2023@
        Nhấn 12 để lập cho user chỉ định quyền remote desktop
        Nhấn 13 để copy file txt từ thư mục nguồn sang thư mục đích
        Nhấn 14 để Deploy phần mềm Foxi Reader(lưu ý cần tải file FoxitReaderInstaller.exe trước!!!)
        Nhấn 15 để cài đặt website''')
    chon = int(input('chọn 1 mục: '))
    if chon == 0: 
        exit
    if chon == 1: 
        name = str(input('Nhập tên: '))
        passwd = str(input('Nhập password: '))
        ou = str(input('Nhập OU: '))
        createUsers(name, passwd, ou, domain)
        break
    





