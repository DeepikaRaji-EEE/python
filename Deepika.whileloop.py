#BUZZ NUMBER
#n=1007
if 1007%7==0:
 print("Buzz number")
else:
     print("not Buzz number")


#fibonacci series:
#0 1 1 2 3 5 8 13 21 34 55....n
#n=50
a=0
b=1
print(a,end=" ")
print(b,end=" ")


n=int(input("Enter a number:"))
if n==0:
      print(1)
else:
    c=0
    while n>0:
        n=n//10
        c+=1
        print(c)


#***
#***
#***

i=0
while i<3:
    j=0
    while j<3:
        print("*",end=" ")
        j+=1
    print()
    i+=1 



#1 2 3 4 5
for i in range(1,6,1):
    for j in range(1,i+1,1):
        print("*",end=" ")
        print()

 #1 2 3 4 5
for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(chr(96+j),end=" ")
        print()


#1 2 3 4 5
for i in range(1,6,1):
    for j in range(1,6,1):
        if i==1 or i==5 or j==1 or j==5:
         print("*",end=" ")
        print()
else:
    print("*",end=" ")
    print()


#1 2 3 4 5
for i in range(1,6,1):
    for j in range(1,6,1):
        if i==j or i+j==6:
         print("*",end=" ")
else:
    print(" ",end=" ")
print()
