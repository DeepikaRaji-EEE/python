#file handling

f=open(r"C:\Users\Livewire\Desktop\file1.txt","w")
f.write("welcome to python")
print("file is written")
f.close()


f=open("file2.txt","w")
f=open(r"C:\Users\Livewire\Desktop\file2.txt","w")
f.write("python")
print("file is written")
f.close()

f=open(r"C:\Users\Livewire\Desktop\file1.txt","a")
n="vishnu"
f.write(n)
f.close()

f=open(r"C:\Users\Livewire\Desktop\file1.txt","a")
n=input("enter a text:")
f.write(n)
print("file is written")
f.close()

print("name of the file:",f.name)
print("file is closer or not:",f.closed)
print("opening mode of the file:",f.mode)
      
f=open(r"C:\Users\Livewire\Desktop\file1.txt","a")
n=input("enter a text:")
f.write(n)
print("file is written")
f.close()

f=open("file1.txt","r")
print(f.read()) #Read All characters
print(f.read(20))#read only 20 characters
print(f.readline())#read the first line
print(f.readlines())#read the all line
print("current position of the cursor:",f.tell())
f.seek(0)#current fuction of the file cursor
f.close()

import os
print(os.getcwd())#get current directory
print(os.listdir())
os.rename('file3.txt","w")
print('ok')
os.remove('file name')
f.close()
