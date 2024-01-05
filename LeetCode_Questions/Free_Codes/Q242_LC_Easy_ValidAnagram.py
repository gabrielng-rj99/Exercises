"""     242  Valid Anagram  Easy

Given two strings s and t,
return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the
letters of a different word or phrase, typically using all
the original letters exactly once.


Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false
 

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters?
How would you adapt your solution to such a case?

"""

testcases = [
    ("anagram", "nagaram"),
    ("rat", "car"),
]

# without Try Except
'''class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        Hmap_s = {}
        Hmap_t = {}

        for char in s:
            Hmap_s[char] = Hmap_s.get(char, 0) + 1

        for char in t:
            Hmap_t[char] = Hmap_t.get(char, 0) + 1

        for letter in s:
            if letter not in t:
                return False
            
            elif Hmap_s[letter] != Hmap_t[letter]:
                return False
            
        return True'''

# My True Way
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        Hmap_s = {}
        Hmap_t = {}

        for char in s:
            Hmap_s[char] = Hmap_s.get(char, 0) + 1

        for char in t:
            Hmap_t[char] = Hmap_t.get(char, 0) + 1
            
        return Hmap_s == Hmap_t






for test in testcases:
    print(Solution().isAnagram(test[0], test[1]))