# DSA Day 7 — Stack and Queue

# today's topic:
        # stack (LIFO)
        # Queue (FIFO)
        # append()
        # pop()
        # deque
        # Reverse String
        # Valid Parentheses
        # LeetCode 20/225/232

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# what is stack?
# a stack follows LIFO: the last element added is the first one removed.
# think of a stack of plates. you put a new plate on top and remove the top plate first.
# basic stack operations:

# append(x)   :push an element           : time O(1)
# pop()       : remove the top element   : time O(1)
# stack[-1]   :peek at the top element   : time O(1)
# len(stack)  :count elements            : time O(1)
stack=[]
stack.append(10)
stack.append(20) 
stack.append(30) 
stack.append(40)
print(stack)
print("top element in the stack :",stack[-1])  #peek at the top element

removed= stack.pop()  #removed the top element
print("removed from the top",removed)       
print(stack)

# output:
# [10, 20, 30, 40]
# top element in the stack : 40
# removed from the top 40
# [10, 20, 30]


# calling pop() on an empty list raise an indexerror


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# reverse a string using a stack.
def reverse_string(text):
    stack=[]
    for ch in text:
        stack.append(ch)
    result=""
    while stack:
        result+=stack.pop()
    return result
print(reverse_string("hello"))

# output:
# olleh

# time: O(n)
# space: O(n)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# valid parentheses
# this is a popular stack interview problem.

# given "({[]})" , determine whether the brackets are balanced and corectly nested.

def is_valid(text):
    stack=[]
    pairs={
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for char in text:
        if char in "([{":
            stack.append(char)
        else:
            if not stack:
                return False
            if stack.pop()!=pairs[char] :
                return False
    
    return len(stack)==0
print(is_valid("{([])}")) 
print(is_valid("[[{(})]]"))

# output:
# True
# False

# time O(n)
# space O(n)



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# what is queue?
# a queue follows FIOF: first in first out.
# think of a people standing in a line . the person who arrive first is served first.

# use deque in python
# avoid using list.pop(0) for large because it take O(n) time.

from collections import deque
queue = deque()

# enqueue
queue.append(10)
queue.append(20)
queue.append(10)

# deque
print(queue.popleft())  #10
print(queue)   

# output:
# 10
# deque([20, 10])


# enqueue       :      queue.append(x)           : O(1)
# dequeue       :      queue.popleft()           : O(1)
# peek at front :       queue[0]                 : O(1)



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# leetcode practice
# 20. Valid Parentheses
# Use a stack to match opening and closing brackets

def is_valid(text):
    stack=[]
    pairs={
        ")":"(",
        "}":"{",
        "]":"["
    }
    for ch in text:
        if ch in "{[(":
            stack.append(ch)
        else:
            if not stack:
                return False
            if stack.pop()!=pairs[ch]:
                return False
    return len(stack)==0
print(is_valid("[({()})]"))
print(is_valid("[[{}()"))

# outout:
# True
# False

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Leetcode
# 225. Implement Stack using Queues
# Learn how stack behavior can be implemented using queues.

from collections import deque
class Mystack:
    def __init__(self):
        self.queue=deque()
    def push(self,x):
        self.queue.append(x)
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
    def pop(self):
        return self.queue.popleft()
    def top(self):
        return self.queue[0]
    def empty(self):
        return len(self.queue)==0
obj=Mystack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.push(50)
print(obj.top())
print(obj.pop())
print(obj.top())
print(obj.pop())
print(obj.top())
print(obj.pop())
print(obj.top())
print(obj.pop())
print(obj.top())
print(obj.pop())
print(obj.empty())

# output:
# 50
# 50
# 40
# 40
# 30
# 30
# 20
# 20
# 10
# 10
# True

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Leetcode:
# 232. Implement Queue using Stacks
# Learn how two stacks can implement queue behavior.

class MyQueue:
    def __init__(self):
        self.stack=[]
    def push(self,x):
        self.stack.append(x)
        for i in range(len(self.stack)-1):
            self.stack.append(self.stack.pop(0))
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def empty(self):
        return len(self.stack)==0
obj=MyQueue()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.push(50)
print(obj.peek())
print(obj.pop())
print(obj.peek())
print(obj.pop())
print(obj.peek())
print(obj.pop())
print(obj.peek())
print(obj.pop())
print(obj.peek())
print(obj.pop())
print(obj.empty())

# output:
# 10
# 10
# 20
# 20
# 30
# 30
# 40
# 40
# 50
# 50
# True


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                        # practice question


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Reverse a string using a stack

def Reverse(text):
    stack=[]
    for ch in text:
        stack.append(ch)
    result=""
    while stack:
        result+=stack.pop()
    return result

print(Reverse("ready"))

# output:
# ydaer


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------