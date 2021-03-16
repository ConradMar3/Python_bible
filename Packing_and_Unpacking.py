Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print (1, 2, 3, 4, 5)
1 2 3 4 5
>>> numbers = [1, 2, 3, 4, 5]
>>> print(numbers)
[1, 2, 3, 4, 5]
>>> print(*numbers)
1 2 3 4 5
>>> 
>>> def add(x + y)
SyntaxError: invalid syntax
>>> def add(x,y)
SyntaxError: invalid syntax
>>> def add(x,y):
	return x + y

>>> add(50, 50)
100
>>> def add(*numbers):
	total = 0
	for number in numbers:
		total = total + number
	return(total)

>>> add(1, 2, 3, 4, 5, 6)
21
>>> numbers = (1, 2, 3, 4, 5, 6)
>>> print(numbers)
(1, 2, 3, 4, 5, 6)
>>> 
>>> 
>>> def about(name, age, likes):
	sentence = "Meet {}! He is {} years old. He likes {}"
	return sentence

>>> dictionary = {"name": "Conrad", "age": 31, "likes": "Python"}
>>> about(**dictionary)
'Meet {}! He is {} years old. He likes {}'
>>> 