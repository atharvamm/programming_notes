# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_array = sorted(nums)
        gt_array = list(range(len(nums)+1))
        for i in range(len(sorted_array)):
            cur_sorted,cur_gt = sorted_array[i],gt_array[i]
            # print(cur_sorted,cur_gt)
            if cur_sorted != cur_gt or i == len(sorted_array):
                return cur_gt
        return cur_sorted + 1
        