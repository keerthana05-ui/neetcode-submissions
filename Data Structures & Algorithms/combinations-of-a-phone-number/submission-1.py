from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Edge case: empty input
        if not digits:
            return []

        # Mapping from digit character to its letters
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        current = []

        def backtrack(index):
            # If we've processed every digit, save the current combination
            if index == len(digits):
                res.append("".join(current))
                return

            # Get the letters that this digit maps to
            letters = mapping[digits[index]]

            # Try each letter as the choice for this digit
            for letter in letters:
                current.append(letter)      # choose
                backtrack(index + 1)        # explore
                current.pop()               # un-choose

        backtrack(0)
        return res