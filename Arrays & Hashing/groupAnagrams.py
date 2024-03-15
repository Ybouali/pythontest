# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        # Create a dictionary 
        res = defaultdict(list)

        # loop through all the strings 
        for s in strs:
            # init the count with 0 * 26 // 26 is the number of the characters existing
            count = [0] * 26

            for c in s:
                # the value of the character will be set to 1
                count[ord(c) - ord("a")] += 1

            # append the s to the key count
            res[tuple(count)].append(s)

        # return the result
        return res.values()
    
    def groupAnagrams_2(self, strs: list[str]) -> list[list[str]]:

        # Create a dictionary 
        res = {}

        # loop through all the strings 
        for s in strs:
            
            # sort the word and store it in new str
            nWord = ''.join(sorted(s))

            # check if the exist in the result dictionary if not store the new word and his value will be empty
            if nWord not in res:
                res[nWord] = []

            # store the word in reslt dictionary
            res[nWord].append(s)

        # return the result
        return res.values()


s = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(f"strs   = ${strs}")
print(f"result = {s.groupAnagrams(strs)}\n")

strs = [""]

print(f"strs   = ${strs}")
print(f"result = {s.groupAnagrams(strs)}\n")

strs = ["a"]

print(f"strs   = ${strs}")
print(f"result = {s.groupAnagrams(strs)}\n")