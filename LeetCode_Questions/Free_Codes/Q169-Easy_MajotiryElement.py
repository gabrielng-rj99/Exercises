class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
    

tescases = [
    ([3,2,3], 3),
    ([2,2,1,1,1,2,2], 2),
    ([4, 3, 3, 3, 2, 1, 3, 5, 6, 7, 3, 3], 3)
]

for testcase in tescases:
    print(Solution().majorityElement(testcase[0]) == testcase[1])