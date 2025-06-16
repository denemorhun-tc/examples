# String Manipulation Questions

# Implement strStr()
# Return the index of the first occurrence of a substring in a string. If not found, return -1.

# Ransom Note
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine.

# Check if Two Strings are Anagrams
# Given two strings, determine if they are anagrams of each other.

# Remove All Duplicates from a String
# Given a string, remove all characters that appear more than once.

# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# Maximum Subarray (Kadane’s Algorithm)
# Find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Two Sum
# Given an array of integers and a target, return the indices of the two numbers that add up to the target.

# Move Zeroes
# Move all 0's to the end of the array while maintaining the relative order of the non-zero elements.

# Find All Numbers Disappeared in an Array
# Given an array of integers where 1 ≤ a[i] ≤ n, find all the elements that don't appear in the array.

# Remove Element
# Given an array and a value, remove all instances of that value in-place and return the new length.

# Merge Sorted Array
# Given two sorted arrays, merge them into one sorted array in-place.


# Reverse a String – Given a string, return the reversed string.
def reverse_string():
    denem = 'denem'
    return denem[::-1]

# this creates a new array.
def reverse_string_2point(str):
    v = list(str)
    i = len(v) - 1
    newStr = []
    while i >= 0:
        newStr.append(v[i])
        i -= 1

    return "".join(newStr)

# print(reverse_string_2point('denem'))

# the idea is to have left of the string less than right, 
# and keep swapping O(1) space, O(n) with while loop
def reverse_string_inplace(str):
    arr = list(str)
    left = 0
    right = len(arr) - 1
    temp = ""

    while (left < right):
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
    
    return "".join(arr)

# print(reverse_string_inplace('dinosaur'))


# Valid Palindrome – Check if a string is a palindrome (ignoring non-alphanumeric characters and case).
#again try the left / right method, one pointer increasing other decreasing

def check_valid_palindrome(s):
    arr = list(s)
    left = 0
    if len(arr) == 0:
        return True
    if not arr:
        return True
    right = len(arr) - 1
    while (left < right):
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1

    return True

assert check_valid_palindrome('madam') == True
# print(check_valid_palindrome('madam'))
assert check_valid_palindrome('denem') == False, 'returns false for non palindrome'
# print(check_valid_palindrome('denem'))
assert check_valid_palindrome("madam") == True
assert check_valid_palindrome("racecar") == True
assert check_valid_palindrome("ege") == True
assert check_valid_palindrome("hello") == False
assert check_valid_palindrome("") == True
assert check_valid_palindrome("a") == True
        

# Remove wovels, loop through each character, if vowel, skip
s = 'denemsaurus'
def remove_vowels(s):
    s = list(s)
    vowels = set("aeiouAEIOU")
    redux_str = []
    for letter in s:
        if letter not in vowels:
            redux_str.append(letter)
        
    print(redux_str)
    return "".join(redux_str)

# print(remove_vowels(s))

# First Unique Character – Given a string, find the first non-repeating character and return its index.
# Count frequency of each character (collections.Counter or a dict)
# Loop through string again, check which character has count 1
# Return its index
def first_unique_char(s):
    seen = {}
    for i in range(len(s)):
        print(f's[{i}] -> {s[i]}')
        if s[i] not in seen:
            seen[s[i]] = 1
        else:
            seen[s[i]] += 1

    print(seen)
    for i in range(len(s)):
        if seen[s[i]] == 1:
            return i

    return -1

print(first_unique_char('yarrayerring'))
print(first_unique_char('aabbcc'))


# Anagram Check – Determine if two strings are anagrams of each other.

def check_anagram(first, second): 
    # O(nlogn) due to sort for long strings
    if sorted(first) == sorted(second):
        return True
    else:
        return False
assert(check_anagram('eren', 'nere')) == True

#You build two separate loops for first and second that do the same thing. You can DRY (Don’t Repeat Yourself) by making a helper function to count frequencies or using one dictionary that adds counts for the first string and subtracts for the second.\What does work well is treating the counts like a stack of character frequencies:
# Use a dictionary to increment counts for the first string
# Then decrement counts for the second string
# Finally check if all counts are zero

def check_anagram_dict(first, second):

    if (len(first)) != len(second):
        return False
    count = {}

    for i in range(len(first)):
        if first[i] not in count:
            count[first[i]] = 1
        else:
            count[first[i]] += 1

    for i in range(len(second)):
        if second[i] not in count:
            return False
        else:
            count[second[i]] -= 1

    for a in count.values():
        if a > 0:
            return False
        
    return True
                   
print(check_anagram_dict('dude', 'dudr'))


# Longest Common Prefix – Find the longest common prefix string among an array of strings. ["flower", "flow", "flight"]
# You need to find the longest string prefix that is common to all the strings in the array.
# 🔹 What is a "prefix"?
# A prefix is the beginning of a word. For example
# The prefix of "flight" could be "f", "fl", "fli", etc.
# "fl" is a prefix of "flower", "flow", and "flight".

# String to Integer (atoi) – Implement the atoi function to convert a string to an integer.

# Count and Say – Given a number n, generate the n-th term in the "count and say" sequence.

# Array Manipulation Questions
# Remove Duplicates from Sorted Array – Remove duplicates in-place and return the new length.

# Two Sum – Find two numbers in an array that add up to a target value.

# Best Time to Buy and Sell Stock – Find the maximum profit from buying and selling a stock (single transaction).

# Move Zeroes – Move all zeroes to the end of an array while maintaining the order of non-zero elements.

# Plus One – Given a number represented as an array of digits, increment it by one and return the result as an array.

# Single Number – Find the number that appears only once in an array where every other number appears twice.

# Intersection of Two Arrays – Return the intersection of two arrays (unique common elements).

# Missing Number – Given an array containing n distinct numbers from 0 to n, find the missing one.

# These questions cover key concepts like iteration, hash maps, two-pointer techniques, and basic algorithm design, which are common in SDET/QA interviews.
