# '''Given an array of integers nums and an integer target, return indices of the two
# numbers such that they add up to target. You may assume that each input would
# have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order'''

# Example 1:
# Input: nums = [2,7,11,15], target = 9

# Example 2:
# Input: nums = [3,2,4], target = 6

# Example 3:
# Input: nums = [3,3], target = 6

# 'm using nested loop to get the output u desired................'

# Sol:

def two_sums(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]


nums1 = [2,7,11,15]
target1 = 9
print(two_sums(nums1, target1))

nums2 = [3,2,4]
target2 = 6
print(two_sums(nums2, target2))

nums3 = [3,3]
target3 = 6
print(two_sums(nums3, target3))


# ----------------------------------------------------------------------------------------