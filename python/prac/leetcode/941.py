# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        len_arr = len(arr)
        switch = None
        if len(arr) >= 3:
            for i in range (1,len_arr - 1):
                if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                    switch = i
                    break
                
            if switch is None:
                return False
            else:
                for i in range(1,switch+1):
                    if arr[i] > arr[i-1]:
                        pass
                    else:
                        return False
                    
                for i in range(switch + 1,len_arr):
                    if arr[i] < arr[i-1]:
                        pass
                    else:
                        return False
                return True
        return False





