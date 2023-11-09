# Given an array nums of integers, return how many of them contain an even number of digits.

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counts = 0
        for i in range(len(nums)):
            digits = 0
            cur_num = nums[i]
            while cur_num > 0:
                digits += 1
                cur_num = cur_num//10
            if digits % 2 == 0:
                counts += 1
        return counts

