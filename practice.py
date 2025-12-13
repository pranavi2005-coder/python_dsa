# greatest among 3 numbers using functions
# def greatest(a,b,c):
#     if a>b and a>c:
#         print("a is greater than b and c")
#     elif b>c and b>a:
#         print("b is greater than a and c")
#     elif c>a and c>b:
#         print("c is greater than a and b")
# greatest(297,198,70)


# def add(a,b,c):
#     print(a+b+c)
# add(20,60,40)



# def add(a,b,c):
#     return a+b+c
# print(add(12,22,20))


# adding elements in an array
# arr=list(map(int,input("enter : ").split()))
# result=0
# for i in range(len(arr)):
#     result=result+arr[i]
# print(result)


# 2**n program  using functions
# def power(n):
#     count=1
#     for i in range(n):
#         count=count*2
#     print(count)
# n=int(input("enter ="))
# power(n)



# factorial of a number using functions
# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
# fact(6)


# factorial using recursion
# def fact(n):
#     if n == 0 or n == 1:   # base case
#         return 1
#     else:
#         return n * fact(n - 1)   # recursive call
# print(fact(8))



# name="pranavi"
# print(name)
# n=int(input("enter a number:"))
# if n%2==0:
#     print("even number")
# else:
#     print("odd number")


# sum of elements in an array
# arr=[1,2,3,4,5,6,8]
# res=0
# for i in range(len(arr)):
#     res=res+arr[i]
# print(res)


# find given element in an array
# arr=[12,3,44,5,67,8,96]
# n=96
# for i in range(len(arr)):
#     if n==arr[i]:
#         print("n is present at:",i)


# variation2:
# arr=list(map(int,input("enter: ").split()))
# n=int(input("enter a number:"))
# flag=False
# indx=-1
# for i in range(len(arr)):
#     if n==arr[i]:
#         flag=True
#         indx=i
#         print("element is present",indx)
# else:
#     print("element is not present")

# duplicate elements:
# arr=list(map(int,input("enter:").split()))
# flag=True 
# for i in range(len(arr)-1):
#     for j in range(i+1,len(arr)):
#         if arr[i]==arr[j]:
#             flag=False
# if flag:
#     print("it is a good array")
# else:
#     print("it is bad array")

# n=5
# num=1
# for rows in range(1,n+1):
#     for col in range(1,rows+1):
#         print(col,end=" ")
#         num=col+0
#     print()


# n=5
# num=1
# for rows in range(1,n+1):
#     for col in range(1,rows+1):
#         print(num,end=" ")
#         num=num+1
#     print()

# n=6
# num=1
# for rows in range(1,n+1):
#     for col in range(1,rows+1):
#         print("*",end=" ")
#         num=num+1
#     print()

# n=6
# num=1
# for rows in range(1,n+1):
#     for col in range(rows,n+1):
#         print("*",end=" ")
#         num=num+0
#     print()


# n=4
# for row in range(n):
#     for col in range(n):
#         if row==0 or row==n-1 or col==0 or col==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# Z pattern
# n=4
# for row in range(n):
#     for col in range(n):
#         if row==0 or row==n-1 or col==n-row-1 or row+col==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# string to int conversion:
# str1="25"
# str2="50"
# num1=int(str1)
# num2=int(str2)
# print(num1+num2)

# int to string conversion
# num1=96
# num2=12
# str1=str(num1)
# str2=str(num2)
# print(str1+str2)


# palindrome
# number=960
# str1=str(number)
# if str1==str1[::-1]:
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")



# integer to binary conversion
# num=5
# int1=bin(num)
# print(int1)



# without 0b prefix
# num=5
# int1=bin(num)[2:]
# print(int1)

# character to ord
# char="a"
# print(ord(char))

# sortinggggg

# bubble sort
# arr=[21,30,42,44,49,23,0,-1,17]
# for i in range(len(arr)):
#     for j in range(len(arr)-1-i):
#         if arr[j]>arr[j+1]:
#             new=arr[j]
#             arr[j]=arr[j+1]
#             arr[j+1]=new
# print(arr)

# searching consists of two algorithms 
# 1.linear search:it search the element by comparing each element
# 2.binary search:it works when the array is sorted
# arr=[-1,0,17,21,23,42,44,49]
# k=21
# lo=0
# high=len(arr)-1
# while lo<=high:
#     mid=(lo+high)//2
#     if arr[mid]==k:
#         print("element found")
#         break
#     elif k>arr[mid]:
#           lo=mid+1
#     elif k<arr[mid]:
#          high=mid-1


# def binary(arr,lo,high,k):
#     if lo+high:
#         return-1
#     mid=(lo+high)//2
#     if arr[mid]==k:
#         return mid
#     elif arr[mid]<k:
#         return binary(arr,mid+1,high,k)
#     elif arr[mid,k]:
#         return binary(arr,lo,mid-1,k)
# arr=[-1,0,3,2,4,7,6,5,7,8,9]
# k=6
# print(binary(arr,0,len(arr)-1,k)) 


# finding index of the element using binary search algorithm:
# arr=[2,3,4,5,6,7,7,7,7,8,9]
# target=3
# lo=0
# hi=len(arr)-1
# indx=-1
# while lo<=hi:
#     mid=(lo+hi)//2
#     if arr[mid]==target:
#         indx=mid
#         hi=mid-1
#     elif arr[mid]<target:
#         lo=mid+1
#     elif arr[mid]>target:
#         hi=mid-1
# print(indx)


# printing even numbers using functions
# def even(element):
#     return element%2==0
# arr=[-1,0,17,21,23,42,44,4,50,52,23]
# new_arr=list(filter(even,arr))
# print(new_arr)


# true or false:
# def even(element):
#     return element%2==0
# arr=[-1,0,17,21,23,42,44,4,50,52,23]
# new_arr=list(map(lambda element:element%2==0,arr))
# print(new_arr)


# def  divide(arr,lo,hi):
#     if lo>=hi:
#         return
#     mid=(lo+hi)//2
#     divide(arr,lo,mid)
#     divide(arr,mid+1,hi)
#     merge(arr,lo,mid,hi)
# def merge(arr,lo,mid,hi):
#     p1=lo
#     p2=mid+1
#     new_arr=[]
#     while p1<=mid and p2<=hi:
#         if arr[p1]<=arr[p2]:
#             new_arr.append(arr[p1])
#             p1=p1+1
#         else:
#             new_arr.append(arr[p2])
#             p2=p2+1
#     while p1<=mid:
#         new_arr.append(arr[p1])
#         p1=p1+1
#     idx=lo
#     for i in range(len(new_arr)):
#         arr[idx]=new_arr[i]
#         idx=idx+1
        
# arr=[1,6,9,4,0,2]
# divide(arr,0,len(arr)-1)
# print(arr)


# def divide(arr,lo,hi):
#     if lo>=hi:
#         return
#     mid=(lo+hi)//2
#     divide(arr,lo,mid)
#     divide(arr,mid+1,hi)
#     merge(arr,lo,mid,hi)
# def merge(arr,lo,mid,hi):
#     p1=lo
#     p2=mid+1
#     new_arr=[]
#     while p1<=mid and p2<=hi:
#         if arr[p1]<=arr[p2]:
#             new_arr.append(arr[p1])
#             p1=p1+1
#         else:
#             new_arr.append(arr[p2])
#             p2=p2+1
#     while p1<=mid:
#         new_arr.append(arr[p1])
#         p1=p1+1
#     idx=lo
#     for i in range(len(new_arr)):
#         arr[idx]=new_arr[i]
#         idx=idx+1
# arr=[1,8,7,6,4,0,2]
# divide(arr,0,len(arr)-1)
# print(arr)



# data structures:
# hash map:it is a data structure where elements are stored in key value pair
# hashmap={
#     "name":"pranavi",
#     "rollno":"23n31a0496",
#     "branch":"ece",
#     "section":"b"
# }
# print(hashmap["name"])
# print(hashmap["rollno"])
# print(hashmap["section"])
# print(hashmap.pop("section"))
# print(hashmap)


# manipulation functions:
# arr=[21,33,44,55,67,89,96,30,24,62,15,26]
# arr.sort()
# freq={}
# for i in range(len(arr)):
#     if arr[i] not in freq:
#         freq[arr[i]]=1
#     elif arr[i] in freq:
#         freq[arr[i]]+=1
# print(freq)

# sets:set is an data structure which only stores the unique elements
# arr=[23,57,89,99,9,32,44,21]
# new_arr=list(set(arr))
# if len(arr)==len(new_arr):
#     print("good array")
# else:
#     print("bad array")


# bit manipulation:
# num1=6
# num2=4
# print(num1|num2)
# print(num1&num2)
# print(num1^num2)
# print(~num2)
# print(~num1)
# print(num1<<1)
# print(num2>>1)
# print(num1>>1)
# print(num2<<1)


# finding even and odd without percentile
# n=int(input("enter:"))  
# n1=1
# if n&n1==0:
#     print("even no")
# else:
#     print("odd no")


# finding 2**n using bit manipulation
# n=int(input("enter:"))
# print(1<<n)
# print(n)


# Stack:it is a linear data structure which follows LIFO and time complexity of deleting or inserting the element in a stack O(n)
# stck=[26,58,28,90,67,96]
# stck.append(60)
# stck.append(70)
# stck.append(14)
# stck.append(78)
# print(stck)
# print(stck[-1])
# stck.pop(-1)
# print(stck)



# stck=[]
# stck.append('m')
# stck.append('o')
# stck.append('n')
# palindrome=stck[::-1]
# if palindrome==stck:
#     print("it is a palindrome")
# else:
#     print("not a palindrome")


# string="{[()]}"
# stck=[]
# hashmap={')':'(','}':'{',']':'['}
# flag=True
# for i in range(len(string)):
#     if string in "({[":
#         stck.append(string[i])
#     else:
#         if not stck or stck[-1]!=hashmap(string[i]):
#             flag=False
#             break
#         stck.pop()
# if flag:
#     print("valid")
# else:
#     print("invalid")


# queue:it is a linear data structure which follows FIFO principle
#time complexity for inserting and removing any element is O(1) 
#inserting element in queue:enqueue
#deleting element in queue:dequeue
# best way of implementing queues is OOPS

# queue=[]
# queue.append(20)
# queue.append(96)
# queue.append(89)
# queue.append(34)
# queue.append(2)
# queue.append(78)
# while queue:
#     print(queue[0])
#     queue.pop(0)


# queue=[]
# while queue:
#     print(queue[0],end=" ")
#     queue.pop(0)
# def enqueue(ele):
#     queue.append(ele)
# def dequeue():
#     print(queue[0])
#     queue.pop(0)
# queue=[]
# enqueue(26)
# enqueue(9)
# enqueue(70)
# enqueue(7)

# dequeue()


# queues using stacks:
# stck1=[]
# stck2=[]
# def enqueue(ele):
#     stck1.append(ele)
# def dequeue():
#     if stck2==[]:
#         while stck1:
#             stck2.append(stck1[-1])
#             stck1.pop()
#     print(stck2[-1])
#     stck2.pop()
# enqueue(96)
# enqueue(40)
# enqueue(60)
# enqueue(80)
# dequeue()


# prefix sum:
# arr=[10,20,30,40,50,60]
# count=0
# prefix_arr=[]
# for i in range(len(arr)):
#     count=count+arr[i]
#     prefix_arr.append(count)
# print(prefix_arr)



# sub arrays:a array itself  is called as a sub array
# sub arrays are considered as continuous elements in array
# carry forward:
# arr=[1,2,3,4]
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         for k in range(i,j+1):
#             print(arr[k],end=" ")
#         print()


# sum of sub array:
# arr=[1,2,3,4,5]
# count=0
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         for k in range(i,j+1):
#             count=count+arr[k]
# print(count)


# maximum subarray sum:
# arr=[1,2,3,4]
# maxi=0
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         count=0
#         for k in range(i,j+1):
#             count=count+arr[k]
#         print(count)


# arr=[-15,-20,-1,-3]
# maxi=arr[0]
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         count=0
#         for k in range(i,j+1):
#             count=count+arr[k]
#             if maxi<count:
#                 maxi=count
#                 print(maxi)


# for reducing time complexity removing for loop:
# arr=[-15,-20,-1,-3]
# max=arr[0]
# for i in range(len(arr)):
#     count=0
#     for j in range(i,len(arr)):
#         count=count+arr[j]
#         if max<count:
#             max=count
# print(max)
# maximum time complexity for finding sum of subarrays is O(n**2)


# arr=[3,2,3,4,5,6,7]
# k=10
# maxi=arr[0]
# for i in range(len(arr)):
#     count=0
#     for j in range(i,len(arr)):
#             count=count+arr[j]
#             if count>maxi:
#                   if count>maxi and count<=k:
#                         maxi=count
# print(maxi)

# arr=[10,-2,-3,5]
# k=-1
# mini=arr[0]
# for i in range(1,len(arr)):
#     if mini>arr[i]:
#         mini=arr[i]
# maxi=mini
# for i in range(len(arr)):
#     count=0
#     for j in range(i,len(arr)):
#         count=count+arr[j]
#         if count>maxi and count<=k:
#             maxi=count
# print(maxi)

# OOPs object oriented programming language:
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def study(self):
#         print(self.name,"is studying")
# s1=student("pranavi",20)
# s2=student("lasya",19)
# s1.study()
# s2.study()


# class BankAccount:
#     def __init__(self,balance):
#         selfbalance=balance
#         self_pin=1234
#         self__password="abc123"
#         def get_password(self):
#             return self__password
# account=BankAccount(1000)
# print(account)


# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#         self._pin = 1234
#         self.__password = "abc123"
#     def get_password(self):
#         return self.__password
#     def __repr__(self):
#         return f"BankAccount(balance={self.balance})"
# account = BankAccount(1000)
# print(account)
# print(account.get_password())


# kadanes algorithm:
# if you find any current sum which is less 0 than just make your current sum as zero
# where you can reduce your time complexity
# here single for loop is used
# kadanes algorithm is used to reduce time complexity
# if current sum is negative then it makes current sum as zero
# arr=[-2,-1,0,2,9]
# arr[0]=-2
# current=0
# maxi=0
# for i in range(len(arr)):
#     current=current+arr[i]
#     maxi=max(maxi,current)
#     if current<0:
#         current=0
# print(maxi)



# finding length of maximum sum of subarray using kadanes algorithm:
# arr=[-2,-1,0,1,2]
# k=3
# max_length=0
# for i in range(len(arr)):
#     sum=0
#     for j in range(len(arr)):
#         sum=sum+arr[j]
#         if sum<=k:
#             if max_length<j-i+1:
#                 max_length=j-i+1
# print(max_length)


# sliding window:
# sliding window is a technique used in subarrays to find the sum of continuous elements within the given window size.
# arr=[1,2,3,4,5,6]
# k=3
# n=len(arr)
# sum=0
# for i in range(k):
#     sum=sum+arr[i]
#     max_sum=sum
# for i in range(n-k):
#     sum=sum+arr[i]+arr[i+k]
# max_sum=max(max_sum,sum)
# print(max_sum)

# OOPS:object oriented programming structure
# my OOPS consist of classes,objects,constructors and methods 

#class is a blueprint of my entire source code
# methods and attritubes are accessed
# constructor is used to execute our code automatically
# in python we added default constructor called __init__
# my constructor consist of atleast one parameter called self

# self is a keyword which refers to the current instance
# method is a function which is created inside the class block


# class students:
#     name="pranavi"
#     rollno="23N31A0496"
#     year="3rd year"
# s1=students
# print(s1.name)
# print(s1.rollno)
# print(s1.year)


# THE FOUR PILLARS OF OOPS:
# 1.ABSTRACTION
# 2.INHERITANCE:it can acquire properties from parent class
# 3.ENCAPSULATION
# 4.POLYMORPHISM:it consists of method overriding and method overloading


# abstraction:
# class student:
#     def __init__(self,name,rollno,year):
#         self.name=name
#         self.rollno=rollno
#         self.year=year
#     def aboutstudent(self):
#         print(self.name,self.rollno,self.year)
# s1=student("pranavi","23N31A0496","3rd")
# s2=student("meghana","23N31A04A6","3rd")
# print(s1.name,s1.rollno,s1.year)
# print(s2.name,s2.rollno,s2.year)


# class pen:
#     def __init__(self,brand,type,price,color):
#         self.brand=brand
#         self.type=type
#         self.price=price
#         self.color=color
#     def aboutpen(self):
#         print(self.brand,self.type,self.price,self.color)
# p1=pen("cello","ball","10","blue")
# p2=pen("butterflow","gel","20","black")
# p1.aboutpen()
# p2.aboutpen()


#inheritance
# class parent:
#     def _init_(self):
#         print("parent")
#     def parent1(self):
#         print("I'm parent1")
#     def parent2(self):
#         print("I'm parent2")
# class child(parent):
#     def child1(self):
#         print("I'm child 1")
#     def child2(self):
#         print("I'm child 2")
# c1=child()
# c1.child1()
# c1.parent1()


# encapsulation:
# class Bank:
#     def __init__(self,amount):
#         self.balance=amount
#     def debit(self,amount):
#         self.balance-=amount
#         print("debited amount:",amount)
#         print("total:",self.balance)
#     def credit(self,amount):
#         self.balance+=amount
#         print("credited amount:",amount)
#         print("total:",self.balance)
# user=Bank(2000)
# user.balance=10000
# print(user.balance)
# user.debit(200)
# user.credit(500)
# user.debit(100)
# user.credit(600)


#polymorphism:

#method overloading:same method name with different behaviour
# class poly:
#     def add(self,num1,num2):
#         return num1+num2
# p1=poly()
# print(p1.add(8,26))
# print(p1.add("pranu ","is beautiful"))

#method overriding:
# class dog:
#     def sound(self):
#         print("dog sound")
# class cat(dog):
#     def sound(self):
#         super().sound()
#         print("cat sound")
# c=cat()
# c.sound()


#linked list:
# it is a linear data structure which consists of node where my node consists of next Reference
# each and every node is linked with next node
# TYPES OF LINKED LIST:
# 1.single linked list
# 2.double linked list
# 3.circular linked list

# 1.single linked list:consists of set of operations
# 1.insertion at head
# 2.insertion at end
# 3.insertion at position
# 4.deletion at head
# 5.deletion at end
# 6.deletion at position

# 1.INSERTION AT HEAD:
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class linkedlist:
#     def __init__(self):
#         self.head=None
#     def InsertionAtHead(self,data):
#         new_node=Node(data)
#         new_node.next=self.head
#         self.head=new_node
#     def display(self):
#         temp=self.head
#         while temp!=None:
#             print(temp.data,end="->")
#             temp=temp.next
#         print("None")
# l1=linkedlist()
# l1.InsertionAtHead(10)
# l1.InsertionAtHead(20)
# l1.InsertionAtHead(30)
# l1.InsertionAtHead(40)
# l1.display()



# INSERTION AT END:
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class linkedlist:
#     def __init__(self):
#         self.head=None
#     def InsertionAtEnd(self,data):
#         new_node=Node(data)
#         if self.head==None:
#             self.head=new_node
#             return
#         temp=self.head
#         while temp.next:
#             temp=temp.next
#         temp.next=new_node
#     def display(self):
#         temp=self.head
#         while temp:
#             print(temp.data,end="->")
#             temp=temp.next
#         print("None")
# l1=linkedlist()
# l1.InsertionAtEnd(10)
# l1.InsertionAtEnd(20)
# l1.InsertionAtEnd(30)
# l1.InsertionAtEnd(40)
# l1.display()



# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class linkedlist:
#     def __init__(self):
#         self.head=None
#     def insertAtPosition(self,data,position):
#         new_node=Node(data)
#         if position==0:
#             new_node.next=self.head
#             self.head=new_node
#             return
#         temp=self.head
#         for i in range(position-1):
#             if temp is None:
#                 print("position out of bounds")
#                 return
#             temp=temp.next
#         new_node.next=temp.next
#         temp.next=new_node
#     def display(self):
#         temp=self.head
#         while temp!=None:
#             print(temp.data,end=">>")
#             temp=temp.next
# list1=linkedlist()
# list1.insertAtPosition(10,0)
# list1.insertAtPosition(20,1)
# list1.insertAtPosition(30,1)
# list1.insertAtPosition(40,1)
# list1.display()


#deletion at head:
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class linkedlist:
#     def __init__(self):
#         self.head=None
#     def insertAtHead(self,data):
#         new_node=Node(data)
#         new_node.next=self.head
#         self.head=new_node
#     def deleteAtHead(self):
#         if self.head==None:
#             print("linked list is empty")
#             return
#         self.head=self.head.next
#     def display(self):
#         if self.head==None:
#             print("linked list is empty")
#             return
#         temp=self.head
#         while temp!=None:
#             print(temp.data,end=">>")
#             temp=temp.next
# list1=linkedlist()
# list1.insertAtHead(20) 
# list1.insertAtHead(30)  
# list1.display()
# list1.deleteAtHead()
# list1.display()

#insertion at position:
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class linkedlist:
#     def __init__(self):
#         self.head=None
#     def InsertionAtPos(self,data,pos):
#         new_node=Node(data)
#         if pos<1:
#             print("invalid")
#             return
#         if pos==1:
#             new_node.next=self.head
#             self.head=new_node
#             return
#         temp=self.head
#         count=1
#         while temp!=None and count<pos-1:
#             temp=temp.next
#         new_node.next=temp.next
#     def display(self):
#         temp=self.head
#         while temp!=None:
#             print(temp.data,end="->")
#             temp=temp.next
# l1=linkedlist()
# l1.InsertionAtPos(10,1)
# l1.InsertionAtPos(20,1)
# l1.InsertionAtPos(30,1)
# l1.display()


# slow pointer and fast pointer technique:
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class linkedlist:
#     def __init__(self):
#         self.head=None
#     def InsertionAtEnd(self,data):
#         new_node=Node(data)
#         if self.head==None:
#             self.head=new_node
#             return
#         temp=self.head
#         while temp.next:
#             temp=temp.next
#         temp.next=new_node
#     def display(self):
#         temp=self.head
#         while temp!=None:
#             print(temp.data,end="->")
#             temp=temp.next
#     def findMiddle(self):
#         slw_ptr=self.head
#         fast_ptr=self.head
#         if self.head is not None:
#             while fast_ptr is not None and fast_ptr.next is not None:
#                 slw_ptr=slw_ptr.next
#                 fast_ptr=fast_ptr.next.next
#             return slw_ptr.data
# l1=linkedlist()
# l1.InsertionAtEnd(10)
# l1.InsertionAtEnd(20)
# l1.InsertionAtEnd(30)
# l1.display()
# print()
# print("middle element is:",l1.findMiddle())



# Tree:it is a non linear data structure it consists of several nodes
# each node consists of three nodes
# data is separated as left and right
# each node consists of left partitian and right partitian

# TYPES OF TREES:
# 1.binary tree
# 2.binary search tree
# 3.heap-min
# 4.heap-max
# 5.AVL self balancing tree
# 6.red black self balancing tree

# 1.binary tree:
# top  most node is called root node
# root node consist of two partitians i.e left and right

# parent node:a node which consists of another sub nodes is called as parent node
# child node:the subnode from the parent node
# leaf node:when the left and right partitians are null then it is called as leaf node.
# it has levels which start from level0 and goes on...
# height of tree:the longest path between the root node to the leaf node which as maximum length
# edges:the link between two nodes is called as edge.
# number of edges=number of nodes-1

# tree traversal techniques:
# 1.inorder
# 2.pre order
# 3.post order

# 1. inorder tree traversal technique:
# which works under a principle called left root and right



class Node:
    def __init__(self,Node):
        self.data=Node
        self.left=None
        self.right=None
    
    

