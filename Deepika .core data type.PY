#fibonacci series

#0 1 1 2 3 5 8 13 21 34 55...n
n=50
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(0,n+1,1):
   s=a+b
   if s>=n:
     break
print(s,end=' ')
a,b=b,s


#list

a=[1,2,3,4,5]
print(a)
print(a[:])
print(a[0:3])
print(a[::-1])

a.append(5)
print(a)
a.extend([7,8])
print(a)
a.insert(0,0)
print(a)

a.remove(7)
print(a)

#del a
#print(a)

a.pop()
print(a)
a.pop(0)
print(a)

#input
x=[1,2,1,3,5,1,2,4,2,3,6,3]
#output
x=[1,2,3,5,4,6]

x=set(x)
print(list(x))

b=[]
for i in x:
    if i not in b:
        b.append(i)
        print(b)

x1=[1,2,3,5]
x1[3]=4
print(x1)

x=[1,2,1,3,5,1,2,4,2,3,6,3]
print(x.index(5))
x.sort()
print(x)
print(x.count(1))

print(min(x))
print(max(x))
print(sum(x))

x.reverse()
print(x)

y=[[0,0],[1,1]]
print(y[0])
print(y[1])
print(y[1][0])

#Tuble

a=(1,2,3,4,5)
b=(6,7,8)
c=a+b
print(c)
print(b*2)
print(list(c))
print(("python"))
print(c.index(7))
data=("Id1","priya","100")
data1=("Id2","vishnu","95")
i_d,name,mark=data
i_d,name,mark=data1
print(i_d,name,mark)


#set

s1={1,2,3,4}
s2={2,4,6,8}
s={3,1,4,2}
s.add(5)
print(5)
s.update([1,3,5,7])
print(5)
s.remove(7)
print(5)
s.discard(5)
print(5)
s.pop()
print(5)
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s1.difference(s2))
print(s2.difference(s1))
s1.intersection_update(s2)
print(s1)
s2.intersection_update(s1)
print(s2)


#Dictionary

d={"python":"60","java":"64","WD":"48"}
print(d["python"])
print(d.get("python"))
d.pop("python")
print(d)
print(d.keys())
print(d.values())
print(d.items())
d.update({"python":"60"})
print(d)
d["WD"]="50"
print(d)

#del dict
print(d)
for i in d:
    print(i,':',d[i])
