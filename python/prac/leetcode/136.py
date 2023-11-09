# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        counts = Counter(nums)
        for item in counts.items():
            if item[1] == 1:
                return item[0]