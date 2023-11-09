'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        ans = []
        counts = Counter(nums)
        return [ele[0] for ele in counts.most_common(k)]
