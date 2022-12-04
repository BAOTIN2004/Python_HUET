a=open('test.txt',mode="r+")
a=open('test.txt')
a=open('test.txt',mode="r+b")
a=open('test.txt',mode='r',encoding='utf8')
print(a.read())
a.close()
try:
    a=open('test.txt',mode="r")
finally: a.close()

with open('test.txt',mode="r") as f:
    f.read()

a=open('test.txt',"r+")
a.write("I'm Bao Tin\n I'm 18 \n Man")

a=open('test.txt',mode="r")
print(a.read())

b=open('BL.jpg',mode="r+b")
print(b.read())
