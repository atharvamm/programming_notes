# Given an array arr of integers, check if there exist two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            cur_ele = arr[i]
            find_ele = 2*cur_ele
            try :
                if find_ele > cur_ele:
                    print()
                    arr[i+1:].index(find_ele)
                else:
                    arr[:i].index(find_ele)
                return True
            except ValueError:
                pass
        return False