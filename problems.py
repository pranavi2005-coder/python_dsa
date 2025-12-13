# arr=[1,2,3,4,5,6,7]
# sum=0
# for num in arr:
#     sum=sum+num
# print("sum=",sum)


# arr=[1,2,3,4,5,6,7]
# res=0
# for i in range(len(arr)):
#     res=res+arr[i]
#     print(res)

# #count of even and odd numbers in an array
# arr=[1,2,3,4,5,6,7,8,9]
# even=0
# odd=0
# for num in arr:
#     if num%2==0:
#         even=even+1
#     else:
#         odd=odd+1
# print("even=",even)
# print("odd=",odd)


# #finding max value:
# arr=[1,2,3,4,5,6,7]
# max=0
# for num in arr:
#     if num>max:
#         max=num
# print("maximum value:",max)


# arr=[1,2,3,4,5,6,7,8]
# maxi=0
# for i in range(len(arr)):
#     if maxi<arr[i]:
#         maxi=arr[i]
#     print(maxi)

# #reverse of a string:
# arr=[-1,-2,-3,-4,-5,-6,-7,-8]
# for i in range(len(arr)-1,-1,-1):
#     print(arr[i])

# #finding roots:
# a=4
# b=2
# res=1
# for i in range(b):
#     res=res*a
# print(res)


# #factorial:
# n=int(input("enter a value:"))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)


# #fibonacci series:
# first=0
# sec=1
# n=5
# for i in range(n):
#     print(first)
#     new=first+sec
#     first=sec
#     sec=new



# first=0
# sec=1
# n=5
# for i in range(n):
#     new=first+sec
#     first=sec
#     sec=new
#     print(first,end=" ")


# #reverse of number:
# n=int(input("enter a number:"))
# res=0
# while n>0:
#     rem=n%10
#     res=res*10+rem
#     n=n//10
# print(res)


# #adding integers:
# n=12345
# result=0
# while n>0:
#     rem=n%10
#     result=result+rem
#     n=n//10
# print(result)


# #2**n problem using functions:
# def power(n):
#     count=1
#     for i in range(n):
#         count=count*2
#     print(count)
# power(5)


# #factorial
# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# print(fact(5))

# # sub arrays:a array itself  is called as a sub array
# # sub arrays are considered as continuous elements in array
# # carry forward:
# arr=[1,2,3,4]
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         for k in range(i,j+1):
#             print(arr[k],end=" ")
#         print()


# # sum of sub array:
# arr=[1,2,3,4,5]
# count=0
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         for k in range(i,j+1):
#             count=count+arr[k]
# print(count)


# # maximum subarray sum:
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



# # for reducing time complexity removing for loop:
# arr=[-15,-20,-1,-3]
# max=arr[0]
# for i in range(len(arr)):
#     count=0
#     for j in range(i,len(arr)):
#         count=count+arr[j]
#         if max<count:
#             max=count
# print(max)
# # maximum time complexity for finding sum of subarrays is O(n**2)


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


# problems on linked list:
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
#     def addElements(self):
#         temp=self.head
#         sum=0
#         while temp!=None:
#             sum=sum+temp.data
#             temp=temp.next
#         return sum
# l1=linkedlist()
# l1.InsertionAtEnd(10)
# l1.InsertionAtEnd(20)
# l1.InsertionAtEnd(30)
# l1.display()
# print()
# print("sum of all elements in the linked list is:",l1.addElements())



#reverse of elements in linked list:
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
#     def reverse(self,Node):
#         if Node is None:
#             return
#         self.reverse(Node.next)
#         print(Node.data,end="->")
# l1=linkedlist()
# l1.InsertionAtEnd(10)
# l1.InsertionAtEnd(20)
# l1.InsertionAtEnd(30)
# l1.display()
# print()
# l1.reverse(l1.head)


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
#     def middle(self):
#         middle=self.head
#         end=self.head
#         while end!=None and end.next!=None:
#             middle=middle.next
#             end=end.next.next
#         return middle.data
# l1=linkedlist()
# l1.InsertionAtEnd(10)
# l1.InsertionAtEnd(20)
# l1.InsertionAtEnd(30)
# l1.display()
# print()
# print("middle element is:",l1.middle())


#duplicates of elements in linked list:
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def duplicates(self):
#         unique = set()
#         temp = self.head
#         while temp:
#             if temp.data in unique:
#                 print("bad list")
#                 return
#             else:
#                 unique.add(temp.data)
#             temp = temp.next
#         print("good list") 
# ll = LinkedList()
# ll.head = Node(10)
# ll.head.next = Node(20)
# ll.head.next.next = Node(30)
# ll.head.next.next.next = Node(40)
# ll.duplicates()   




