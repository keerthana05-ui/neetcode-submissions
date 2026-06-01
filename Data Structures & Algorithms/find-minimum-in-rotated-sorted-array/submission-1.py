class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        # INTERVIEW EDGE CASE TRICK:
        # If the first element is already smaller than the last element,
        # the array is NOT rotated out of order at all! It's perfectly sorted.
        # We can instantly return the first element.
        if nums[left] < nums[right]:
            return nums[left]
            
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        return nums[left]