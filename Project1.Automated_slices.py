Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> word = "supercalifragilisticexpialidocious"
>>> word[-2]
'u'
\
>>> word[-5]
'c'
>>> word[-1]
's'
>>> word.index("cali")
5

>>> word[word.index("cali"):word.index("fragi")]
'cali'
>>> 