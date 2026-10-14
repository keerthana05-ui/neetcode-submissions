class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        current = []
        def backtrack(open, close):
            if open == n and close == n:
                res.append("".join(current))
                return
            if open < n:
                current.append("(")
                backtrack(open + 1, close)
                current.pop()
            if close < open:
                current.append(")")
                backtrack(open, close + 1)
                current.pop()
        backtrack(0,0)
        return res
