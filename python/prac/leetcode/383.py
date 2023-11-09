# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        magazine_ct = Counter(magazine)
        ransomNote_ct = Counter(ransomNote)

        for key in ransomNote_ct.keys():
            if ransomNote_ct[key] <= magazine_ct.get(key,0):
                continue
            else : 
                return False
        return True