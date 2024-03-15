# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution(object):
    def containsDuplicate(self, nums):
        """
        : type nums: List<int>
        : return type bool
        """

        # create a hashset will contain nums not duplicated
        hashset = set()

        # loop through all elements of nums
        for n in nums:
            # if n is in the hashset will return True
            if n in hashset:
                return True
            # else add the number to the hashset
            hashset.add(n)
        return False
        

# test 

s = Solution()

nums = [1, 2, 3, 1]

print(f"nums Test 1 -> {nums}")
print(f"Result      -> {s.containsDuplicate(nums)}\n")

nums = [1, 2, 3, 4]

print(f"nums Test 2 -> {nums}")
print(f"Result      -> {s.containsDuplicate(nums)}\n")

nums = [1,1,1,3,3,4,3,2,4,2]

print(f"nums Test 3 -> {nums}")
print(f"Result      -> {s.containsDuplicate(nums)}")
