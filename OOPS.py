# OOPs object oriented programming language:
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def study(self):
        print(self.name,"is studying")
s1=student("pranavi",20)
s2=student("lasya",19)
s1.study()
s2.study()


class BankAccount:
    def __init__(self,balance):
        selfbalance=balance
        self_pin=1234
        self__password="abc123"
        def get_password(self):
            return self__password
account=BankAccount(1000)
print(account)


class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self._pin = 1234
        self.__password = "abc123"
    def get_password(self):
        return self.__password
    def __repr__(self):
        return f"BankAccount(balance={self.balance})"
account = BankAccount(1000)
print(account)
print(account.get_password())


# kadanes algorithm:
# if you find any current sum which is less 0 than just make your current sum as zero
# where you can reduce your time complexity
# here single for loop is used
# kadanes algorithm is used to reduce time complexity
# if current sum is negative then it makes current sum as zero
arr=[-2,-1,0,2,9]
arr[0]=-2
current=0
maxi=0
for i in range(len(arr)):
    current=current+arr[i]
    maxi=max(maxi,current)
    if current<0:
        current=0
print(maxi)



# finding length of maximum sum of subarray using kadanes algorithm:
arr=[-2,-1,0,1,2]
k=3
max_length=0
for i in range(len(arr)):
    sum=0
    for j in range(len(arr)):
        sum=sum+arr[j]
        if sum<=k:
            if max_length<j-i+1:
                max_length=j-i+1
print(max_length)


# sliding window:
# sliding window is a technique used in subarrays to find the sum of continuous elements within the given window size.
arr=[1,2,3,4,5,6]
k=3
n=len(arr)
sum=0
for i in range(k):
    sum=sum+arr[i]
    max_sum=sum
for i in range(n-k):
    sum=sum+arr[i]+arr[i+k]
max_sum=max(max_sum,sum)
print(max_sum)

# OOPS:object oriented programming structure
# my OOPS consist of classes,objects,constructors and methods 

# class is a blueprint of my entire source code
# methods and attritubes are accessed
# constructor is used to execute our code automatically
# in python we added default constructor called __init__
# my constructor consist of atleast one parameter called self

# self is a keyword which refers to the current instance
# method is a function which is created inside the class block


class students:
    name="pranavi"
    rollno="23N31A0496"
    year="3rd year"
s1=students
print(s1.name)
print(s1.rollno)
print(s1.year)


# THE FOUR PILLARS OF OOPS:
# 1.ABSTRACTION
# 2.INHERITANCE:it can acquire properties from parent class
# 3.ENCAPSULATION
# 4.POLYMORPHISM:it consists of method overriding and method overloading


# abstraction:
class student:
    def __init__(self,name,rollno,year):
        self.name=name
        self.rollno=rollno
        self.year=year
    def aboutstudent(self):
        print(self.name,self.rollno,self.year)
s1=student("pranavi","23N31A0496","3rd")
s2=student("meghana","23N31A04A6","3rd")
print(s1.name,s1.rollno,s1.year)
print(s2.name,s2.rollno,s2.year)


class pen:
    def __init__(self,brand,type,price,color):
        self.brand=brand
        self.type=type
        self.price=price
        self.color=color
    def aboutpen(self):
        print(self.brand,self.type,self.price,self.color)
p1=pen("cello","ball","10","blue")
p2=pen("butterflow","gel","20","black")
p1.aboutpen()
p2.aboutpen()


# inheritance
class parent:
    def _init_(self):
        print("parent")
    def parent1(self):
        print("I'm parent1")
    def parent2(self):
        print("I'm parent2")
class child(parent):
    def child1(self):
        print("I'm child 1")
    def child2(self):
        print("I'm child 2")
c1=child()
c1.child1()
c1.parent1()


# encapsulation:
class Bank:
    def __init__(self,amount):
        self.balance=amount
    def debit(self,amount):
        self.balance-=amount
        print("debited amount:",amount)
        print("total:",self.balance)
    def credit(self,amount):
        self.balance+=amount
        print("credited amount:",amount)
        print("total:",self.balance)
user=Bank(2000)
user.balance=10000
print(user.balance)
user.debit(200)
user.credit(500)
user.debit(100)
user.credit(600)


# polymorphism:

# method overloading:same method name with different behaviour
class poly:
    def add(self,num1,num2):
        return num1+num2
p1=poly()
print(p1.add(8,26))
print(p1.add("pranu ","is beautiful"))

# method overriding:
class dog:
    def sound(self):
        print("dog sound")
class cat(dog):
    def sound(self):
        super().sound()
        print("cat sound")
c=cat()
c.sound()




