class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        longest = 0
        for i in num:
            if i - 1 not in num:
                len = 1
                while i+1 in num:
                    len += 1
                    i = i+1
                longest = max(len, longest)
        return longest