# 28 Oct 2023
#27-40

'''
27
l1=['A','B','C','D','E','F','G','H']
l2=[0,0,0,0,0,0,0,0]
d1=zip(l1,l2)
print (dict(d1))
-------------------------------------
# This one can not work
l = [1,2,3,4,5,6,7]
d = {}
d = set{}
for a in l:

    dict[a] = 0
print(d)
---------------------------------------
28
from tkinter import _flatten

a = [[1, 2], [3, 4]]
b = ((5,6),(7,8))

a = list(_flatten(a))
b = list(_flatten(b))
d1=zip(a,b)
print (dict(d1))
-----------------------------------
29
q = (1,2,3)
w = (4,5,6)
print(q+w)
-------------------------------------
30
x,y,z = (1,2,3)
print(x,y,z)
----------------------
31
a= ("c", "java", "python")
print(a.index('java'))
------------------------
32
a = (2,5,3,2,4)
b = 0
for i in a:
    if i == 2 :
        b = b + 1
print(b)
------------------------
33
a = ('Alice','Beth','Cecil')
for i in a:
    if i == 'Beth' :
        print('it is')
        break
    else:
        a = 0    #this one isn't have any meaning
-------------------------------------------------------
34
a = (3,5,6,7,8)
a = list(a)
a.insert(1,4)
print(a)
------------------------
35
a = {}
b = {1,2,3}
a = set(a)
a.update(b)
print(a)
------------------
36
a = {'x','y','z'}
a = set(a)
a.remove('x')
print(a)
a.add('w')
print(a)
a.clear()
print(a)
------------------------
37
a = {'a','d','b'}
b = {'d','k','h'}
c = {}
c = set(c)
for i in a:
    if i not in b:
        c.add(i)
    else:
        a = 0 #this one isn't have any meaning
print(c)
-------------------------------------
38
a = {'q','w'}
b = {'a','s'}
a.update(b)
print(a)
-----------------------
39
a = {'a','d','b'}
b = {'d','k','h'}
c = {}
c = set(c)
for i in a:
    if i in b:
        c.add(i)
    else:
        a = 0 #this one isn't have any meaning
print(c)
----------------------------------------------------------
40
a = {'a','d','b'}
b = {'d','k','h'}
c = {}
c = set(c)
for i in a:
    if i in b:
        c.add(i)
    else:
        c.add(i)
print(c)
'''
import numpy

# 4 Noverber 2023
# 44-56

'''
44
a = 'abCdEfg'
print(a.upper())
print(a.lower())

b = ''
for i in a:
    if 'a' <= i <= 'z' :
        b += str.upper(i)
    else:
        b += str.lower(i)
print(b)
-------------------------------
45
a = 'abCdEfg'
if 'A' <= a[0] <= 'Z' :
    print('the first str is big letter')
else:
    print('the first str is not big letter')

#/\#

i don't know why this can not work(past

i make it ohhhhhhh

it can work now

###

def why_you_can_not_work():
    if b != 0 and c == 0:
        print('it is all small letter')
    elif b == 0 and c != 0:
        print('it is all big letter')
    else:
        print('they are not all big or small letter')


a = 'abCdEfg'
q = 0
b = 0
c = 0
while q < len(a) :
    if 'a' <= a[q] <= 'z' :
        b = b + 1
    else:
        c = c + 1
    q += 1

print(why_you_can_not_work())

--------------------
46
import string
a = 'this is python'
print(a.capitalize())
print(string.capwords(a))
------------------------------
47
a = 'this is python'
a = a.split()

if a[0] == 'this' and a[-1] == 'python':
    print('aaa')
----------------------------
48
a = 'this is python'
a = a.split()

print(a.count('is'))
----------------------------
49
a = 'this is python'
a = a.split()
print(a.index('is'))
-----------
50
a = 'this is python'
print(a.split())
----------------
51
光棍节就要到了，要不要给你介绍个 python 对象？

a = 'blog.csdn.net/xufive/article/details/102946961'
print(a.split('/'))
--------------------
52
a = '2.72, 5, 7, 3.14'
print(a.replace(',',','))
a = a.split(",")
print(list(map(float,a)))
-------------
53
def why_you_can_not_work():
    if b != 0 and c == 0:
        print('it is all letter')
    elif b == 0 and c != 0:
        print('it is all number')
    else:
        print('i have no idea')


a = 'adS12K56'
q = 0
b = 0
c = 0
while q < len(a) :
    if 'a' <= a[q] <= 'z' :
        b = b + 1
    else:
        c = c + 1
    q += 1

print(why_you_can_not_work())


if a.isascii():
    print(True)
else:
    print(False)
-----------------------------------------
54
a = 'there is python'
print(a.replace('is','are'))
----------------
55
a =  '\t python \n'
a = a.replace('\t','')
a = a.replace('\n','')
print(a)
---------------------------------------
56
a = 'ok hello thank you'
a = a.split()
for i in a :
    print(i)
for b in a:
    print("{:>10}".format(b))
for c in a:
    print("{:^10}".format(c))
----------------------------------
57
a = ['a','b','c']
a = '|'.join(a)
print(a)
'''













import numpy














