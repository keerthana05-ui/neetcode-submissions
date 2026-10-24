class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for i in strs:
            value = "".join(sorted(i))
            if value not in group:
                group[value] = []
            group[value].append(i)
        return list(group.values())
        