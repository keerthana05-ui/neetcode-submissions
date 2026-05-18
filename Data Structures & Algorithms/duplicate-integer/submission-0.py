class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no = set()
        for num in nums:
            if num in no:
                return True
            no.add(num)
        return False

