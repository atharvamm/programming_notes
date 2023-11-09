# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

class Solution:
    def isHappy(self, n: int) -> bool:
        prev_values = []
        while True:
            sum_n = sum([int(ele)**2 for ele in list(str(n))])
            if sum_n == 1:
                return True
            elif sum_n not in prev_values:
                prev_values.append(sum_n)
                n = sum_n
            elif sum_n in prev_values:
                return False
