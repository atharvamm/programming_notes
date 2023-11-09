'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        counts = Counter(nums).most_common(1)
        if counts and counts[0][1] > 1:
            return True
        return False
        