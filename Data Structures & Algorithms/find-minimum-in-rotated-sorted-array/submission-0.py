class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        # Binary Search
        while left < right:
            mid = (left + right) // 2
            
            # If the middle element is greater than the rightmost element,
            # it means the minimum element must live on the right side of mid.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, the middle element is less than or equal to the rightmost,
            # meaning the minimum element is either mid itself or to the left of mid.
            else:
                right = mid
                
        # When left and right pointers meet, they point exactly at the minimum element
        return nums[left]