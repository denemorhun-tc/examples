'''While loop and array studying:
✅ 1. Remove Duplicates from Sorted Array (Easy)
Given a sorted array, remove the duplicates in-place so that each element appears only once and return the new length.
⏱️ Involves: while loop, two pointers, index boundaries.'''

def remove_duplicates_return_length() -> int:
    arr = [1, 1, 2, 3, 4, 4, 5, 5]
    i = 0
    j = 1

    while i < len(arr)-1:
        if arr[i] != arr[i+1]:
            # print(f'i={i}, j={j}, arr[{i}] = {arr[i]}, arr[{j}] = {arr[j]}')
            arr[j] = arr[i+1]
            j +=1 
        # increment i always
        i += 1

    for k in range(j, len(arr)):
        arr[k] = 'x'  
    # print('final array', arr)
    return j

# print(remove_duplicates_return_length())

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

# print(check_if_sorted_ascending(arr))
# print(check_if_sorted_ascending(arr2))

'''
✅ 2. Move Zeroes (Easy)
Given an array nums, move all 0's to the end while maintaining the relative order of the non-zero elements.
⏱️ Involves: while loop (optional), index checks, swapping.
'''
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
⏱️ Uses: while loop or for loop with skipping logic and boundaries. Keep the values if arr[i] is not '''
def remove_element(target):
    arr = [12, 3, 4, 4, 6, 0, 99, 33, 99, 33]

    i = 0 #fast
    j = 0 #slow

    while i < len(arr):
        if arr[i] != target:
            arr[j] = arr[i]
            j += 1
        i += 1

    return j

print('Remove element', remove_element(4))

'''✅ 9. Find the Index of the First Occurrence in a String (Easy)
Implement strStr() to find the first occurrence of needle in haystack. Return the index or -1.
⏱️ Uses: boundary check in while/for, substring matching. “I loop through the haystack and check if the substring from the current index matches needle. To avoid out-of-bounds issues, I only loop while i <= len(haystack) - len(needle).” '''
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

# print(strStr('denem', 'em'))

'''TODOFind the Index of First Negative Number
Given a sorted array (may have negative and positive numbers), find the index of the first negative number using a while loop (with binary search).'''

def find_index_of_last_negative_number():
    arr = [1, 8, -4, 3, 3, 9, 0]

# print(find_index_of_last_negative_number())







# Binary search  using left, right, and mid on sorted array
def binary_search(target):
    arr = [1, 3, 5, 6, 7, 9, 11, 99]
    if target not in arr:
        return -1
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        # print(f'left = {left}, right = {right}, mid={mid}')
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
# if I see a 1, increase count
# if I see a 0, and if greater than max_count, set max_count and reset count, After the loop, check once more if the final streak was the longest, incase it ends with 1.

def max_consecutive_ones(arr):

    i = 0
    count = 0
    max_count = 0
    while i < len(arr):
        print(f'count {count}, max_count {max_count}')
        if arr[i] == 1:
            count += 1
        elif arr[i] == 0:
            if (count > max_count):
                max_count = count
            count = 0
        i += 1

    # extra check one more time if input ends with 1
    if (count > max_count):
        max_count = count
    return max_count

arrx = [1, 1, 0, 1, 1, 1, 1, 1]
print(max_consecutive_ones(arrx))
 
'''Check if Array is Sorted and Rotated

Find the Difference Between Element Sum and Digit Sum

Replace Elements with Greatest Element on Right Side'''
