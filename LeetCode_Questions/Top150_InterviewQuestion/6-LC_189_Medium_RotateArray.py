"""     189.    Rotate Array     Medium      

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]

Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]


Example 2:
    Input: nums = [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]

Explanation: 
    rotate 1 steps to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:
    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can.
There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?"""

import time

nums = [1,2,3,4,5,6,7]
k = 3


class Solution1():
    def rotate(self, nums: list[int], k: int) -> None:
        for i in range(k):
            nums.insert(0, nums.pop())

        return nums

class Solution2():
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)               # Time Complecity O(n) because slicing method uses "for" in low level
        nums[:] = nums[-k:] + nums[:-k] # same as nums = nums[-k:] + nums[:-k], but O(1) space instead of O(n)
        return nums

class Solution3():
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        for i in range(k):
            nums = [nums[-1]] + nums[:-1]

        return nums


def benchmark(solution):  
    nums = [1,2,3,4,5,6,7] 
    k = 3

    t1 = time.perf_counter()
    ans= solution.rotate(nums, k)
    t2 = time.perf_counter()
    tt = t2-t1
    return ans, tt


solutions = [
    Solution1(),
    Solution2(),
    Solution3(),
]

n = 1
Hmap = {}

for solution in solutions:
    Hmap[f"S{n}"] = Hmap.get(f"S{n}", benchmark(solution))
    n += 1

for key in Hmap:
    print (key, Hmap[key])
    