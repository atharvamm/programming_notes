# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# Binary Search


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1

        start,mid,end = 0,0,x//2 + 1
        sq = lambda n : n * n

        while start <= end:
            mid = (start + end) // 2
            cur_sq = sq(mid)
            if cur_sq > x:
                if sq(mid - 1) < x:
                    return mid - 1
                end = mid
            elif cur_sq == x:
                return mid
            else:
                if sq(mid + 1) > x:
                    return mid 
                start = mid
        