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

        print ("----------- freq start -----------")
        print (freq)
        print ("----------------------------------")

        for n in nums:
            count[n] = 1 + count.get(n , 0)

        print ("----------- count start -----------")
        print (count)
        print ("----------------------------------")

        for n, c in count.items():
            freq[c].append(n)

        print ("----------- count start -----------")
        print (freq)
        print ("----------------------------------")

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

# test 
s = Solution()

nums = [1, 1, 1, 2, 2, 3, 3]
k = 3

print(f"nums: {nums} && k: {k}")
print(s.topKFrequent(nums, k))
