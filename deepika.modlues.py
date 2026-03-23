#modlues:

#Random
import random as r
print(r.random())
print(r.randint(1,100))
print(r.randrange(1,100,1))

#sys
import sys as s
a=dir (s)
print(a)
print(s.path)
print("--------")
print(s.version)

while True:
    print("1.login\n2.exit")
c=int(input("Enter choice(1/2)"))
if c==1:
    print("logged in")
elif c==2:
    print("Before exit")
s.exit(0)
print("after exit")


#SOCKET

import socket
host=socket.gethostname
print(host)

#pywhatkit

import pywhatkit
product=input("enter search data:")
pywhatkit.search("http://m.media.amazon.com/images/./61rf//vealt")

#calendar
import calendar as c
print(c.month(2023,8))
print(c.isleap(2023))
print(c.calendar(2026))

#Time
import time
print(time.ctime())
print("hi")      
time.sleep(2)
print("bye")

l=["VIVO Book","HP","Dell","Asus","Acer","MI"]
for i in l:
 time.sleep(2)
 print(i)

 import datetime as d
 print(d.datetime.now())


