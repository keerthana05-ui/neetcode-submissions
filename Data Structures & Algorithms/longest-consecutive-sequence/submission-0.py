class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Step 1: Put all numbers into a set for instant O(1) lookups
        num_set = set(nums)
        longest_streak = 0
        
        # Step 2: Loop through each number to look for sequence starters
        for num in num_set:
            # Check if this number is the absolute start of a chain
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1
                
                # Keep counting upward as long as the next consecutive numbers exist
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Update our record holder with the maximum value found
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak