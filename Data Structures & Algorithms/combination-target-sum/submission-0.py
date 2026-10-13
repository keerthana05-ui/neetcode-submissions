class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        com = []
        def backtrack(i: int, remain: int) -> None:
            if remain == 0:
                result.append(com.copy())
                return
            if remain < 0 or i == len(nums):
                return
            com.append(nums[i])
            backtrack(i, remain - nums[i])
            com.pop()
            backtrack(i+1, remain)
        backtrack(0, target)
        return result