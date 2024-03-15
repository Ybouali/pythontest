# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

class Solution(object):
    def towSum(self, nums, target):
        """
        : type nums: List<int>
        : type target: int
        : rtype List<int>
        """

        # hashmap to set the numbers
        hashmap = {}

        # loop through all the numbers and get the index of each number and the index
        for i, n in enumerate(nums):
            # get what is the number needed to reach the target
            diff = target - n
            
            # if the diff is in the map so return the index in the map and i 
            if diff in hashmap:
                return [hashmap[diff], i]
            
            # else add the number to the map and set the index
            hashmap[n] = i

# test 
s = Solution()

nums = [2,7,11,15]
target = 9

print("test 1")
print(f"nums   = {nums} && target = {target}")
print(f"result = {s.towSum(nums, target)}\n")

nums = [3,2,4]
target = 6

print("test 2")
print(f"nums   = {nums} && target = {target}")
print(f"result = {s.towSum(nums, target)}\n")

nums = [3,3]
target = 6

print("test 3")
print(f"nums   = {nums} && target = {target}")
print(f"result = {s.towSum(nums, target)}")