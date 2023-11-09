# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start,end = 0,len(nums)
        while True:
            mid = (start + end) // 2
            if end < start or mid > len(nums) - 1:
                break
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                break
        return -1