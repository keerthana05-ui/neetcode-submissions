class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        have = {}
        formed = 0
        required = len(need)

        l = 0
        best_len = float('inf')
        best_start = 0

        for r in range(len(s)):
            c = s[r]
            if c in need:
                have[c] = have.get(c, 0) + 1
                if have[c] == need[c]:
                    formed += 1

            while formed == required:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_start = l

                left_char = s[l]
                if left_char in need:
                    have[left_char] -= 1
                    if have[left_char] < need[left_char]:
                        formed -= 1
                l += 1

        return "" if best_len == float('inf') else s[best_start:best_start + best_len]