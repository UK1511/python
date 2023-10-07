file = open("C:\Users\CICT\Desktop\lab02\data.txt", "r")
read = file.readlines()
listSv = []
sv = []
for i in read:
    if i not in listSv:
        listSv.append(i.strip())
print("\nDanh Sách Sinh Viên:\n",listSv)

listSv.sort(key=lambda x: x.split(',')[1])  
print("\nDanh sách sinh viên theo họ tên tăng dần:")
print('\n'.join(listSv)) 

listSv.sort(key=lambda x: x.split(',')[1],reverse=True) 
print("\nDanh sách sinh viên theo họ tên giảm dần:")
print('\n'.join(listSv))  
file.close()