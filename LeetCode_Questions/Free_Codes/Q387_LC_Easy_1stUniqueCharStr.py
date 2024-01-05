'''     387. First Unique Character in a String

Given a string "s", find the first non-repeating character in it
and return its index.If it does not exist, return -1.

 

Example 1:
    Input: s = "leetcode"
    Output: 0

Example 2:
    Input: s = "loveleetcode"
    Output: 2

Example 3:
    Input: s = "aabb"
    Output: -1
 

Constraints:

1 <= s.length <= 10^5
"s" consists of only lowercase English letters.
'''


import time
import collections

largeStringRepeating    = "abcdefghjiklmnopqrstuvwxyz" + "z"*1000000 + "zyxwvutsrqponmlkjihgfedcba"
largeStringNonRepeating = "bcdefghjiklmnopqrstuvwxyz" + "z"*1000000 + "zyxwvutsrqponmlkjihgfedcba"

testcases = ["leetcode",
             "abcdefghjiklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba",
             "bcdefghjiklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba",
             largeStringNonRepeating,
             largeStringRepeating]

# __________________________________________________________

def firstUniqChar_1st(s: str) -> int:
    for i in range(len(s)):
        if s[i] not in s[i+1:] and s[i] not in s[:i]:
            return i
    return -1


def firstUniqChar_Last(s: str) -> int:
    m = [0]*26
    for i in range(len(s)):
        m[ord(s[i]) - ord('a')] += 1

    #print(m)

    for i in range(len(s)):
        if m[ord(s[i]) - ord('a')] == 1:
            return i

    return -1

def test_1st(testcases):
    print("\n_______________________\n")
    cronometro = time.perf_counter()
    for test in testcases:
        t1 = time.perf_counter()
        ans = (firstUniqChar_1st(test))
        t2 = time.perf_counter()
        print (f"{ans:<9}", t2-t1)

    print(f'\nTotal: {time.perf_counter()-cronometro}')
    print("\n_______________________\n")

def test_Last(testcases):
    print("\n_______________________\n")
    cronometro = time.perf_counter()
    for test in testcases:
        t1  = time.perf_counter()
        ans = (firstUniqChar_Last(test))
        t2  = time.perf_counter()
        print (f"{ans:<9}", t2-t1)

    print(f'\nTotal: {time.perf_counter()-cronometro}')
    print("\n_______________________\n")

# __________________________________________________________


def firstUniqChar_community1(s: str) -> int:
    d = {}
    for char in s:
        d[char] = d.get(char,0) + 1
    #print (d)
    for i , char in enumerate(s):
        if d[char] == 1:
            return i
    return -1

def test_community1(testcases):
    print("\n_______________________\n")
    cronometro = time.perf_counter()
    for test in testcases:
        t1 = time.perf_counter()
        ans = (firstUniqChar_community1(test))
        t2 = time.perf_counter()
        print (f"{ans:<9}", t2-t1)
    print(f'\nTotal: {time.perf_counter()-cronometro}')
    print("\n_______________________\n")

def firstUniqChar_communityBEST(s: str) -> int:
    hset = collections.Counter(s);
    # Traverse the string from the beginning...
    for idx in range(len(s)):
        # If the count is equal to 1, it is the first distinct character in the list.
        if hset[s[idx]] == 1:
            return idx
    return -1       # If no character appeared exactly once...

def test_communityBEST(testcases):
    print("\n_______________________\n")
    cronometro = time.perf_counter()
    for test in testcases:
        t1 = time.perf_counter()
        ans = (firstUniqChar_communityBEST(test))
        t2 = time.perf_counter()
        print (f"{ans:<9}", t2-t1)
    print(f'\nTotal: {time.perf_counter()-cronometro}')
    print("\n_______________________\n")



#test_1st(testcases)
test_community1(testcases)
test_communityBEST(testcases)
test_Last(testcases)