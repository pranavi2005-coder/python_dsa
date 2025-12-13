#Stack:it is a linear data structure which follows LIFO and time complexity of deleting or inserting the element in a stack O(n)
stck=[26,58,28,90,67,96]
stck.append(60)
stck.append(70)
stck.append(14)
stck.append(78)
print(stck)
print(stck[-1])
stck.pop(-1)
print(stck)



stck=[]
stck.append('m')
stck.append('o')
stck.append('n')
palindrome=stck[::-1]
if palindrome==stck:
    print("it is a palindrome")
else:
    print("not a palindrome")


string="{[()]}"
stck=[]
hashmap={')':'(','}':'{',']':'['}
flag=True
for i in range(len(string)):
    if string in "({[":
        stck.append(string[i])
    else:
        if not stck or stck[-1]!=hashmap(string[i]):
            flag=False
            break
        stck.pop()
if flag:
    print("valid")
else:
    print("invalid")


# queue:it is a linear data structure which follows FIFO principle
# time complexity for inserting and removing any element is O(1) 
# inserting element in queue:enqueue
# deleting element in queue:dequeue
# best way of implementing queues is OOPS

queue=[]
queue.append(20)
queue.append(96)
queue.append(89)
queue.append(34)
queue.append(2)
queue.append(78)
while queue:
    print(queue[0])
    queue.pop(0)


queue=[]
while queue:
    print(queue[0],end=" ")
    queue.pop(0)
def enqueue(ele):
    queue.append(ele)
def dequeue():
    print(queue[0])
    queue.pop(0)
queue=[]
enqueue(26)
enqueue(9)
enqueue(70)
enqueue(7)

dequeue()


# queues using stacks:
stck1=[]
stck2=[]
def enqueue(ele):
    stck1.append(ele)
def dequeue():
    if stck2==[]:
        while stck1:
            stck2.append(stck1[-1])
            stck1.pop()
    print(stck2[-1])
    stck2.pop()
enqueue(96)
enqueue(40)
enqueue(60)
enqueue(80)
dequeue()
