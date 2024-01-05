'''     9. Palindrome Number       Easy

Given an integer x, return true if x is a 
palindrome
, and false otherwise.


Example 1:
    Input: x = 121
    Output: true
        Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
    Input: x = -121
    Output: false
        Explanation: From left to right, it reads -121. From right to left,
        it becomes 121-. Therefore it is not a palindrome.

Example 3:
    Input: x = 10
    Output: false
        Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-2^31 <= x <= 2^31 - 1
 

Follow up: Could you solve it without converting the integer to a string?
'''

import time

testcases = [
    5*10000**1074 + 5,
    2**100,
    2**32,
    5*10**1000 + 5,
    2*10**30 + 2,
    250052,
    121,
    -121,
    10,
]


class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        i, j = 0, 0    
        x_list = []

        while True:
            if x//(10**j) == 0:
                j -= 1
                break

            x_list += [x//10**j - (x//10**(j+1))*10]
            j += 1

        while i<j:
            if x_list[i] == x_list[j]:
                i += 1
                j -= 1
            else:
                return False
            
        return True

class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev = 0
        temp = x

        while temp > 0:
            rev = rev * 10 + temp % 10
            temp //= 10

        return rev == x





def print1():
    start = time.perf_counter()
    for test in testcases:
        start2 = time.perf_counter()
        solution = Solution1().isPalindrome(test)
        end2 = time.perf_counter()
        print (f"Answer: {solution} ; time: {end2-start2}")

    end = time.perf_counter()
    print (f"\nAnswer: {solution} ; time: {end-start}")
    print("\n", "_"*40, "\n")


def print2():
    start = time.perf_counter()
    for test in testcases:
        start2 = time.perf_counter()
        solution = Solution2().isPalindrome(test)
        end2 = time.perf_counter()
        print (f"Answer: {solution} ; time: {end2-start2}")

    end = time.perf_counter()
    print (f"\nAnswer: {solution} ; time: {end-start}")
    print("\n", "_"*40, "\n")


print1()
print2()
