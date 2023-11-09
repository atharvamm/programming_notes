# Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_num = list(bin(n)[2:])
        return sum([int(dig) for dig in bin_num])

        