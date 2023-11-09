# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_i = -1
        for i in range(len(arr)-1):
            if i >= max_i:
                spliced_arr = arr[i+1:]
                max_i = spliced_arr.index(max(spliced_arr)) + i + 1
            arr[i] = arr[max_i]
        arr[-1] = -1
        return arr