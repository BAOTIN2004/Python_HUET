import os
fd=os.getcwd()
print('thu muc hien tai',fd)
os.chdir('E:\data')
print('Thu muc sau khi thay doi',os.getcwd())
os.makedirs("E:\NNLT")
print(os.listdir("E:\My documents"))
print(os.path.exists("E:\My documents\BAI12.xlsx"))
os.rmdir("E:\My documents\THUMUCCANXOA") # Xoa thu muc
os.remove("E:\My documents\bai11.xlsx") # xoa file

