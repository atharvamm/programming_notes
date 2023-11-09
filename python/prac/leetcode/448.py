# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        from collections import Counter
        counts = Counter(nums)
        ans = []
        for i in range(1,len(nums)+1):
            if not counts.get(i,0):
                ans.append(i)
        return ans