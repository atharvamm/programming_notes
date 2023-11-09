# Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_cons = 0
        for i in range(len(nums)):
            ele = nums[i]
            if ele == 1:
                count += 1
            else :
                if count > max_cons:
                    max_cons = count
                count = 0
        if count > max_cons:
            max_cons = count
        return max_cons
            