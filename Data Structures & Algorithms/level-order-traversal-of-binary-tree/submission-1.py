from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        result = []
        queue = deque([root])
        
        while queue:
            # 1. Take a snapshot of the current level size
            level_size = len(queue)
            current_level = []
            
            # 2. Process exactly that many nodes
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # 3. Add children to the queue for the NEXT level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            # 4. Add the completed level to our result
            result.append(current_level)
            
        return result