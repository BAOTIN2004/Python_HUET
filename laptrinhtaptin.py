def bai1():
    a='Hello everyone '
    b=open('infor.txt',mode="r+")
    b.write(a)
  
def bai2():
    a=open('infor.txt',mode="r")
    print(a.read())


def bai3():
    b="I'm Bao Tin"
    a=open('infor.txt',mode="a+")
    a.writelines(b)
    
def bai4():
    a=open('infor.txt',mode="r")
    print(a.read())

def bai5():
    import random
    x=[random.randint(-1000,1001) for i in range(0,1000)]
    a=open('so.txt',mode="w")
    k=0
    for i in range(100):
        for j in range(0,10):
            a.write(f"{x[k]}, ")
            k+=1
        a.write('\n')
    a=open('so.txt',mode="r")
    for sx in a.readlines():
        print(sx.replace(', ' ,"\t"))
        
def main():
    bai1() 
    bai2()
    bai3()   
    bai4()
    bai5()
if __name__=="__main__":
    main()
    





