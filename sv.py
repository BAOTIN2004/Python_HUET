class SinhVien():
    def __init__(self,fullname,yob,score):
        self.hoten=fullname
        self.namsinh=yob
        self.dtb=score
    def __str__(self):
        message='[Ho ten: '+self.hoten+'; Nam sinh: '+str(self.namsinh)+'; Diem trung binh: '+str(self.dtb)+']'
        return message
    def __gt__(self,obj):
        return (self.dtb>obj.dtb)
    def __ge__(self,obj):
        return(self.dtb>=obj.dtb)
    def __lt__(self,obj):
        return(self.dtb<obj.dtb)    
    def __le__(self,obj):
        return(self.dtb<=obj.dtb)
    def __eq__(self,obj):
        return(self.dtb==obj.dtb)

# def main():
#     sv1=SinhVien('Pham Phuoc Bao Tin',2004,10)
    
#     print(sv1)
# if __name__=="__main__":
#     main()



