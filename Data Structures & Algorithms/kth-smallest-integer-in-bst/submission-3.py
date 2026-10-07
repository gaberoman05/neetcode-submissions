# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        # best data structure for fast insertion
        def findSmallest(node: Optional[TreeNode]):
            if node is None:
                return
            findSmallest(node.left)
            result.append(node.val)
            findSmallest(node.right)
        findSmallest(root)
        return result[k-1]