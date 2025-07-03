# String Manipulation Questions

'''✅ 8. Remove Element (Easy)
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
⏱️ Uses: while loop or for loop with skipping logic and boundaries. Keep the values if arr[i] is not '''
def remove_element(target):
    i = 0 #fast
    j = 0 #slow
    while i < len(arr):
        if arr[i] != target:
            arr[j] = arr[i]
            j += 1
        i += 1
    return j

#Merge Strings Alternately
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string. Use two pointers for this problem. 
def merge_strs_alternatively(word1, word2) -> str:
        short_length = min(len(word1), len(word2))
        merge = []
        for i in range(short_length):
            merge.append(word1[i])
            merge.append(word2[i])
        if len(word1) > short_length:
            merge.append(word1[short_length:])
        if len(word2) > short_length:
            merge.append(word2[short_length:])
        return "".join(merge)

# strStr(): Return the index of the first occurrence of a substring in a string. If not found, return -1.
def strStr(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    i = 0
    slice = len(needle)
    while i < len(haystack):
        if haystack[i] == needle[0]:
            if haystack[i:i+slice] == needle:
                return i
        i += 1
    return -1

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

# the idea is to have left of the string less than right, 
# and keep swapping O(1) space, O(n) with while loop
def reverse_string_inplace(s):
    left = 0
    right = len(s) - 1

    while (left < right):
        s[right], s[left] = s[left], s[right]
        print(f's is now {s}')
        left += 1
        right -= 1
    return "".join(s)

# Valid Palindrome – Check if a string is a palindrome (ignoring non-alphanumeric characters and case).
#again try the left / right method, one pointer increasing other decreasing

def check_valid_palindrome(s):
    arr = list(s)
    left = 0
    right = len(arr) - 1
    while (left < right):
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True


        

# Remove wovels, loop through each character, if vowel, skip
def remove_vowels(s):
    s = list(s)
    vowels = set("aeiouAEIOU")
    redux_str = []
    for letter in s:
        if letter not in vowels:
            redux_str.append(letter)
    return "".join(redux_str)

# First Unique Character – Given a string, find the first non-repeating character and return its index.
# Count frequency of each character (collections.Counter or a dict)
# Loop through string again, check which character has count 1
# Return its index
def first_unique_char(s):
    seen = {}
    for i in range(len(s)):
        if s[i] not in seen:
            seen[s[i]] = 1
        else:
            seen[s[i]] += 1

    for i in range(len(s)):
        if seen[s[i]] == 1:
            return i
    return -1

# print(first_unique_char('yarrayerring'))
# print(first_unique_char('aabbcc'))


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

    #initialize or increase each occurrence
    for i in range(len(first)):
        if first[i] not in count:
            count[first[i]] = 1
        else:
            count[first[i]] += 1

    #if any letter not found is present not anagram
    for i in range(len(second)):
        if second[i] not in count:
            return False
        else:
            #decrease occurrence
            count[second[i]] -= 1

    # if any occurrence is more than 1, not an anagram
    for a in count.values():
        if a > 0:
            return False
        
    return True
                   
# print(check_anagram_dict('dude', 'dudr'))


# Longest Common Prefix – Find the longest common prefix string among an array of strings. ["flower", "flow", "flight"]
# For each word in the list starting from the second:
# Compare it to your current prefix
# Find how many characters at the beginning are still the same
# Trim prefix to only that matching part
# If at any point prefix becomes an empty string, return "" right away
def common_longest_prefix():
    a = ["flour","flow", "flower", "flo", "flowering"]
    if not a:
        return ""
    
    prefix = a[0]

    for i in range(1, len(a)):
        #length of the prefix
        j = 0
        while j < len(prefix) and j < len(a[i]) and a[i][j] == prefix[j]:
            j += 1

        prefix = prefix[:j]
        if prefix == "":
            return ""
       
    return prefix

# print(common_longest_prefix())


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

# Two sum
def two_sum(nums, target):
        seen = {}
        # loop through nums
        # if target - num is present, you've found match. return i and the index of target - num. 
        # if not present, store it for future use. 
        for i in range(len(nums)):
            if target - nums[i] in seen.keys():
                return [seen[target - nums[i]], i]
            else:
                seen[nums[i]] = i
        return None

# Group anagrams:
def groupAnagrams(strs):
        seen = {}
        for anag in strs:
            key = tuple((sorted(anag)))
            if key not in seen.keys():
                seen[key] = [anag]
            else:
                seen[key].append(anag)
        return list(seen.values())

#balance paranthesis
def paranthesis_is_valid(s):
    stack = []
    opening = ('(', '{', '[')
    closing = (')', '}', ']')
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            # must check to see if matching pair
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack


#group_strings- check diff between chars for key, group using dict
def group_shifted_strings(strings):
    groups = {}
    for s in strings:
        key = ""
        for i in range(1, len(s)):
            diff = (ord(s[i]) - ord(s[i - 1])) % 26
            key += str(diff)  # just digits
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())

