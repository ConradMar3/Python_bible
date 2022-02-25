Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> string = "ABCDEFG123456"
>>> word = "supercalifragilisticexpialidocious"
>>> word[0]
's'
\
>>> word[2]
'p'
>>> word[0:5:1]
'super'
>>> word[5:9:1]
'cali'
>>> word[5:]
'califragilisticexpialidocious'
>>> word[5::2]
'clfaiitcxildcos'
>>> word[[:7]
     
SyntaxError: invalid syntax
>>> word[:7]
'superca'
>>> word[::-1]
'suoicodilaipxecitsiligarfilacrepus'
>>> 