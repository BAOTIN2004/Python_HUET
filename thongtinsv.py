from sv import SinhVien
def main():
    dssv=[SinhVien('Bao Tin',2004,100),
    SinhVien('Quoc Dan',2004,11),
    SinhVien('Tung Duong',2001,19)]
    sv=sorted(dssv)
    for item in sv:
        print(item)
if __name__=="__main__":
    main()