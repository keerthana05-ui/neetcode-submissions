import heapq
from typing import List
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)
        
        queue = deque()  
        time = 0
        
        while max_heap or queue:
            time += 1
            
            if max_heap:
                count = heapq.heappop(max_heap) + 1
                if count != 0:
                    queue.append((count, time + n))
            
            if queue and queue[0][1] == time:
                count, _ = queue.popleft()
                heapq.heappush(max_heap, count)
        
        return time