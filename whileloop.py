'''While loop and array studying:
✅ 1. Remove Duplicates from Sorted Array (Easy)
Given a sorted array, remove the duplicates in-place so that each element appears only once and return the new length.
⏱️ Involves: while loop, two pointers, index boundaries.'''

def remove_duplicates_return_length():
    a = [1, 1, 2, 3, 4, 4, 5, 5]
    # i is the fast index, j is the slow index
    i, j = 0, 1

    while i < len(a) and j < len(a):
        print(f'i={i} a[{i}] = {a[i]}, j={j} a[{j}] = {a[j]}')
        if a[i] != a[j]:
            a[i] = a[j]
            j = i
        i += 1
    return j

#print(remove_duplicates_return_length())

def reverse_array():
    arr = [3, 5, 2, 9]
    i = len(arr)-1
    while i >= 0:
        i -= 1
reverse_array()

def sum_of_array():
    arr = [1, 2, -8, 9999]
    i = 0
    total = 0
    while i < len(arr):
        total += arr[i]
        i += 1
    return total

# print(f'sum of array {sum_of_array()}')

def find_first_even():
    arr = [1, 3, 5, 7, 9, 9, 6]
    i = 0
    while i < len(arr) and arr[i] % 2 != 0:
        i += 1

    if i < len(arr):
        return arr[i]
    else:
        return None

# print(find_first_even())

def find_how_many_are_greater_than(target):
    arr = [0, 1, 4, 6, 7, 44, 5, 6,25252, 67, 53, 4]
    i = 0
    count = 0
    while i < len(arr):
        if arr[i] > target:
            count += 1
        i += 1
    return count

# print(find_how_many_are_greater_than(5))

def check_if_sorted_ascending(arr):
    i = 0
    while i < len(arr)-1:
        if arr[i] > arr[i+1]:
            return False
        i += 1
    return True

arr = [0, 2, 4, 5, 6, 7, 8, 9]
arr2 = [9, 4, 3, 8, 1]

print(check_if_sorted_ascending(arr))
print(check_if_sorted_ascending(arr2))

'''
✅ 2. Move Zeroes (Easy)
Given an array nums, move all 0's to the end while maintaining the relative order of the non-zero elements.
⏱️ Involves: while loop (optional), index checks, swapping.
'''

def move_zeroes(arr):
    i = 0 #write pointer
    j = 0 #read pointer
    while j < len(arr):
        print(arr)
        if arr[j] != 0:
            arr[i] = arr[j]
            # increment write pointer, where the next non-zero element should go
            i += 1
        j += 1
    for replace in range(i, len(arr)):
        arr[replace] = 0
    return arr

# print(move_zeroes([0, 0, 9, 8, 0, 4, 0 ,3, 0]))

'''
✅ 3. Squares of a Sorted Array (Easy)
Given a sorted array of integers, return a new array with the squares of each number, also sorted.
⏱️ Involves: two-pointer approach with while loop and edge handling. '''

def square_of_array():
    arr = [1, 4, 5, 6, 7, 0]
    #return [x * x for x in arr]
    #return [x**2 for x in arr]

    i = 0
    while i < len(arr):
        arr[i] = arr[i]**2
        i += 1
    return arr
# print(square_of_array())


'''✅ 5. Reverse a String In-Place (Easy)
Write a function that reverses a string. The input string is given as a char array.
⏱️ Involves: while loop with left < right boundary.'''
def reverse_string_another_way(string):
    arr = list(string)
    left = 0
    right = len(arr)-1
    while (left < right):
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -= 1
    return "".join(arr)
# print(reverse_string_another_way('denem'))

'''✅ 6. Valid Palindrome (Easy)
Return true if the given string is a palindrome, considering only alphanumeric characters and ignoring cases.
⏱️ Uses: while loop with left/right boundaries, isalpha() and lower(). '''

def valid_palindrome(string):

    if len(string) == 0 or len(string) == 1:
        return True
    
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True

# print(valid_palindrome('yarrak'))
    
'''✅ 7. Merge Sorted Arrays (Easy)
Given two sorted arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
⏱️ Uses: while loop, edge cases, pointers.'''

'''✅ 8. Remove Element (Easy)
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
⏱️ Uses: while loop or for loop with skipping logic and boundaries.'''
# def remove_element(target):
#     arr = [12, 5, 3, 4, 5, 6, 0, 99, 33]

#     i = 0
#     while i < len(arr):

'''✅ 9. Find the Index of the First Occurrence in a String (Easy)
Implement strStr() to find the first occurrence of needle in haystack. Return the index or -1.
⏱️ Uses: boundary check in while/for, substring matching. '''

def strStr(haystack: str, needle: str) -> int:
    i= 0
    slice = len(needle)-1
    while i < len(haystack)-1:
        if haystack[i] == needle[0]:
            print(f'found a matching char')
            print(f'haystack[i:i+slice] {haystack[i:i+slice]}')
            if haystack[i:i+slice] == needle:
                return i
        i += 1
    return -1

print(strStr('denem', 'e'))

'''Find the Index of First Negative Number
Given a sorted array (may have negative and positive numbers), find the index of the first negative number using a while loop (with binary search).'''
def find_index_of_last_negative_number():
    arr = [1, 8, -4, 3, 3, 9, 0]
    i = len(arr) - 1
    while i >= 0:
        if arr[i] < 0:
            return i
        i -= 1
    return -1
# print(find_index_of_last_negative_number())

# Binary search  using left, right, and mid on sorted array
def binary_search(target):
    arr = [1, 3, 5, 6, 7, 9, 11, 99]
    if target not in arr:
        return -1
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        print(f'left = {left}, right = {right}, mid={mid}')
        if target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1
        else:
            return mid
    return -1
# print(binary_search(99))

# 10. Maximum Consecutive Ones (Easy)
# Given a binary array, find the maximum number of consecutive 1s.
# ⏱️ Uses: while loop to count consecutive 1s and reset on 0.



