Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def about(name, age, likes):
	sentence = "Meet {}! They are {} years old. They like {}".format(name, age, likes)
	return sentence

>>> about
<function about at 0x000002596E763EE0>
>>> about("Jack", 32, "Python")
'Meet Jack! They are 32 years old. They like Python'
>>> about(name = "Jack", age = 32, likes = "Python")
'Meet Jack! They are 32 years old. They like Python'
>>> about()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    about()
TypeError: about() missing 3 required positional arguments: 'name', 'age', and 'likes'
>>>  def about(name, age, likes = "Python"):
	sentence = "Meet {}! They are {} years old. They like {}".format(name, age, likes)
	return sentence
SyntaxError: unexpected indent
>>> 
>>> def about(name, age, likes = "Python"):
	sentence = "Meet {}! They are {} years old. They like {}".format(name, age, likes)
	return sentence

>>> 
>>> about()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    about()
TypeError: about() missing 2 required positional arguments: 'name' and 'age'
>>> def about(name, age, likes = "Python"):
	sentence = "Meet {}! They are {} years old. They like {}".format(name, age, likes)
	return sentence

>>> about("Jack", 32)
'Meet Jack! They are 32 years old. They like Python'
>>> about()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    about()
TypeError: about() missing 2 required positional arguments: 'name' and 'age'
>>> about("Jack", 32, "Python")
'Meet Jack! They are 32 years old. They like Python'
>>> about()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    about()
TypeError: about() missing 2 required positional arguments: 'name' and 'age'
>>> 