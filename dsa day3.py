# DSA Day 3 — Binary Search

# Today's goals:
    # Understand binary search and its complexity.
    # Implement it iteratively in Python.
    # Learn how to dry-run pointer changes.
    # Solve practice problems and a LeetCode question

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Linear search vs. binary search
# Suppose we have this sorted array:
# we want to find 23.
# linear search: 
            # checks elements one by one.
# Binary search:
            # checks the middle element and eliminates half of the remaining search range.

# linear search algorithm : 
        # time complexity O(n)
        # sorted array not requires

# binary search algorithm:
        # time complexity O(log n)
        #  data must be sorted for he standard algorithm


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# how binary search works:

# example:
# target : 23

[2    ,   5    ,   8   ,    12  ,    16  ,    23  ,    38   ,   56   ,   72]

# 0       1       2          3       4        5        6         7      8

# step 1: missle index is 4. the middle value is 16. since 23>16, it search the right half

23    ,  38   ,   56  ,    72

# 5       6        7        8

# step 2: the new middle is 6 . the value is 38 . since 23<38, search the left half

23

# 5
# step3: the middle value is 23. target found at index 5


# rebember the three important variables:
    # low: beginning of the search range.
    # high: end of the search range.
    # mid: middle index, calculated from low and high.



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# implement binary search in python
# study these code and trace the value of low, high, and mid

def binary_search(numbers,target):
    low=0
    high=len(numbers)-1
    while low<=high:
        mid=(low+high)//2
        if numbers[mid]==target:
            return mid
        elif numbers[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
numbers=[2,3,8,12,16,23,28,56,72]
print(binary_search(numbers,23))
print(binary_search(numbers,10))

# output:
# 5
# -1

# understand these lines:

# mid=(low+high)//2
        # the // operator performs integer division, giving a valid integer index.

# low=mid+1
        # if the middle value is smaller than the target, discard the middle and everithing to its left.

# high=mid-1
        # if the middle value is larger than the target, discard the middle and everithing to its right.

# return -1
        # the target does not exist in the array.

# important:
        # binary search requires sorted input. if the list is unsorted, this implementation can return the wrong result.


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#                                                                     coding practice
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Search Insert Position : LeetCode 35 · Easy

# Input: numbers = [1, 3, 5, 6], target = 2
# Expected output: 1
# Return the index where the target exists, or where it should be inserted to keep the array sorted.

def search_insert_position(numbers,target):
    low=0
    high=len(numbers)-1
    while low<=high:
        mid=(low+high)//2
        if numbers[mid]==target:
            return mid
        elif numbers[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return low
print(search_insert_position([1,3,5,6],2))
print(search_insert_position([1,3,5,6],6))
print(search_insert_position([1,3,5,6],0))

# output:
# 1
# 3
# 0

# or


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        self.num=nums
        self.target=target
        high=len(self.num)-1
        low=0
        while low<=high:
            mid=(low+high)//2
            if self.num[mid]==self.target:
                return mid
            elif self.num[mid]<self.target:
                low=mid+1
            else:
                high=mid-1
            
        return low

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# First and last occurrence : Leetcode 34 medium:
# Input: numbers = [1, 2, 2, 2, 3, 4], target = 2
# Expected output: [1, 3]
# Find the first and last indices of the target. Challenge yourself to achieve O(logn) time.


def search_first_last(numbers,target):
    def find_occurrence(find_first):
        low=0
        high=len(numbers)-1
        answer=-1
        while low<=high:
            mid=(low+high)//2
            if numbers[mid]==target:
                answer=mid
                if find_first:
                    high=mid-1
                else:
                    low=mid-1
            elif numbers[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return answer
    first=find_occurrence(True)
    last=find_occurrence(False)
    return[first,last]
print(search_first_last([1,2,2,2,2,2,2,3,4],2))

# OR

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        self.nums=nums
        self.target=target
        def find_occurance(find_first):
            high=len(self.nums)-1
            low=0
            answer=-1
            while low<=high:
                mid=(high+low)//2
                if self.nums[mid]==self.target:
                    answer=mid
                    if find_first:
                        high=mid-1
                    else:
                        low=mid+1
                elif self.nums[mid]<self.target:
                    low=mid+1
                else:
                    high=mid-1
            return answer
        first=find_occurance(True)
        last=find_occurance(False)
        return [first,last]
obj=Solution()
print(obj.searchRange([5,7,7,8,8,10],8))


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Binary search edge cases

# Test your implementation on:

# numbers = [], target 5 → -1
# numbers = [7], target 7 → 0
# numbers = [7], target 2 → -1
# numbers = [1, 3, 5, 7, 9], target 9 → 4


def search_insert_position(numbers,target):
    low=0
    high=len(numbers)-1
    while low<=high:
        mid=(low+high)//2
        if numbers[mid]==target:
            return mid
        elif numbers[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

print(search_insert_position([],5))
print(search_insert_position([7],7))
print(search_insert_position([7],-1))
print(search_insert_position([1,3,5,7,9],9))


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------