class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # 1. Create the map so we can instantly find where a root is in inorder
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # 2. Our pointer for the preorder list. It starts at the first element (index 0).
        pre_idx = 0
        
        # 3. The magic recursive function
        def build(left, right):
            # We need this to modify the pre_idx from the outer function
            nonlocal pre_idx
            
            # BASE CASE: If left > right, we have no numbers left to process.
            # This means we are at the bottom of a branch. Return None.
            if left > right:
                return None
            
            # STEP 1: Get the root (first number in preorder)
            root_val = preorder[pre_idx]
            pre_idx += 1  # Move the pointer forward for the next node!
            root = TreeNode(root_val)
            
            # STEP 2: Find where this root is in the inorder list
            mid = inorder_map[root_val]
            
            # STEP 3: Build the left and right sides
            # Left side uses everything before 'mid'
            root.left = build(left, mid - 1)
            # Right side uses everything after 'mid'
            root.right = build(mid + 1, right)
            
            return root
            
        # Start building with the whole inorder list
        return build(0, len(inorder) - 1)