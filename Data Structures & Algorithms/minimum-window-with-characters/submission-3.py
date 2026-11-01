class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
            
        need = Counter(t)
        required = len(need)  # Total unique characters we need
        have = {}
        formed = 0            # How many unique characters we have fully satisfied

        left = 0
        best_len = float('inf')
        best_start = 0

        for right, ch in enumerate(s):
            have[ch] = have.get(ch, 0) + 1
            
            # Check if we just completed a required character
            if ch in need and have[ch] == need[ch]:
                formed += 1
                
            # This replaces your isvalid() function
            while formed == required:
                window = right - left + 1
                if window < best_len:
                    best_len = window
                    best_start = left
                    
                left_ch = s[left]
                have[left_ch] -= 1
                
                # Check if we just broke a required character
                if left_ch in need and have[left_ch] < need[left_ch]:
                    formed -= 1
                    
                left += 1

        if best_len == float('inf'):
            return ""
            
        return s[best_start : best_start + best_len]     