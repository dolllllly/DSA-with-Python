# DSA Day 4 — Hashing and Dictionaries

# today's topic:
    # Hashing and hash tables
    # Python dictionaries (dict)
    # Python sets (set)
    # Dictionary and set operations
    # Time complexity: Average O(1)
    # Frequency counting
    # Duplicate detection
    # Two Sum using hashing
    # First repeated element
    # Frequency comparison
    # LeetCode 1: Two Sum

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# what is hashing?
# Hashing is a technique that uses a hash function to help organize and locate data efficiently
# It is especially useful when you need to check whether an element exists, count occurrences, or find duplicates

# why do we need hashing?
# Suppose you have this list:
numbers = [10, 20, 30, 40, 50]

# You want to check whether 40 exists.
# Using Linear Search, you may need to check each element until you find 40. This takes O(n) time in the worst case.
# With a hash-based data structure, checking for an element takes O(1) average time



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# hashing in python: dict and set:

# python dictionaries:
# create a dictionary
student={
    "name":"Dolly",
    "age": 20,
    "marks":89
}

# here "name", "age", "marks" are keys . "Dolly", 20, and 89 are their values.

# access values:

print(student["name"])
print(student.get("marks"))
print(student.get("gread","not available"))

# output:
# Dolly
# 89
# not available

# Important difference:
    # student["grade"] raises a KeyError if the key is missing.
    # student.get("grade") returns None by default.
    # student.get("grade", "Not available") returns the supplied default.


# add and update values:

student={
    "name":"Dolly",
    "age": 20,
    "marks":89
}

student["gread"]="B"
student["marks"]=90
student["city"]="Banglore"
print(student)

# output:
# {'name': 'Dolly', 'age': 20, 'marks': 90, 'gread': 'B', 'city': 'Banglore'}


# Check whether a key exist

if "marks" in student:
    print("marks are available")
# in checks dictionary keys , not values

# output:
# marks are available


# loop through a dicyionary:

for key,value in student.items():
    print(key,value)

# output:
# name Dolly
# age 20
# marks 90
# gread B
# city Banglore


# other useful methods:

# student.keys() : get keys
print(student.keys())

# output:
# dict_keys(['name', 'age', 'marks', 'gread', 'city'])



#  student.values()  : get values
print(student.values())

# output
# dict_values(['Dolly', 20, 90, 'B', 'Banglore'])


# student.items()  : get key-value pairs
print(student.items())

# output:
# dict_items([('name', 'Dolly'), ('age', 20), ('marks', 90), ('gread', 'B'), ('city', 'Banglore')])



# student.pop("age")    : remove a key and return its value
print(student.pop("age"))

# output:
# 20

# len(student)  : count kry-value pairs
print(len(student))

# output:
# 4


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# python sets
# a set stores unique elements.

numbers=[1,2,2,3,2,3,4,5,5]
unique_number=set(numbers)
print(unique_number)

# output:
# {1, 2, 3, 4, 5}

# Sets are useful when you want to check whether an element has already appeared
 
seen=set()
seen.add(10)
seen.add(20)
seen.add(10)
print(10 in seen)
print(seen)

# output:
# True
# {10, 20}


# common operation:
a={1,2,3}
b={3,4,5}

print(a|b)   #union
print(a&b)    #intersection
print(a-b)    #difference

# output:
# {1, 2, 3, 4, 5}
# {3}
# {1, 2}
 
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# time complexity:

# dictionary lookup   : O(1)
#  dictionary insertation: O(1)
#  dictionary deletion : O(1)
# set membership check : O(1)
# traversing all dictionary entries : O(n)

# These are average-case complexities . in unusual collisuon-heavy casw, dictionary or set operations can take O(n).

# Hashing often trades extra memory for faster operations


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                            # coding exercises

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# count frequency:
# given: 
# numbers=[1,2,2,3,1,2,4]

def count_frequency(numbers):
    frequency={}
    for number in numbers:
        if number in frequency:
            frequency[number]+=1
        else:
            frequency[number]=1
    return frequency
print(count_frequency([1,2,2,3,1,2,4]))

# output:
# {1: 2, 2: 3, 3: 1, 4: 1}

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# find duplicate:
# given:
# numbers = [1, 2, 3, 2, 4, 1, 5]

def find_duplicate(numbers):
    seen=set()
    duplicates=set()
    for number in numbers:
        if number not in seen:
            seen.add(number)
        else:
            duplicates.add(number)
    return list(duplicates)
print(find_duplicate([1, 2, 3, 2, 4, 1, 5]))

# output:
# [1, 2]


# to find the first duplicate number:

def find_duplicate(numbers):
    seen=set()

    for number in numbers:
        if number in seen:
            return number
        else:
            seen.add(number)
print(find_duplicate([1, 2, 3, 4, 1, 5]))

# output:
# 1


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Two Sum : Leetcode :number 1
# numbers = [2, 7, 11, 15]
# target = 9

def two_sum(numbers,target):
    dictionary={}
    for index , number in enumerate(numbers):
        complement=target-number
        if complement in dictionary:
            return [dictionary[complement],index]
        dictionary[number]=index
    return []
        
     
print(two_sum([2,7,11,15],9))





# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# First repeated element

def first_repeated_element(numbers):
    seen=set()
    for number in numbers:
        if number in seen:
            return number
        else:
            seen.add(number)
    return None
print(first_repeated_element([5,3,4,3,5,6]))

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Check whether two arrays have the same elements with the same frequencies


def check_two_array():
    def two_array(array):
        dictionary1={}
        for i in array:
            if i in dictionary1:
                dictionary1[i]+=1
            else:
                dictionary1[i]=1
        return dictionary1
    a=two_array([1,2,2,3])
    b=two_array([2,1,3,2])
    return a==b
print(check_two_array())
    