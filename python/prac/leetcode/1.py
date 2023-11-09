'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            cur_num = nums[i]
            find_num = target - cur_num
            if find_num in sorted_nums:
                find_ind = nums.index(find_num)
                if i != find_ind:
                    return [i,find_ind]
        return []