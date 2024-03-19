# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

class Solution(object):
    def topKFrequent(self, nums, k):
        """
            :type nums: List[int]
            :type k: int
            :rtype: List[int]
        """
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        # count the number of unique elements
        for n in nums:
            count[n] = 1 + count.get(n , 0)

        # append the numder of the element to the value 
        # Example: 2 existe 3 times so in the freq 3 will be the index and 2 will be the value
        for n, c in count.items():
            freq[c].append(n)

        # start the loop from the last element to the first element in descending order
        for i in range(len(freq) - 1, 0, -1):
            # append the result to the res array until we reach the (k)
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

# test 
s = Solution()

nums = [1, 1, 1, 2, 2, 3, 3]
k = 2

print(f"nums: {nums} && k: {k}")
print(s.topKFrequent(nums, k))
