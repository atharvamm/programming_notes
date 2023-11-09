# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        from math import factorial
        count = 0
        for j in range(n//2 + 1):
            i = n - (j * 2)
            count += factorial(i+j)//(factorial(i)*factorial(j))
        return count

