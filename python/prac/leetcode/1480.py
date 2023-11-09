# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = [None]*len(nums)
        runningSum[0] = nums[0]
        for i in range(1,len(nums)):
            runningSum[i] = nums[i] + runningSum[i-1]
        return runningSum