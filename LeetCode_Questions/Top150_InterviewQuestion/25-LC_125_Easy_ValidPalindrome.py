'''    125. Valid Palindrome, Easy


A phrase is a palindrome if, after converting all uppercase letters into lowercase
lettersand removing all non-alphanumeric characters, it reads the same forward and
backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
        Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: false
        Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: true
        Explanation: s is an empty string "" after removing non-alphanumeric characters.

Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.'''


testcases = ["0P"]

def isPalindrome(s: str) -> bool:
    lp, rp = 0, len(s)-1

    while lp<rp:
        if not s[lp].isalnum():
            lp += 1
        
        if not s[rp].isalnum():
            rp -= 1

        if s[lp].isalnum() and s[rp].isalnum():
            if s[lp].lower() != s[rp].lower():
                return False
            
            lp += 1
            rp -= 1

    return True
        
for test in testcases:
    print(isPalindrome(test))