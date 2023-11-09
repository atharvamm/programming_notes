# 209. Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead


def minSubArrayLen(target, nums) -> int:
    start,end,cur_sum,min_len,cur_len = 0,0,0,len(nums),0
    min_len_sum = 0
    while True:
        if cur_sum >= target:
            cur_len = end - start
            if cur_len <= min_len:
                min_len = cur_len
                min_len_sum = cur_sum
            cur_sum -= nums[start]
            start += 1
        else:
            if end == len(nums):
                break
            cur_sum += nums[end]
            end += 1
        # print("Start,End:",start,end," Cur Len, Min Len:",cur_len,min_len," Sum,Target:",cur_sum,target)
    if min_len == len(nums) and min_len_sum < target:
        return 0
    else:
        return min_len
    
    



test_cases = [(7,[2,3,1,2,4,3],2),
(15,[5,1,3,5,10,7,4,9,2,8],2),
(4,[1,4,4],1),
(11,[1,1,1,1,1],0),
(15,[1,2,3,4,5],5)]

for test_case in test_cases:
    op = minSubArrayLen(test_case[0],test_case[1])
    if op == test_case[-1]:
        print("Passed")
    else:
        print(test_case[-1],op,end = " : ")
        print("Failed")
    # break
