class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #twoSum question solution
        seen = {}
        for i  in range(len(nums)):
            c=target-nums[i]
            if c in seen:
                return [seen[c] , i]
            seen[nums[i]] = i     
        