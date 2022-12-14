from student import SinhVien
import pickle
import  os
def luu(path:str,filename:str,obj:SinhVien):
    try:
        with open(os.path.join(path,filename),'wb') as f:
             return pickle.dump(obj,f)
        print('Da ghi sinh vien ')
    except Exception as e: print('Da xay ra loi')
def doc(path,filename) -> SinhVien:
    try:
        with open(os.path.join(path,filename),'rb') as f:
             return pickle.dump(f)
    except Exception: return  None
def main():
    path = 'C:\\k3'
    filename = 'dulieusv.dat'
    sv = SinhVien('Pham Phuoc Bao Tin', 2004, 10)
    a=luu(path,filename,sv)
    b=doc(path,filename)

if __name__=="__main__":
    main()



