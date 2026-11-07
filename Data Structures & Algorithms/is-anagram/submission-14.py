class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = Counter(s)
        if len(s) != len(t):
            return False
        for i in t:
            count[i] -= 1
            if count[i] < 0:
                return False
        return True
        