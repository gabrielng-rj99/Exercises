'''     14. Longest Common Prefix       Easy

Write a function to find the longest common prefix
string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
        Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        j = 0
        output = ""
        while True:
            try:
                for i in range(1, len(strs)):
                    if strs[i][j] != strs[0][j]:
                        return output
                    
                output += strs[0][j]
                j += 1
            
            except IndexError:
                break

        return output
    
testcases = [
    ["flower","flow","flight"],
    ["dog","racecar","car"],
]

for test in testcases:
    print(Solution().longestCommonPrefix(test))