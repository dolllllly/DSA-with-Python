# DSA Day 5 — Hashing Practice & Sliding Window Basics

# learning plan
    # Review hashing and frequency counting.
    # Learn the sliding window technique.
    # Solve array and string problems.
    # Practice LeetCode


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# revision hashing :
# hashing helps you find ,count or track elements efficiently using dictionaries and sets.
# example: count the frequency of each number.
def count_frequency(numbers):
    frequency={}
    for num in numbers:
        frequency[num]=frequency.get(num,0)+1
    return frequency
print(count_frequency([1,2,3,4,2,3,4]))

# output:
# {1: 1, 2: 2, 3: 2, 4: 2}
# average time complexity: O(n)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# what is sliding window?
# sliding window is a technique used to solve problems involving continious elements in an array or string.
# instead of calculating everything again for each group of elements, we move a window and update the reault.

# for example, given:
numbers=[2,1,5,1,3,2]
k=3
# find the maximum sum of any three consecutive elements

#  2        1       5       1       3       2
# window size=3
# first window: 2+1+5=8
# window sum:8

# slight right: remove 2 , add 1.sum=1+5+1=7
# window sum=7

# slight right : remove 1 and add 3. sum=5+1+3=9
# window sum=9

# slight right remove 5 , add 3 , sum=1+3+2=6
# windo sum=6

# the maximum sum is 9

# code of maximum sum of k consecutive elements

def max_window_sum(numbers,k):
    if k<=0 or k>len(numbers):
        return None
    window_sum=sum(numbers[:k])
    maximum_sum=window_sum
    for right in range(k,len(numbers)):
        window_sum+=numbers[right]
        window_sum-=numbers[right-k]
        maximum_sum=max(maximum_sum,window_sum)
    return maximum_sum
print(max_window_sum([2,1,5,1,3,2],3))

# output:
# 9

# how it works:
# 1. calculate the sum of the first k elements.
# 2. add  the new element entering the window .
# 3. substract the element leaving the widow.
# 4. update the maximum sum.

# time complexity: O(n)
# auxiliary space O(n)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# hashing problem ---Leetcode

# Contains Duplicate — 217

# Determine whether an array contains any repeated number

def contain_duplicate(numbers):
    if len(numbers)!=len(set(numbers)):
        return True
    return False
print(contain_duplicate([1,2,3,2,1,3]))

# output:
# True

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Valid Anagram — 242
# Check whether two strings contain the same letters with the same

def is_alangram(s,t):
    if len(s)!=len(t):
        return False
    frequency={}
    for ch in s:
        frequency[ch]=frequency.get(ch,0)+1
    for ch in t:
        if ch not in frequency:
            return False
        frequency[ch]-=1
        if frequency[ch]<0:
            return False
    return True
print(is_alangram("listen","silent"))
print(is_alangram("abb","baa"))


# output:
# True
# False


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                                        # coding practice

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Count elements greater than 5
# Input: [2, 6, 8, 1, 9, 3]. Expected output: 3.

def count_element_greater_then_5(numbers):
    count=0
    for ch in numbers:
        if ch>5:
            count+=1
    return count
print(count_element_greater_then_5([2,6,8,1,9,3]))

# output:
# 3

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Find the maximum sum of 2 consecutive elements
# Input: [4, 2, 7, 1, 8]. Expected output: 9

def max_sum_2consecutive_element(numbers):
    if len(numbers)<2:
        return None
    sum=numbers[0]+numbers[1]
    max_sum=sum
    for i in range(2,len(numbers)):
        sum+=numbers[i]
        sum-=numbers[i-2]
        max_sum=max(sum,max_sum)
    return max_sum
print(max_sum_2consecutive_element([4,2,7,1,8]))

# output:
# 9
    

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------