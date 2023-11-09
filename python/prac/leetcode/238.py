'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''

import numpy as np
from functools import reduce

# nums = np.random.randint(low = 0,high = 5, size = 5).tolist()
nums = [1, 2, 4, 1, 4]
excepted_result = []
for i in range(len(nums)):
    cur_list = nums[0:i]+nums[i+1:]
    excepted_result.append(reduce(lambda x,y: x*y,cur_list))
print("Original Array: ",nums)
print("All Product: ",reduce(lambda x,y : x*y,nums))
print("Expected Array: ",excepted_result)

##### Optimized Solution #####
optimized_soln = None

print("Optimized Solution: ",optimized_soln)


