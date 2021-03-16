Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(x,y):
	x+y

	
>>> add(5,20)
>>> print(add)
<function add at 0x000001F27C5E3EE0>
>>> def add(x,y):
	return x+y

>>> add(5, 20)
25
>>> answer = add(100, 20)
>>> answer
120
>>> word = "pen"
>>> word[::-1]
'nep'
>>> 
>>> def rev(text):
	return text[::-1]
rev("hello")
SyntaxError: invalid syntax
>>> rev("hello")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    rev("hello")
NameError: name 'rev' is not defined
>>> def rev(text):
	return text[::-1]

>>> rev("hello")
'olleh'
>>> 