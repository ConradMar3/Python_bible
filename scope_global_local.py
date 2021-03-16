# a = 100
# a = 250
a = [1, 2, 3]

def f1():
    #a = 100
    #b = a + 10
    #global a
    a[0] = 5
    #a = 100 #global
    #print(b)
    print(a)

def f2():
    a = 50 #local
    print(a)

f1()
f2()
print(a)
#print(f1)
