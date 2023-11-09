# Sorting Algorithms 
# Refer for theory : https://www.programiz.com/dsa/sorting-algorithm

# 1. **Bubble Sort
def bubble_sort(ip):
    '''
    Swapped variable is not necessary but optimizes the sort when the array is already sorted by breaking the loop.
    '''
    len_ip = len(ip)
    for max_sort in range(len_ip):
        swapped = False
        for sub_ind in range(len_ip - max_sort - 1):
            if ip[sub_ind] > ip[sub_ind + 1]:
                ip[sub_ind],ip[sub_ind + 1] = ip[sub_ind + 1],ip[sub_ind]
                swapped = True
            else:
                continue
        if not swapped :
            break
    return ip

# 2. **Selection Sort
def selection_sort(ip):
    len_ip = len(ip)
    for start in range(len_ip):
        minimum = start
        for ind in range(start,len_ip):
            cur_ele = ip[ind]
            if cur_ele < ip[minimum]:
                minimum = ind
        ip[start],ip[minimum] = ip[minimum],ip[start]
    return ip

# 3. **Insertion Sort
def insertion_sort(ip):
    len_ip = len(ip)
    sorted_ind = 1
    for key_ind in range(sorted_ind,len_ip):
        if ip[key_ind] < ip[key_ind - 1]:
            temp = ip[key_ind]
            for ele_ind in range(key_ind,-1,-1):
                if temp < ip[ele_ind - 1]:
                    ip[ele_ind] = ip[ele_ind - 1]
                else:
                    break
            ip[ele_ind] = temp                
    return ip

# 4. **Merge Sort

def merge(sec1,sec2):
    sec1_ind,sec2_ind = 0,0
    len_sec1,len_sec2 = len(sec1),len(sec2)
    new_arr_len = len_sec1 + len_sec2
    new_arr = []
    while len(new_arr) < new_arr_len:
        # There are no elements in sec1
        if not sec1_ind < len_sec1:
            if sec2_ind < len_sec2:
                temp = sec2[sec2_ind]
                sec2_ind += 1
        # There are no elements in sec2
        elif not sec2_ind < len_sec2:
            if sec1_ind < len_sec1:
                temp = sec1[sec1_ind]
                sec1_ind += 1
        # Else
        else :
            # sec1 < sec2
            if sec1[sec1_ind] < sec2[sec2_ind]:
                temp = sec1[sec1_ind]
                sec1_ind += 1
            # sec2 < sec1
            else:
                temp = sec2[sec2_ind]
                sec2_ind += 1
        new_arr.append(temp)
    return new_arr

def merge_sort(ip):
    ip_len = len(ip)       
    if ip_len < 2:
        return ip
    mid = ip_len//2
    sec1,sec2 = merge_sort(ip[0:mid]),merge_sort(ip[mid:])
    merged = merge(sec1,sec2)
    return merged

# 5. **Quick Sort
def quick_sort(ip):
    pass

# 6. **Heap Sort
def heap_sort(ip):
    pass

# 7. **Counting Sort
def counting_sort(ip):
    pass

# 8. **Radix Sort
def radix_sort(ip):
    pass

# 9. **Bucket Sort
def bucket_sort(ip):
    pass

sorting = {
    "bubble": bubble_sort,
    "selection": selection_sort,
    "insertion": insertion_sort,
    "merge": merge_sort,
    "quick": quick_sort,
    "heap": heap_sort,
    "counting": counting_sort,
    "radix": radix_sort,
    "bucket": bucket_sort
}


ip_arrays = [[2,1],
             [3,4,1,2],
             [1,7,2],
             [8,3,5,2,4],
             [30, 28, 84, 72, 59, 65, 94, 74, 4, 96],
             [77, 39, 97, 52, 60, 86, 79, 43, 44, 3],
             [85, 97, 59, 79, 69, 97, 35, 4, 94, 17],
             [81, 98, 51, 49, 9, 5, 90, 18, 56, 23],
             [41, 37, 33, 30, 23, 73, 33, 87, 97, 30]]



for array in ip_arrays:
    custom_sort = sorting["quick"](array)
    print(custom_sort,custom_sort == sorted(array))
