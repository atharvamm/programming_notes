# Reverse bits of a given 32 bits unsigned integer.

class Solution:
    def reverseBits(self, n: int) -> int:
        bin_str = bin(n)[2:]
        rev_str_list = "0"*(32 - len(bin_str)) + bin_str
        rev_bin_list = [2**i*int(rev_str_list[i]) for i in range(len(rev_str_list))]
        return sum(rev_bin_list)
