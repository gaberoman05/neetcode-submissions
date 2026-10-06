# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # BST means 3 scenarios by comparing value
            # 1. one greater than root, one less -> LCA is root
            # 2. both greater -> rightside, LCA is first found (p,q)
            # 3. both less -> leftside, LCA is first found (p,q)
        if (root.val >= p.val and root.val <= q.val) or (root.val <= p.val and root.val >= q.val):
            return root
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)