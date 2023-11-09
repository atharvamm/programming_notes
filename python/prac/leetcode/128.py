'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''
def longestConsecutive(ip):
    def merge(sec1,sec2):
        len_sec1,len_sec2 = len(sec1),len(sec2)
        sec1_ind,sec2_ind = 0,0
        new_arr,new_arr_len = [],len_sec1+len_sec2
        while len(new_arr) < new_arr_len:
            if not sec1_ind < len_sec1:
                if sec2_ind < len_sec2:
                    temp = sec2[sec2_ind]
                    sec2_ind += 1
            elif not sec2_ind < len_sec2:
                if sec1_ind < len_sec1:
                    temp = sec1[sec1_ind]
                    sec1_ind += 1
            else:
                if sec1[sec1_ind] < sec2[sec2_ind]:
                    temp = sec1[sec1_ind]
                    sec1_ind += 1
                else:
                    temp = sec2[sec2_ind]
                    sec2_ind += 1
            new_arr.append(temp)
        return new_arr
    def merge_sort(ip):
        if len(ip) < 2:
            return ip
        mid = len(ip)//2
        sec1,sec2 = merge_sort(ip[0:mid]),merge_sort(ip[mid:])
        return merge(sec1,sec2)
    
    if len(ip) == 0:
        return 0
    sorted_ip = merge_sort(ip)
    len_sorted_ip = len(sorted_ip)
    start,cur,end,max_len = 0,0,0,0
    while cur < len_sorted_ip - 1:
        if sorted_ip[cur] + 1 == sorted_ip[cur + 1]:
            end += 1    
        else:
            cur_len = end - start + 1
            if cur_len > max_len:
                max_len = cur_len
            start = cur
            end = start
        cur += 1
    
    cur_len = end - start + 1
    if cur_len > max_len:
        max_len = cur_len

    return max_len


test_cases = [
    # Test Case 1
    {
        "input": [100, 4, 200, 1, 3, 2],
        "expected": 4
    },
    # Test Case 2
    {
        "input": [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
        "expected": 9
    },
    # Test Case 3
    {
        "input": [1, 1, 1, 1, 1],
        "expected": 1
    },
    # Test Case 4
    {
        "input": [],
        "expected": 0
    },
    # Test Case 5
    {
        "input": [9, 8, 7, 6, 5, 4, 3, 2, 1],
        "expected": 9
    },
    # Test Case 6
    {
        "input": [10, 11, 12, 13],
        "expected": 4
    },
    # Test Case 7
    {
        "input": [5, 2, 20, 9, 4, 3],
        "expected": 4
    },
    # Test Case 8
    {
        "input": [8, 5, 10, 6, 7],
        "expected": 4
    },
    # Test Case 9
    {
        "input": [100],
        "expected": 1
    },
    # Test Case 10
    {
        "input": [1, 2, 3, 4, 5],
        "expected": 5
    },
    # Test Case 11
    {
        "input": [7, 7, 7, 7, 7],
        "expected": 1
    },
    # Test Case 12
    {
        "input": [5, 9, 11, 6, 7],
        "expected": 3
    },
    # Test Case 13
    {
        "input": [15, 8, 12, 14, 13],
        "expected": 4
    },
    # Test Case 14
    {
        "input": [6, 4, 2, 0, 8],
        "expected": 1
    },
    # Test Case 15
    {
        "input": [30, 35, 40, 45],
        "expected": 1
    }
]

for idx, test_case in enumerate(test_cases, 1):
    input_data = test_case["input"]
    expected_output = test_case["expected"]
    output = longestConsecutive(input_data)
    print(output == expected_output)

