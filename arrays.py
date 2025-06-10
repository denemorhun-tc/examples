input_array = [1, 7, 4, 5, 200, 200, 200, 0, 9, 9, 9, 200,11, -66, 8]
target = 9

# # TODO SCENARIOS ould you like a slightly harder challenge next? Something like:
# Return all even numbers in a new list
# Count how many numbers are greater than a threshold
# Return the index of the largest number

#Initializing max_item with the first element
#Looping through all elements 
#Comparing each current_item to max_item 
#Updating max_item when needed 
# Returning the final max_item 

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

def remove_duplicates(array):
    array = set(array)
    return array

# # def remove_duplicates2(array):
#     print(array)
#     #Hint: Loop through the array and add items to a new list only if they haven’t appeared before.
#     seen = {}
#     # current_item = array[0]
#     seen[array[0]] = 1
#     for i in range(1, len(array)):
#         if array[i] not in seen:
#             seen[array[i]] = 1
#         else:
#             seen[array[i]] += 1
#         i += 1
#     return seen

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
    array = [1, 3, 3, 1, 3, 1, 1, 1, 1, 1, 3]
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

print(move_even_numbers_to_front())

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

print(separate_element(1))






    
# Remove Duplicates from Sorted Array
# Given a sorted array nums, remove the duplicates in-place such that each element appears only once. Return the new length of the array.
# You must not use extra space; modify the input array in-place with O(1) extra memory.
# def remove_duplicating_elements():
#     array = [0, 1, 2,3, 4]

#     #i -> fast index
#     #j -> slow index
#     j = 1
#     # loop through array if different, that's a unique number.
#     for i in range(len(array)):
#         print(f'fast index i array[{i}] with value {array[i]} vs slow index j array[{j}] with value {array[j]}')
#         if array[i] != array[j]:
#             print('we found a new unique value')
#             # assigned the value of i to slow index and move j to next
#             j += 1
#             array[j] = array[i]
#         print(f'j is {j} now')

#         # the length of the array has only gone to the j
#     return j

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


