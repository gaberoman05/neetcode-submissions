# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Swap left and right child node for every tree
        if root is None:
            return
        else:
            left_temp = root.left
            root.left = root.right
            root.right = left_temp
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
            
            

        