name="pranavi"
print(len(name))
print(name[5])

name="pranavi rajulapati"
print(name)
print(len(name))
print(name[:7])
print(name[:-3])
print(name[::-1])
greet="hi"
print(greet+name)

name=input("enter a string:")
greet="hello"
print(greet+name)

name="pranu"
print(name.upper())


name="SRINIVASARAO"
print(name.lower())

# palindrome
number=960
str1=str(number)
if str1==str1[::-1]:
    print("it is a palindrome")
else:
    print("it is not a palindrome")


#vowels
name="pranavi"
count=0
for i in range(len(name)):
    if name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o' or name[i]=='u':
        count=count+1
print(count)

name=input("enter a string:")
vowels="aeiou"
count=0
for ch in name:
    if ch in vowels:
        count=count+1
print(count)


# string to int conversion:
str1="25"
str2="50"
num1=int(str1)
num2=int(str2)
print(num1+num2)

# int to string conversion
num1=96
num2=12
str1=str(num1)
str2=str(num2)
print(str1+str2)


# integer to binary conversion
num=5
int1=bin(num)
print(int1)



# without 0b prefix
num=5
int1=bin(num)[2:]
print(int1)

# character to ord
char="a"
print(ord(char))

