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


