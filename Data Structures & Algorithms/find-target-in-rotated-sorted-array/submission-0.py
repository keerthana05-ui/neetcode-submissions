from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # 1. Check if the middle element is our target
            if nums[mid] == target:
                return mid
            
            # 2. Check if the left half is continuously sorted
            if nums[left] <= nums[mid]:
                # Verify if target lies within this sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Search left
                else:
                    left = mid + 1   # Search right
                    
            # 3. Otherwise, the right half MUST be continuously sorted
            else:
                # Verify if target lies within this sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Search right
                else:
                    right = mid - 1  # Search left
                    
        # Target not found in the array
        return -1