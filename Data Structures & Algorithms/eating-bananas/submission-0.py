class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(k:int) -> bool:
            hours = 0
            for pile in piles:
                hours += (pile+k-1)//k
            return hours <= h
        low = 1
        high = max(piles)
        while low < high:
            mid = (low + high)//2
            if eat(mid):
                high = mid
            else:
                low = mid+1
        return low