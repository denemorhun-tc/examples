input_array = [1, 7, 4, 5, 200, 200, 200, 0, 9, 9, 9, 200,11, -66, 8]
target = 9

# Count how many numbers are greater than a threshold
# A list of numbers: [3, 7, 1, 9, 5, 12, 4]
# A threshold value: 6
# In this example, you would check each number to see if it’s greater than 6.

# Return the index of the largest number

# Find max from array
def find_largest_from_array(array):
    max_item = array[0]
    for i in range(len(array)):
        if array[i] > max_item:
            max_item = array[i]
    return max_item

#pythonic way
def find_max_from_array(array):
    current_max = array[0];
    for element in array:
        if element > current_max:
            current_max = element
    return current_max

def compute_sum_of_elements(array):
    current_sum =0
    for i in range(len(array)):
        current_sum += array[i]
    return current_sum

def count_the_even_numbers(array):
    even_count = 0
    for number in array:
        if ( number % 2) == 0:
            even_count +=1
    return even_count

# Remove duplicates
def remove_duplicates(array):
    array = set(array)
    return array

def remove_duplicates2(array):
    print(array)
    #Hint: Loop through the array and add items to a new list only if they haven’t appeared before.
    seen = {}
    # current_item = array[0]
    seen[array[0]] = 1
    for i in range(1, len(array)):
        if array[i] not in seen:
            seen[array[i]] = 1
        else:
            seen[array[i]] += 1
        i += 1
    return seen

def count_occurrences(array, target: int):
    print(array, target)
    lookup = {}
    for element in array:
        if element not in lookup:
            print(f"Initialize lookup for {element}")
            lookup[element] = 1
        else:
            print(f'increment count for element {element}')
            lookup[element] += 1
    return lookup.get(9)

# why does this work?
def reverse_array(array):
    array = array[::-1]
    return array

def find_min(array):
    min = array[0]
    for element in array:
        if element < min:
            min = element
    return min

def get_squares(array):
    return [x**2 for x in array]

def remove_negative(array):
    for element in array:
        if element <= 0:
            array.remove(element)
    return array

def move_non_zero_elements():
    array = [1, 0, 3, 0, 5]
    j = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[j] = array[i]
            j += 1
    for k in range(j, len(array)):
        array[k] = 0
    return array

def remove_ocurring_elements(val):
    # Problem: Remove all occurrences of val in-place from nums. Return the length of the new array.
    # Pattern: Two-pointer: overwrite valid elements to the front. One pointer (i) scans all values, and the other (j) overwrites only when a value ≠ val.
    array = [1, 3, 3, 1, 3, 1, 1, 9, 8, 1, 1]
    # output shoudl be 3
    val = 1 
    j=0
    # loop through the array and see if equal to 1
    for i in range(len(array)):
        print(f'i {i} j {j}')
        if array[i] != val:
            print(f'array[{i}] is not target value')
            # if not equal to 1, shift the value left
            array[j] = array[i] 
            print(f'array[{i}], i->{i} {array[i]} array[{j}], j->{j} {array[j]}')
            j += 1
    return j


    # def remove_occurrences_in_place(arr, value_to_remove):
    #     write_index = 0

    #     for read_index, value in enumerate(arr):
    #         if value != value_to_remove:
    #             arr[write_index] = value
    #             write_index += 1

    #     # Remove extra elements from the end
    #     while len(arr) > write_index:
    #         arr.pop()

    #     return write_index  # New length
    



# Problem:
# Given a list of numbers, move all even numbers to the front, preserving their relative order. Fill the rest with -1.
# Use the two-pointer approach: one for reading, one for writing.
    

def move_even_numbers_to_front():
    array = [1, 4, 5, 6, 7, 8, 9, 2222, 222, 2]

    # loop through array storing 2 indices
    # if value for current index == even, assign value to slow index
    #increment slow index

    # if even, assign value to the slow index
    j = 0
    for i in range(len(array)):
        if array[i] % 2 == 0:
            array[j] = array[i]
            j += 1

    # assign -1 to the rest of the array
    for k in range(j, len(array)):
        array[k] = -1

    return array

# print(move_even_numbers_to_front())

def separate_element(target):
    array = [0, 0, 0, 0, 0, 0, 0, 1]
    #scan array, if 0 is found, shift left
    #if not increment j, slow ticker
    j = 0
    filler = None

    for element in array:
        if element != target:
            filler = element
            break
  
    if filler == None:
        return array

    for i in range(len(array)):
        if array[i] == target:
            array[j] = array[i]
            j += 1

    for k in range (j, len(array)):
        array[k] = filler

    return array
    # add another loop from j to end of array and insert 1

# print(separate_element(1))
    
# Remove Duplicates from Sorted Array
# Given a sorted array nums, remove the duplicates in-place such that each element appears only once. Return the new length of the array.
# You must not use extra space; modify the input array in-place with O(1) extra memory.
def remove_duplicating_elements():
    array = [0, 1, 2,3, 4]

    #i -> fast index
    #j -> slow index
    j = 1
    # loop through array if different, that's a unique number.
    for i in range(len(array)):
        print(f'fast index i array[{i}] with value {array[i]} vs slow index j array[{j}] with value {array[j]}')
        if array[i] != array[j]:
            print('we found a new unique value')
            # assigned the value of i to slow index and move j to next
            j += 1
            array[j] = array[i]
        print(f'j is {j} now')

        # the length of the array has only gone to the j
    return j

# print(remove_duplicating_elements())
#print(remove_ocurring_elements(1))
# max_item = find_largest_from_array(input_array)
# print(f'max_item is {max_item}')
#sum_of_elements = compute_sum_of_elements(input_array)
# print(sum_of_elements)
# print(move_non_zero_elements())
# even_count = count_the_even_numbers(input_array)
# print(even_count)
# print(remove_duplicates2(input_array))
# print(f"Count for {target}", count_occurrences(input_array, target))
# print(reverse_array(input_array))
# print(find_min(input_array))
# print(get_squares(input_array))
# print(remove_negative(input_array))

# 1. Check if an Array is a Palindrome #
def check_palindrome(arr):
    left = 0
    right = len(arr)-1
    while left <= right:
        if arr[left] != arr[right]:
            return False
        else:
            left += 1
            right -= 1

    return True

# print(check_palindrome([1, 2, 5, 2, 1]))

def reverse_integer(n) -> int:
    
    reversed_int = 0
    while n > 0:
        reversed_int = reversed_int*10 + n % 10
        #removes last digit
        n //=10
    return reversed_int

print(reverse_integer(123455))


'''5. Count Pairs with a Given Sum (Sorted Array)
Problem:
Count the number of pairs in a sorted array that add up to a specific target.

Input: [1, 2, 3, 4, 5], target = 6
Output: 2 (pairs: 1+5, 2+4)'''

# use left, right and compare first with last, incrememt both. increase count.
def count_pairs(arr, target):
    
    count = 0
    left = 0
    right = len(arr) - 1

    while (left < right):
        total = arr[left] + arr[right]
        if (total == target):
            count += 1
            left +=1
            right -= 1
        elif (total < target):
            left +=1
        elif (total > target):
            right -= 1

    return count

print(count_pairs([1, 2, 3, 4, 5], 7))
print(count_pairs([1, 2, 3, 4, 5], 4))



        
        

'''3. Find the First Pair That Sums to a Target (Sorted Array)
Problem:
Given a sorted array and a target sum, find the first pair that adds to the target.

Input: [1, 2, 3, 4, 6], target = 7
Output: (1, 6)

Concept:
Start one pointer at the beginning, one at the end. Adjust based on the sum.'''

def buy_and_sell_stock(prices):
 # first 
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


# String to Integer (atoi) – Implement the atoi function to convert a string to an integer.

# Count and Say – Given a number n, generate the n-th term in the "count and say" sequence.

# Array Manipulation Questions
# Remove Duplicates from Sorted Array – Remove duplicates in-place and return the new length.

# Two Sum – Find two numbers in an array that add up to a target value.

# Best Time to Buy and Sell Stock – Find the maximum profit from buying and selling a stock (single transaction).
def maxProfit(prices) -> int:
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

# Plus One – Given a number represented as an array of digits, increment it by one and return the result as an array.

# Single Number – Find the number that appears only once in an array where every other number appears twice.

# Intersection of Two Arrays – Return the intersection of two arrays (unique common elements).

# Missing Number – Given an array containing n distinct numbers from 0 to n, find the missing one.
