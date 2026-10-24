class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            if b in seen:
                return [seen[b], i]
            seen[a] = i
        return []        