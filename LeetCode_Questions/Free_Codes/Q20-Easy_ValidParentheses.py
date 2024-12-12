""" 20. Valid Parentheses - Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
import math

def isValid(s: str) -> bool:
    if len(s)<2 or len(s)%2!=0:
        return False

    match_map = {
        ')':'(',
        ']':'[',
        '}':'{',
    }

    stack = []

    for char in s:
        if char in match_map.values():
            stack.append(char)
        
        elif char in match_map.keys():
            if stack and stack[-1] == match_map[char]:
                stack.pop()
            else:
                return False
        else:
            return False
    
    return len(stack) == 0

print(isValid("(){}}{"))
print(isValid("[{()}]"))
print(isValid("[()]"))
print(isValid("(([]){})"))
print(isValid("()"))
print(isValid("[("))