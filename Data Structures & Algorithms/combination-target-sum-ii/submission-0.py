from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        combination = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(combination.copy())
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Prune: if this number is too big, all later ones are too
                if candidates[i] > remaining:
                    break

                combination.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])
                combination.pop()

        backtrack(0, target)
        return result