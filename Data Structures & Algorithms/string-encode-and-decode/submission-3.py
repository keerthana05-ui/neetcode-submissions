class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s)) + "#" + s)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        final = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = j + length + 1
            final.append(s[start : end])
            i = end
        return final
