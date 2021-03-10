Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = "happy birthday"
>>> x.index("birthday")
6
>>> x.find("birthday")
6
>>> y = "000happybirthday000"
>>> y.strip("0")
'happybirthday'
>>> y.lstrip("0")
'happybirthday000'
>>> name = input("Who?:")
Who?:C
>>> print(name)
C
>>> len(name)
1
>>> name = input("Who?:").strip()
Who?:Conrad
>>> print(name)
Conrad
>>> len(name)
6
>>> 