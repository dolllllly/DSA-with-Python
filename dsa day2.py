# DSA Day 2: Arrays

# Today's topic:
    # Learn array operations
    # build problem-solving logic
    # practice coding questions
    # solve a LeetCode problem

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# What is an array?
# an array is a data structure that stores multiple elements in an ordered collection
# in python , we commonly use a list to perform array-style operations

# indexing:
# python indexing start from 0
numbers=[1,2,3,4,5]
print(numbers[0])  #1
print(numbers[1])   #2
print(numbers[2])   #3
print(numbers[3])   #4


# important array operations

# access by index
    # numbers[2]
    # typical time: O(1)

# update an element
    # numbers[2]=99
    # typical time: O(1)

# append to the end
    # numbers.append(60)
    # O(1) amortized

# inserrt at the bigining
    # numbers.insert(0,5)
    # typical time: O(n)

# delete by index
    # number.pop(2)
    # O(n)

# search for a value
    # 30 in numbers
    # O(n)

# why in inserting at the beginning O(n)? because existing elements may need to shift right.


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Traversing an array
# traversal means  visiing each element of a collection.

# method 1 : direct traversal

numbers=[10,20,30,40]
for number in numbers:
    print(number)

# method 2: indec based traversal

numbers=[10,20,30,40]
for i in range(len(numbers)):
    print(i,numbers[i])

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Two pointers
# the goal is to solve array problem efficiently using two indices

# What is the Two Pointers technique?
# instead of using just one index to traverse an array, we can use two pointers(variables representing position)

# for example:
numbers=[10,20,30,40.50]
left=0
right=len(numbers)-1
print(number[left])
print(number[right])

# output:
# 10
# 50

# the pointer start at opposite end of the array.

# 10      20      30      40       50
# left  index1  index2   index3   right

# move left->                   <-move rigth


# example : reverse an array in-place
# Instead of creating a new list, swap the first and last elements, then move both pointers inward

def reverse_array(numbers):
    left=0
    rigth=len(numbers)-1
    while left<rigth:
        numbers[left],numbers[rigth]=numbers[rigth],numbers[left]
        left+=1
        rigth-=1
    return numbers
print(reverse_array([1,2,3,4,5]))

# complexity:
# time: O(n)
# auxiliary space: O(1)

# When should you use Two Pointers?
# reversing an array
# Checking whether a string is a palindrome.
# Finding two numbers in a sorted array that add to a target.
# Moving zeros to the end.
# Removing duplicates from a sorted array.

# # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#                                                                      coding practice
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Reverse an array

# Easy · Time target: 10 minutes
# Input: [1, 2, 3, 4, 5]
# Expected output: [5, 4, 3, 2, 1]

# Constraint: Do not use reverse() or slicing with [::-1]

def reverse_array(numbers):
    left=0
    rigth=len(numbers)-1
    while left<rigth:
        numbers[left],numbers[rigth]=numbers[rigth],numbers[left]
        left+=1
        rigth-=1
    return numbers
print(reverse_array([1,2,3,4,5]))


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Count even and odd numbers
# Easy · Time target: 10 minutes
# Input: [1, 2, 3, 4, 5, 6]
# Expected output: Even = 3, Odd = 3
# Constraint: Traverse the array once.

def count_even_odd(numbers):
    even=0
    odd=0
    for num in numbers:
        if num%2==0:
            even+=1
        else:
            odd+=1
    return f'Even= {even}\nOdd= {odd}'
print(count_even_odd([1,2,3,4,5,6]))

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Find the second-smallest distinct number
# Easy–Medium · Time target: 15 minutes
# Input: [8, 3, 1, 3, 5, 1]
# Expected output: 3
# Constraint: No sort(), sorted(), min(), or max().

def second_smallest_number(numbers):
    smallest=None
    second_smallest=None
    for number in numbers:
        if smallest is None or number<smallest:
            second_smallest=smallest
            smallest=number
        elif smallest!=number and (second_smallest is None or number<second_smallest):
            second_smallest=number  
    return second_smallest
print(second_smallest_number([8, 3, 1, 3, 5, 1]))

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Move all zeros to the end
# Medium · Time target: 20 minutes
# Input: [0, 1, 0, 3, 12]
# Expected output: [1, 3, 12, 0, 0]
# Constraint: Preserve the relative order of non-zero elements.

def move_zero(numbers):
    pointer=0
    for i in range(len(numbers)):
        if numbers[i]!=0:
            numbers[pointer],numbers[i]=numbers[i],numbers[pointer]
            pointer+=1
    return numbers
print(move_zero([0,1,0,3,12]))


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Check whether a string is a palindrome using two pointers.
# A palindrome reads the same forward and backward.

def palindrome(str):
    left=0
    right=len(str)-1
    copy=list(str)
    while left<right:
        copy[left],copy[right]=copy[right],copy[left]
        left+=1
        right-=1
    copy="".join(copy)
    return str==copy
print("madam")

# complexity:
# time:O(n)
# space:O(n)

# OR

def is_palindrome(text):
    left=0
    right=len(text)-1
    while left<right:
        if text[left]!=text[right]:
            return False
        left+=1
        right-=1
    return True

print(is_palindrome("racecar"))  
print(is_palindrome("hello"))    
print(is_palindrome("abba"))     
print(is_palindrome(""))

# complexity:
# time:O(n)
# space:O(1)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------