# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        og_str = "".join([char.lower() for char in s if char.isalnum()])
        rev_str = og_str[::-1]
        if og_str == rev_str :
            return True
        return False