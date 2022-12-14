from student import SinhVien
import pickle
import  os

def luu(path:str,filename:str,objs:list[SinhVien]):
    try:
        with open(os.path.join(path,filename),'ab') as f:
             return pickle.dump(objs,f)
        print('Da ghi sinh vien')
    except Exception as e: print('Da xay ra loi')

def doc(path,filename) -> list[SinhVien]:
    try:
        with open(os.path.join(path,filename),'rb') as f:
             return pickle.load(f)
    except Exception: return  None

def in_ds_sv(content: list[SinhVien]):
    for item in content:
        print(item)
        
def main():
    path = 'C:\\k3'
    filename = 'dulieusv.txt'
    sv1=SinhVien('Trinh Quoc Dan',2004,9)
    sv2= SinhVien('Pham Phuoc Bao Tin', 2004, 10)
    sv3=SinhVien('Tran Tung Duong',2010,2)
    sv=[sv1,sv2,sv3]
    a=luu(path,filename,sv)
    b=doc(path,filename)
    in_ds_sv(doc(path,filename))

if __name__=="__main__":
    main()



