# 167. Two Sum II - Input Array Is Sorted
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

# Binary Search
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(start,end,array,target):
            if (len(array[start:end+1]) == 0):
                return -1
            else:
                mid = (start + end)//2
                if array[mid] == target:
                    return mid
                else:
                    if array[mid] > target:
                        return binary_search(start,mid - 1,array,target)
                    else:
                        return binary_search(mid + 1,end,array,target)
        
        for i in range(len(numbers)):
            search = target - numbers[i]
            ans = binary_search(i+1,len(numbers),numbers,search)
            if ans != -1:
                return [i+1,ans+1]


# Two Pointer
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start,end = 0,len(numbers) - 1

        while(start < end):
            cur_sum = numbers[start] + numbers[end]

            if cur_sum > target:
                end -= 1
            elif cur_sum < target:
                start += 1
            else:
                return [start+1,end + 1]