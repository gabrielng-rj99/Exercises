'''             1. Two Sum      Easy        

Given an array of integers nums and an integer target, return
indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]
 

Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9

Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?'''

nums = [3,2,4,6,8]

def twoSum_On2(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in nums[i+1:]:
            return (i, (nums[i+1:].index(complement)+i+1))
        
def twoSum_On(nums: list[int], target: int) -> list[int]:
    numsMap = {}

    for i in range(len(nums)):
        complement = target - nums[i]
        print (complement)
        if complement in numsMap:
            print (numsMap)
            return [numsMap[complement], i]
        
        numsMap[nums[i]] = i

    return []  # No solution found

print(twoSum_On(nums = [3,1,2,4,-4,6,8], target=0))

'''Nota:
Estudar HashTable, HashMap e HashFuctions
'''