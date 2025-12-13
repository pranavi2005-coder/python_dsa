# greatest among 3 numbers using functions
def greatest(a,b,c):
    if a>b and a>c:
        print("a is greater than b and c")
    elif b>c and b>a:
        print("b is greater than a and c")
    elif c>a and c>b:
        print("c is greater than a and b")
greatest(297,198,70)


def add(a,b,c):
    print(a+b+c)
add(20,60,40)



def add(a,b,c):
    return a+b+c
print(add(12,22,20))


#calculator:
x=int(input("enter a number:"))
y=int(input("enter another number:"))
method=input("enter a method")
if method=="add":
    print(x+y)
elif method=="sub":
    print(x-y)
elif method=="mul":
    print("x*y")
elif method=="div":
    print("x/y")
else:
    print("it is not a method")