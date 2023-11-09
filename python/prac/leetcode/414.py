# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        len_nums = len(nums)
        if len_nums < 3:
            return nums[-1]
        else:
            i = len_nums - 1
            uniq = 1
            while i > 0:
                if nums[i] != nums[i-1]:
                    uniq += 1
                    if uniq == 3:
                        return nums[i - 1]
                i -= 1
            return nums[-1]