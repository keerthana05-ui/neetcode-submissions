class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python's heapq is a Min-Heap by default. 
        # To make it a Max-Heap, we multiply all numbers by -1.
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)  # Heaviest stone (most negative)
            second = heapq.heappop(stones) # Second heaviest stone (second most negative)
            
            if first != second:
                # Since they are negative, subtracting them gives the correct new weight
                # and we push it back as a negative number.
                heapq.heappush(stones, first - second)
                
        # If a stone remains, convert it back to positive; otherwise return 0
        return -stones[0] if stones else 0