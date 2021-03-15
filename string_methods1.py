Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> "hello".count("e")
1
>>> text = "happy birthday"
>>> text.count("a")
2
>>> text.count("day")
1
>>> x = "Happy Birthday"
>>> x.lower()
'happy birthday'
>>> x.upper()
'HAPPY BIRTHDAY'
>>> x
'Happy Birthday'
>>> x = x.upper()
>>> x
'HAPPY BIRTHDAY'
>>> x = x.lower()
>>> x
'happy birthday'
>>> x = x.capitalize()
>>> x
'Happy birthday'
>>> x.title()
'Happy Birthday'
>>> x = x.title()
>>> x
'Happy Birthday'
>>> x.islower()
False
>>> x.isupper()
False
>>> x.istitle()
True
>>> x.isalpha()
False
>>> x
'Happy Birthday'
>>> x.isdigit()
False
>>> "12345".isdigit()
True
>>> y = "HappyBirthday123"
>>> y.isalnum()
True
>>> 