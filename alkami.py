#8. Remove Element from nums
def remove_element(arr, target):
    i = 0 #fast
    j = 0 #slow
    while i < len(arr):
        if arr[i] != target:
            arr[j] = arr[i]
            j += 1
        i += 1
    return j

# Merge Strings Alternately by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string. 
def merge_strs_alternately(word1, word2) -> str:
    result = []
    i, j = 0, 0
    while i < len(word1) or j < len(word2):
        if i < len(word1):
            result.append(word1[i])
            i += 1
        if j < len(word2):
            result.append(word2[j])
            j += 1
    return "".join(result)

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

# Remove All Duplicates from a String
# Given a string, remove all characters that appear more than once.
def remove_duplicates(s):
    # First pass: count character frequencies
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    # Second pass: keep only characters that appear once
    result = []
    for char in s:
        if char_count[char] == 1:
            result.append(char)
    return "".join(result)

# Maximum Subarray (Kadane) Find the contiguous subarray
# Input: [-2,1,-3,4,-1,2,1,-5,4] -> [4,-1,2,1] has the largest sum = 6)
#  1. Continue the current subarray (add current element to running sum)
 #   2. Start a new subarray from current element
def max_subarray_kadane(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    for i in range(1, len(nums)):
        # Either extend existing subarray or start new one
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

# Merge Sorted Array
# Given two sorted arrays, merge them into one sorted array in-place.
def merge_sorted_array(a1, a2):
    print('solve')

# Find All Numbers Disappeared in an Array
# Given an array of integers where 1 ≤ a[i] ≤ n, find all the elements that don't appear in the array.
def find_missing(nums):
    n = len(nums)
    num_set = set(nums)
    result = []
    for i in range(1, n + 1):
        if i not in num_set:
            result.append(i)
    return result

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

# Longest Common Prefix – Find the longest common prefix string among an array of strings. ["flower", "flow", "flight"]
# For each word in the list starting from the second: Compare it to your current prefix
# Find how many characters at the beginning are still the same
# Trim prefix to only that matching part
# If at any point prefix becomes an empty string, return "" right away
def longest_common_prefix(words):
    # Start with the first word as our prefix
    prefix = words[0]
    # Compare with each remaining word
    for i in range(1, len(words)):
        current_word = words[i]
        # Find how many characters match from the beginning
        j = 0
        while j < len(prefix) and j < len(current_word) and prefix[j] == current_word[j]:
            j += 1
        # Trim prefix to only the matching part
        prefix = prefix[:j]
        # If no common prefix, return empty string
        if prefix == "":
            return ""
    return prefix


# Remove Duplicates from Sorted Array – Remove duplicates in-place and return the new length.
def remove_duplicates2(array):
    seen = {}
    seen[array[0]] = 1 #initialize with first element
    for i in range(1, len(array)):
        if array[i] not in seen:
            seen[array[i]] = 1
        else:
            seen[array[i]] += 1
        i += 1
    return seen

# Best Time to Buy and Sell Stock – Find the maximum profit from buying and selling a stock (single transaction).
def buy_sell_stock(prices) -> int:
        # first day
        lowest_price_so_far = prices[0]
        #no profit on first date
        max_profit = 0
        for price in prices:
            #check prices everyday vs lowest price so far
            if price < lowest_price_so_far:
                lowest_price_so_far = price
            profit = price - lowest_price_so_far
            if profit > max_profit:
                max_profit = profit
        return max_profit

# Move Zeroes – Move all zeroes to the end of an array while maintaining the order of non-zero elements.
def move_zeroes(arr):
    i = 0 #read pointer, always increment
    j = 0 #write pointer
    while i < len(arr):
        if arr[i] != 0:
            arr[j] = arr[i]
            # only increment j when not equal to target
            j += 1
        i += 1
    for k in range(j, len(arr)):
        arr[k] = 0
    return arr

# Plus One – Given a number represented as an array of digits, increment it by one and return the result as an array.

# Single Number – Find the number that appears only once in an array where every other number appears twice.

# Intersection of Two Arrays – Return the intersection of two arrays (unique common elements).
def intersection(a1, a2):
    return set(a1) & set(a2)

# Rotate Array Right by K
def rotate_array_right_by_k(nums, k):
    n = len(nums)
    k %= n  # Handle cases where k is larger than the array length
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    # 1. Reverse the entire array.
    reverse(0, n - 1)
    print(nums)
    # 2. Reverse the first k elements.
    reverse(0, k - 1)
    print(nums)
    # 3. Reverse the remaining n-k elements.
    reverse(k, n - 1)

# Missing Number – Given an array containing n distinct numbers from 0 to n, find the missing one.

# Two sum
def two_sum(nums, target):
        seen = {}
        # loop through nums, if target - num is present, return i and the index of target - num.
        # if not present, store it for future use. 
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen.keys():
                return [seen[complement], i]
            else:
                seen[nums[i]] = i
        return None

# Group anagrams:
def groupAnagrams(strs):
        seen = {}
        for anag in strs:
            key = tuple(sorted(anag)) #can't use list as key
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

# Binary search  using left, right, and mid on sorted array
def binary_search(arr, target):
    if target not in arr:
        return -1
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1
        else:
            return mid
    return -1
