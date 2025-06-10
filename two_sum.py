# Goal:
# Instead of checking every possible pair, you remember what you’ve seen so far, and check if the number you need to reach the target has already appeared.

# Think this way:
# As you loop through the array:

# For each num, calculate the complement:
# complement = target - num

# Ask: Have I already seen this complement?

# If yes → you’ve found the two numbers.

# If not → store the current number and its index for future lookups.


def two_sum(nums, target):
    seen = {}
    for i in range (len(nums)):
        print (f'nums[i] {nums[i]}')
        for j in range  (i+1, len(nums)):
            print(f'nums[j] {nums[j]}')
            if nums[i] + nums[j] == target:
                return [i, j]

# print(two_sum([1,5,3,4, 2000, 20000, 40], 7))
# print(two_sum([1,5,3,2000, 20000, 40, 4], 7))

def two_sums_dict(nums, target):
    seen = {}

    for i in range(len(nums)):
        if target - nums[i] in seen.keys():
            print('Complement found in dictionary (3)')
            return [i, seen.get(target-nums[i])]
        else:
            seen[nums[i]] = i
        print(i, seen)

print(two_sums_dict([1,5,3,4, 2000, 20000, 40], 7))
print(two_sums_dict([1,5,3,2000, 20000, 40, 4], 7))
