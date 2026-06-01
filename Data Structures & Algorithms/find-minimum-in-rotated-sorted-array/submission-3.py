class Solution:
    def findMin(self, nums: list[int]) -> int:
        # Initialize the boundary pointers for the binary search space
        left = 0
        right = len(nums) - 1
        
        # Continuously divide the search space in half
        while left < right:
            mid = (left + right) // 2
            
            # Case 1: The midpoint is larger than the right boundary element.
            # This confirms the inflection/drop point lies strictly to the right.
            if nums[mid] > nums[right]:
                left = mid + 1
                
            # Case 2: The midpoint is smaller than or equal to the right boundary.
            # The minimum element is either at 'mid' or situated to its left.
            else:
                right = mid
                
        # The loop terminates exactly when left == right, pinpointing the minimum element.
        return nums[left]