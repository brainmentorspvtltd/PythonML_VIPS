Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> arr = [12,34,56,78,'hello',10.5]
>>> arr[0]
12
>>> a[0:4]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a[0:4]
NameError: name 'a' is not defined
>>> arr[0:4]
[12, 34, 56, 78]
>>> a[-1]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a[-1]
NameError: name 'a' is not defined
>>> arr[-1]
10.5
>>> a = [12,34,11,17,78,9,14]
>>> sorted(a)
[9, 11, 12, 14, 17, 34, 78]
>>> sorted(a, reverse = True)
[78, 34, 17, 14, 12, 11, 9]
>>> a
[12, 34, 11, 17, 78, 9, 14]
>>> a.sort()
>>> a
[9, 11, 12, 14, 17, 34, 78]
>>> 14 in a
True
>>> a.index(14)
3
>>> a.append(90)
>>> a
[9, 11, 12, 14, 17, 34, 78, 90]
>>> a.insert(0,5)
>>> a
[5, 9, 11, 12, 14, 17, 34, 78, 90]
>>> a.pop()
90
>>> a.pop(4)
14
>>> a.remove(0)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.remove(0)
ValueError: list.remove(x): x not in list
>>> a.remove(5)
>>> a
[9, 11, 12, 17, 34, 78]
>>> t = (12,34,56)
>>> dict_1 = {'id':101,'name':'Ram','college':'IP'}
>>> dict_1[0]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    dict_1[0]
KeyError: 0
>>> dict_1['name']
'Ram'
>>> dict_1['age'] = 19
>>> dict_1
{'id': 101, 'name': 'Ram', 'college': 'IP', 'age': 19}
>>> s = {2,4,6,7,23,45,8}
>>> type(s)
<class 'set'>
>>> s1 = {4,5,7,8,9,0,0}
>>> s.intersection(s1)
{8, 4, 7}
>>> s.union(s1)
{0, 2, 4, 5, 6, 7, 8, 9, 45, 23}
>>> s & s1
{8, 4, 7}
>>> s | s1
{0, 2, 4, 5, 6, 7, 8, 9, 45, 23}
>>> 
