# sum of elements in an array
arr=[1,2,3,4,5,6,8]
res=0
for i in range(len(arr)):
    res=res+arr[i]
print(res)


# find given element in an array
arr=[12,3,44,5,67,8,96]
n=96
for i in range(len(arr)):
    if n==arr[i]:
        print("n is present at:",i)


# variation2:
arr=list(map(int,input("enter: ").split()))
n=int(input("enter a number:"))
flag=False
indx=-1
for i in range(len(arr)):
    if n==arr[i]:
        flag=True
        indx=i
        print("element is present",indx)
else:
    print("element is not present")

# duplicate elements:
arr=list(map(int,input("enter:").split()))
flag=True 
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            flag=False
if flag:
    print("it is a good array")
else:
    print("it is bad array")

n=5
num=1
for rows in range(1,n+1):
    for col in range(1,rows+1):
        print(col,end=" ")
        num=col+0
    print()


n=5
num=1
for rows in range(1,n+1):
    for col in range(1,rows+1):
        print(num,end=" ")
        num=num+1
    print()

n=6
num=1
for rows in range(1,n+1):
    for col in range(1,rows+1):
        print("*",end=" ")
        num=num+1
    print()

n=6
num=1
for rows in range(1,n+1):
    for col in range(rows,n+1):
        print("*",end=" ")
        num=num+0
    print()


n=4
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



# Z pattern
n=4
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==n-row-1 or row+col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


arr=list(map(int,input("enter:").split()))
for i in range(len(arr)):
    print(arr[i],end=" ")


#adding the elements in an array:
arr=list(map(int,input("enter:").split()))
result=0
for i in range(len(arr)):
    result=result+arr[i]
print(result)


