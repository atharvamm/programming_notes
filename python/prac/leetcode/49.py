'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = {}
        for i in range(len(strs)):
            cur_str = strs[i]
            ele = tuple(sorted(cur_str))
            if ele not in grouped_anagrams.keys():
                grouped_anagrams[ele] = []
            grouped_anagrams[ele].append(cur_str)
        return list(grouped_anagrams.values())