from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        current = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start):
            # If we've consumed the whole string, save the partition
            if start == len(s):
                res.append(current.copy())
                return

            # Try every possible end position for the next piece
            for end in range(start, len(s)):
                piece = s[start:end + 1]
                if not is_palindrome(piece):
                    continue

                current.append(piece)          # choose
                backtrack(end + 1)             # explore
                current.pop()                  # un-choose

        backtrack(0)
        return res