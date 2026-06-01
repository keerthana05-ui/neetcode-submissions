class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            # PERFORMANCE TRICK: Bitwise right shift behaves exactly like // 2
            # but is handled faster by the lower-level execution engine.
            mid = (left + right) >> 1
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        return nums[left]