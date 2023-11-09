# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        digs = []

        state = 1
        if x < 0:
            state = -1
        x = abs(x)
        while x > 0:
            digs.append(x%10)
            x = x//10
        power = len(digs) - 1
        ans = 0
        for dig in digs:
            ans += dig * 10**power
            power = power - 1
        ans = state * ans
        if state == 1 and ans > 2**31 -1:
            return 0
        elif state == -1 and ans < -2**31:
            return 0
        else:
            return ans
        