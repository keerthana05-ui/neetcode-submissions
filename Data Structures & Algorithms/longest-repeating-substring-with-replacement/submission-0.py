class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        count = {}
        max_freq = 0
        for right in range(len(s)):
            current_char = s[right]
            count[current_char] = count.get(current_char, 0) + 1
            if count[current_char] > max_freq:
                max_freq = count[current_char]
            window_len = right - left + 1
            while window_len - max_freq > k:
                count[s[left]] -= 1
                left += 1
                window_len = right - left + 1
            if window_len > max_len:
                max_len = window_len
        return max_len