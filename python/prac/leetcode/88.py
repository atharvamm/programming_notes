# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ni,i = 0,0
        next,temp = None,None
        while i < m+n:
            if ni < n:
                if nums1[i] > nums2[ni]:
                    temp = nums2[ni]
                    for j in range(i,m+n):
                        next = nums1[j]
                        nums1[j] = temp
                        temp = next
                    ni += 1
                elif i >= m + ni:
                    nums1[i] = nums2[ni]
                    ni += 1
            i += 1