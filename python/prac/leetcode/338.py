# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

class Solution:
    def countBits(self, n: int) -> List[int]:
        nums = list(range(n+1))
        ans = []
        for num in nums:
            bin_num = list(bin(num)[2:])
            ans.append(sum([int(dig) for dig in bin_num]))
        return ans