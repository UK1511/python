from datetime import datetime
class SinhVien:
    truong = 'Đại Học Đà Lạt'

    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime)-> None:
        self.__maSo = maSo
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh
    
    @property
    def maSo(self):
        return self.__maSo
    @property
    def hoTen(self):
        return self.__hoTen
    @property
    def ngaySinh(self):
        return self.__ngaySinh
    
    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self.__maSo = maso
    
    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso))== 7
    
    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi

    def __str__(self)-> str:
        return f'{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}'
    
    def xuat(self):
        print(f'{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}')
class DanhSachSV:
    def __init__(self)-> None:
        self.dssv = []
    
    def ThemSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)
    
    def Xuat(self):
        for sv in self.dssv:
            print(sv)

    def timSvTheoMssv(self, mssv: int):
        return [sv for sv in self.dssv if sv.maSo == mssv]

    def timVTSvTheoMssv(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == mssv:
                return i
        return -1

    def xoaSvTheoMssv(self, maSo: int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
    
    def timSvTheoTen(self, ten: str):
        ten = ten.lower() #chuyển sang chữ thường
        return [sv for sv in self.dssv if sv.hoTen.split(' ')[-1].lower() == ten]

    def timSVSinhTruocNgay(self, ngaySinh: datetime):
        return [sv for sv in self.dssv if sv.ngaySinh < ngaySinh]

   

sv1= SinhVien(2111878, 'Võ Mạnh Quốc', datetime.strptime('28/03/2003', '%d/%m/%Y'))
sv2= SinhVien(2115230, 'Lê Trần Anh Khôi', datetime.strptime('18/09/2002', '%d/%m/%Y'))
sv3= SinhVien(2114569, 'Nguyễn Viết Khoa', datetime.strptime('13/02/2002', '%d/%m/%Y'))
sv4= SinhVien(2110060, 'Nguyễn Thùy Linh', datetime.strptime('13/10/2003', '%d/%m/%Y'))
sv5= SinhVien(1234567, 'Nguyễn Tuấn Hưng', datetime.strptime('01/01/1946', '%d/%m/%Y'))
sv6= SinhVien(5567891, 'Nguyễn Ngọc Uyên Khoa', datetime.strptime('15/11/2002', '%d/%m/%Y'))
ds = DanhSachSV()
ds.ThemSinhVien(sv1)
ds.ThemSinhVien(sv2)
ds.ThemSinhVien(sv3)
ds.ThemSinhVien(sv4)
ds.ThemSinhVien(sv5)
ds.ThemSinhVien(sv6)
ds.Xuat()

a = int(input('Nhập vào mã số muốn tìm kiếm: '))
kq = ds.timSvTheoMssv(a)
if ds.timVTSvTheoMssv(a) != -1:
    print(f'Đã tìm thấy sinh viên có mã số {a}')
    for sv in kq:
        sv.xuat()
else: 
    print(f'không tìm thấy sinh viên có mã số {a}')

b = int(input('Nhập vào mã số muốn xóa: '))
kq = ds.xoaSvTheoMssv(b)
print(f'\nĐã xóa {b} khỏi danh sách\n')
ds.Xuat()

c = str(input('Nhập vào tên sinh viên cần tìm: '))
kq = ds.timSvTheoTen(c)
print(f'\nĐã tìm thấy sinh tên {c}')
for sv in kq:
    sv.xuat()

d = input('nhập vào ngày sinh cần tìm (dd/mm/yyy): ')
ngay = datetime.strptime(d, '%d/%m/%Y')
kqNgay = ds.timSVSinhTruocNgay(ngay)
print(f'\nĐã tìm thấy ngày sinh trước {d}: ')
for sv in kqNgay:
    sv.xuat()

