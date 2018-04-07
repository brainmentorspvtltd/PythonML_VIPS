Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("Hello world")
Hello world
>>> a = 12
>>> b = 13
>>> c = a + b
>>> print(c)
25
>>> type(a)
<class 'int'>
>>> c = "Hello"
>>> type(c)
<class 'str'>
>>> d = 10.5
>>> type(d)
<class 'float'>
>>> c
'Hello'
>>> c * 10
'HelloHelloHelloHelloHelloHelloHelloHelloHelloHello'
>>> a = "Hello"
>>> a,b = 10,12
>>> a,b = b,a
>>> a
12
>>> b
10
>>> a = "Hello"
>>> a[0]
'H'
>>> a[3]
'l'
>>> a[0:4]
'Hell'
>>> a[-1]
'o'
>>> a[::-1]
'olleH'
>>> a = "Hello python"
>>> a[:]
'Hello python'
>>> a[0:]
'Hello python'
>>> a[0:10:2]
'Hlopt'
>>> a[::-1]
'nohtyp olleH'
>>> 
======== RESTART: C:/Users/asus/Desktop/Pythom+ML_VIPS/PythonLoop.py ========
Value of i is 10
Inside Loop
Value of i is 11
Inside Loop
Value of i is 12
Inside Loop
Value of i is 13
Inside Loop
Value of i is 14
Inside Loop
Value of i is 15
Inside Loop
Value of i is 16
Inside Loop
Value of i is 17
Inside Loop
Value of i is 18
Inside Loop
Value of i is 19
Inside Loop
Outside Loop
>>> 
======== RESTART: C:/Users/asus/Desktop/Pythom+ML_VIPS/PythonLoop.py ========
Value of i is 10
Inside Loop
Value of i is 11
Inside Loop
Value of i is 12
Inside Loop
Value of i is 13
Inside Loop
Value of i is 14
Inside Loop
Value of i is 15
Inside Loop
Value of i is 16
Inside Loop
Value of i is 17
Inside Loop
Value of i is 18
Inside Loop
Value of i is 19
Inside Loop
Outside Loop
>>> for i in range(5):
	print('*' * i)

	

*
**
***
****
>>> for i in range(15):
	print('*' * i)

	

*
**
***
****
*****
******
*******
********
*********
**********
***********
************
*************
**************
>>> for i in range(10):
	print(' ' * (10-i) + '*' * (2 * i)+1)

	
Traceback (most recent call last):
  File "<pyshell#35>", line 2, in <module>
    print(' ' * (10-i) + '*' * (2 * i)+1)
TypeError: must be str, not int
>>> for i in range(10):
	print(' ' * (10-i) + '*' * ((2 * i)+1))

	
          *
         ***
        *****
       *******
      *********
     ***********
    *************
   ***************
  *****************
 *******************
>>> for i in reversed(range(10)):
	print(i)

	
9
8
7
6
5
4
3
2
1
0
>>> 
====== RESTART: C:/Users/asus/Desktop/Pythom+ML_VIPS/PythonWhileLoop.py ======
0
1
1
2
3
5
8
13
21
34
55
89
>>> 
====== RESTART: C:/Users/asus/Desktop/Pythom+ML_VIPS/PythonWhileLoop.py ======
0 1 1 2 3 5 8 13 21 34 55 89 
>>> 
