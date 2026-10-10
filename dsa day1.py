# DSA Day 1 — Foundations with Python

# Today's topics
    # DSA basics
    # Big-O 
    # arrays
    # traversal 
    # linear search

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# what is DSA?

# DSA= Data Structure + Algorithms
    # Data Structure: How data is stored and organized
    # Algorithm: A step-by-step method to solve a problem.
    # DSA is the study of data structures used to organize data and algorithms used to solve problems efficiently. It helps optimize the time and memory required by a program


# example: 
# supose you have these marks:
marks=[65,97,72,95,81]
# the list is the data atructure. the steps you use to find the highest mark are the algorithm.

# why learn DSA?
    # build logical thinking and problem-solving ability.
    # write efficient code
    # prepare for technical interviews.
    # understand the algorithm used in real software and AI systems

# common data structures:

        # Array / Python list:  Store ordered items
        # String:  Store text
        # Hash map / Python dictionary:  Store key-value pairs
        # Stack:  Last In, First Out (LIFO)
        # Queue:  First In, First Out (FIFO)
        # Linked list:  Connect nodes in sequence
        # Tree:  Represent hierarchical data
        # Graph:  Represent connected objects

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\

# Time complexity and Big-O
# Time complexity describes how an algorithm's work grows as the input size n increases. It does not simply mean the number of seconds a program takes.

# learn these complexities first:
# complexity 
#                      
# O(1)  :  constant
# example: access a list item by index
numbers=[1,2,3,4,5]
print(numbers[2])
# only one indexed is performed , regardless of the list's size.

# O(log n)  : Logarithmic
# example: binary search on sorted data

# O(n)  : Linear
# example: Traverse a list once
numbers=[1,2,3,4,5]
for i in numbers:
    print(i)
# if there are 5 time , the loop run 4 times. if there are 1000 times, it run 1000 times.


# O(n log n)  : linearithmic 
# example: efficient comparision sorting

# O(n²)  : quadratic 
# example: compare every pair using nested loops
numbers=[1,2,3]
for first in numbers:
    for second in numbers:
        print(first,second)
# for n=3 ,the inner statement executes 9 times. in general, it execute n² times.
    

# Big-O dry-run challenge: Predict the output and time complexity
for i in range(5):
    print(i)

# time complexity:O(n)
# DSA rule: If a loop runs n times, its time complexity is generally O(n). If the number of iterations is fixed, like 5, it is O(1)



# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# space complexity:
# space complexity measure how memory usage grow with inpit size.
# example:
def get_first(numbers):
    return numbers[0]
# this function uses O(1) auxiliary space: it doesn't create another collection that grows with the input.

# example: linear space O(n)
def mak_squares(numbers):
    result=[]
    for number in numbers:
        result.append(number**2)
    return result
# the new result list grows with the input size, so the auxiliary space is O(n).

# Example: Quadratic space  O(n²)
def create_matrix(n):
    matrix = []

    for i in range(n):
        row = []

        for j in range(n):
            row.append(0)

        matrix.append(row)

    return matrix
# The matrix has n rows. Each row has n elements.Total stored elements = n×n=n²



# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Arrays using Python lists
# In Python, we commonly use lists to practise array problems


numbers=[10,20,30,40,50]

# Index positions

# 10  -Index 0
# 20  -Index 1
# 30  -Index 2
# 40  -Index 3
# 50  -Index 4
# Python indexing starts at 0, not 1.

# important operations
numbers=[1,2,3,4,5]
print(numbers[0])  #10: access
numbers[1]=25       #update
numbers.append(60)   #add
numbers.pop()        #remove last item
print(len(numbers))   #length


# typical python list operation costs:
# operation                                                         typical complexity
    # access by index                                                    O(1)
    # update by index                                                    O(1)
    # search by value                                                    O(n)
    # append at the end                                                  O(1)amortixed
    # insert at the beginning                                            O(n)



# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# array traversal 
# tracersal mean visiting each element one by one

# method: direct traversal
numbers=[1,2,3,4,5]
for number in numbers:
    print(number)

# method 2: index base traversal
numbers=[1,2,3,4,5]
for i in range(len(numbers)):
    print(i,numbers[i])

# use direct traversal when you only need the values. use index-based traversal when you also need the positions.


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# linear search
# linear search checks elements one at a time until it find the target or reaches the end.

# question:
# try a linear search
# list:[10,20,30,40,50]
# target=30 ,index

def linear_search(numbers,target):
    for i in range(len(numbers)):
        if numbers[i]==target:
            return i
    return -1
numbers=[10,20,30,40,50]
print(linear_search(numbers,30))
print(linear_search(numbers,99))

# output:
# 2
# -1

#    Why return -1? Because valid list indices start at 0, so -1 is a convenient signal that the target wasn't found # 

# best case: O(1)- the first element matches
# worst case O(n)- the target is last or absent
# auxiliary space O(1)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                            # coding practice:
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# find the maximum:
    # Input: [4, 9, 2, 7] → Output: 9

def maximum(numbers):
    max=numbers[0]
    for i in numbers:
        if i>max:
            max=i
    return max
numbers=[4,9,2,7]
print(maximum(numbers))

# time complexity: O(n)
# space complexity: O(1)


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Find the minimum
    # Input: [4, 9, 2, 7] → Output: 2

def minimum(numbers):
    min=numbers[0]
    for i in numbers:
        if i<min:
            min=i
    return min
numbers=[4,9,2,7]
print(minimum(numbers))

# time complexity: O(n)
# space complexity: O(1)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Calculate the sum
    # Input: [1, 2, 3, 4] → Output: 10

def sum(numbers):
    sum=0
    for i in numbers:
        sum+=i
    return sum
numbers=[1,2,3,4]
print(sum(numbers))

# time complexity: O(n)
# space complexity: O(1)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Count occurrences
    # Count how many times 2 appears in [2, 5, 2, 7, 2]. Output: 3

def count_occurance(numbers,target):
    count=0
    for i in numbers:
        if i==target:
            count+=1
    return count
numbers=[2, 5, 2, 7, 2]
print(count_occurance(numbers,2))

    
# time complexity: O(n)
# space complexity: O(1)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Linear search
    # Return the index of a target, or -1 if absen

def linear_search(numbers,target):
    for i in range(len(numbers)):
        if numbers[i]==target:
            return i
    return -1
numbers=[10,20,30,40]
print(linear_search(numbers,30))
print(linear_search(numbers,99))

# time complexity: O(n) in the worst case.
# space complexity: O(1)


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# leetcode-my first problem:
# Running Sum of 1d Array
# Easy Problem 1480
# Given an array nums, return an array where each position contains the sum of all elements up to that position


def running_sum(numbers):
    result=[]
    for i in range(len(numbers)):
        if i==0:
            result.append(numbers[i])
        if i>0:
            result.append(numbers[i]+numbers[i-1])
    return result
number=[1,2,3,4]
print(running_sum(number))

# proper leetcode 
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        self.nums=nums
        self.result=[]
        for i in range(len(self.nums)):
            if i==0:
                self.result.append(self.nums[i])
            if i>0:
                self.result.append(self.nums[i]+self.result[i-1])
        return self.result
obj=Solution()
print(obj.runningSum([1,2,3,4]))

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Second-largest distinct number


def second_largest_num(numbers):
    largest=None
    second_largest=None
    for number in numbers:
            if largest is  None or number>largest:
                  second_largest=largest
                  largest=number
            elif number!=largest and (second_largest is None or number>second_largest):
                  second_largest=number
            if second_largest is None:
                  return f'no second-largest distinct number'
    return second_largest
print(second_largest_num([5,5,5,5]))


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
