#function is a set of blocks of code
# 1.without parameter without return type
# 2.without parameter with return type
# 3.with parameter without return type
# 4.with parameter with return type

#1.without parameter without return type:
def name():
    print("pranavi")
name()

def name():
    a=10
    b=15
    print(a+b)
    print("pranavi")
name()

#2.with parameter without return type:
def add(a,b):
    print(a+b)
    print(add)
add(3,8)


def mul(c,d):
    print(c*d)
    print(mul)
mul(7,4)

#3.without parameter with return type:
def add():
    a=10
    b=8
    return a+b
print(add())


#4.with parameter and with return type:
def add(a,b):
    return a+b
print(add(30,20))

def fav(a,b,c):
    return a+b+c
print(fav("I ","LOVE ","BIRYANI"))


def fav(a,b,c):
    return a+b+c
def sub(d,f):
    return d-f
print(sub(30,5))
print("I ","LOVE ","BIRYANI")


def number(a,b,c):
    if a>b and a>c:
        return "a is greater"
    elif b>c and b>a:
        return "b is greater"
    elif c>a and c>b:
        return "c is greater"
result=number(10,20,30)
print(result)

