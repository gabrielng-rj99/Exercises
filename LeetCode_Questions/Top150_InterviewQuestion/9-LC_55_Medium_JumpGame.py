'''     55. Jump Game

You are given an integer array nums. You are initially positioned
at the array's first index, and each element in the array represents
your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
    Input: nums = [2,3,1,1,4]
    Output: true
        Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
    Input: nums = [3,2,1,0,4]
    Output: false
        Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
    
Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5'''

def canJump(nums: list[int]) -> bool:
    if len(nums) <= 1:
        return True

    i = len(nums)-2
    zero_counter = 0
    while i >= 0:
        if nums[i] != 0 and zero_counter == 0:
            i -= 1
        
        elif nums[i] == 0:
            zero_counter += 1
            i -= 1

        elif nums[i] > zero_counter:
            zero_counter = 0
            i -= 1

        else:
            zero_counter += 1
            i -= 1


    if zero_counter == 0:
        return True
    else:
        return False
            
nums = []
print(canJump(nums))


'''     Intuition/Approach:
initially i misunderstood the ideia, and I will ignore that part in my explanation
first tought after understand was that i need to try for every index all solution
like make a tree decision, but fastly i see that is a dumb idea for that.

So i realized that the only number that can block the passage is 0, and the numbers
before must to be able to jump the 0, and the number is not capable of jump the 0,
he can be read as zero too. Example:
     ↓            ↓           ↓              ↓ 
[3,2,1,0,4] ➡ [3,2,0,0,4] ➡ [3,0,0,0,4] ➡ [0,0,0,0,4] ➡ False

now this case is impossible to move foward, but in my code I dont change the nums
values, only considering a 0 behavior. 


another 2 examples:
   ↓
[2,5,0,0] ➡ 5 > 1 (n zeros between the objective) so ➡ True

[3,0,0,2,0,4] ➡ [3,0,0,2,0,4] ➡ 2 > 1 and 3 > 2, so ➡ True
       ↑          ↑

See that the last value is not important, the only thing that matters if it
can be reach or no.

The only restriction for that code tha

Time Complexity: O(n)
Space Complexity: O(2)
'''