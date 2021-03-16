Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> words = ["The", "fox", "jumps", "over", "the", "lazy", "dog"]
>>> answer = [[w.upper(), w.lower(), len(w)] for w in words]
>>> print(answer)
[['THE', 'the', 3], ['FOX', 'fox', 3], ['JUMPS', 'jumps', 5], ['OVER', 'over', 4], ['THE', 'the', 3], ['LAZY', 'lazy', 4], ['DOG', 'dog', 3]]
>>> 