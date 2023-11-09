# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i,temp,next = 0, None,None
        len_arr = len(arr)
        while i < len_arr - 1:
            if arr[i] == 0:
                temp,k = 0,i
                while k < len_arr - 1:
                    next = arr[k+1]
                    arr[k+1] = temp
                    temp = next
                    k += 1
                i += 2
            else:
                i += 1
        