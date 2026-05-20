class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrm_map = {}
        for string in strs:
            sort = "".join(sorted(string))
            if sort not in anagrm_map:
                anagrm_map[sort] = []
            anagrm_map[sort].append(string)
        return list(anagrm_map.values())