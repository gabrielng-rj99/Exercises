'''     45. Jump Game II            Medium          

You are given a 0-indexed array of integers nums of length n.
You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a
forward jump from index i. In other words, if you are at nums[i],
you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n

Return the minimum number of jumps to reach nums[n - 1].
The test cases are generated such that you can reach nums[n - 1].

Example 1:

    Input: nums = [2,3,1,1,4]
    Output: 2
        Explanation: The minimum number of jumps to reach
        the last index is 2. Jump 1 step from index 0 to 1,
        then 3 steps to the last index.

Example 2:
    Input: nums = [2,3,0,1,4]
    Output: 2
 

Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 10^3
It's guaranteed that you can reach nums[n - 1].'''

def canJump1(nums: list[int]) -> bool:
    if len(nums) <= 2:
        if len(nums)==1:
            return 0
        
        return 1

    i = len(nums)-1
    jump = 0

    while i > 0:
        j = 1
        maxjump = 0

        while j <= i:
            test_i = nums[i-j]+(i-j)
            if test_i >= i:
                maxjump = j

            j += 1
   
        i -= maxjump
        jump += 1

    return jump

'''
Time  Complexity: O(2^n)
Space Complexity: O(1)    (1*4) + funcitons
'''
#_______________________________________________________________________________________


def canJump2(nums: list[int]) -> bool:
    jumps = 0
    endpoint = 0
    next_end = 0

    for i in range(len(nums) - 1):
      next_end = max(next_end, i + nums[i])
      if next_end >= len(nums) - 1:
        jumps += 1
        break
      if i == endpoint:         # Visited all the items on the current level
        jumps += 1              # Increment the level
        endpoint = next_end     # Make the queue size for the next level

    return jumps

'''
Time  Complexity: O(n)
Space Complexity: O(1)    (1*3) + funcitons
'''
#_______________________________________________________________________________________


nums = [2,3,1,1,2,0,0]
print(canJump1(nums), canJump2(nums), sep=" , ")