# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        len_nums = len(nums)
        while i < len_nums:
            if nums[i] % 2 == 1:
                cur_ele = nums[i]
                nums.remove(cur_ele)
                nums.append(cur_ele)
                len_nums -= 1
                continue
            i += 1
        return nums