# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution(object):
    def validAnagrame(self, s, t):
        """
        : type s: str
        : type t: str
        : rtype: bool
        """

        # check if the two string has not the same length return false
        if len(s) != len(t):
            return False
        
        # will need tow maps that will hod the character and how mush we have of that character in that string 
        countT, countS = {}, {}

        # loop for all the indexs in the string and store the number of that character in the map
        for i in range(len(t)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        
        # in the end loop in the tow map's and check the number of each character
        for c in countT:
            # if the number character is not the same return false
            if countT.get(c, 0) != countS.get(c, 0):
                return False
        
        return True
    
# test

so = Solution()

s = "anagram"
t = "nagaram"

print("test 1")
print(f"s = {s} && t = {t}")
print(f"result -> {so.validAnagrame(s, t)}\n")

s = "rat"
t = "car"
print("test 2")
print(f"s = {s} && t = {t}")
print(f"result -> {so.validAnagrame(s, t)}\n")
