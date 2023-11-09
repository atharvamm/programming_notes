'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        count_s = sorted(Counter(s).most_common(),key = lambda x : x[0])
        count_t = sorted(Counter(t).most_common(),key = lambda x : x[0])
        print(count_s,count_t)

        if all([count_s,count_t]) and count_s == count_t:
            return True
        return False