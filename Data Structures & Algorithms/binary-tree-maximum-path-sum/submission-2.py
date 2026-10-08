# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # first: define what a path can be and how it can be explored
            # path is any string of nodes where they can all be connected by an edge
        # discover how to traverse a path -> keep a running max 
        # how would you get full coverage of a tree such that you explore every possible path
            # a path will always at least include a child and parent node
                # perhaps check every child and parent sum?
                # each node, check max of root.val, root.val + left, root.val + right, root + both)

                max_sum = root.val

                def checkNodeSum(root):
                    nonlocal max_sum
                    if root is None:
                        return 0
                    left = checkNodeSum(root.left)
                    right = checkNodeSum(root.right)
                    max_sum =  max(max_sum, root.val + left + right, root.val + left, root.val + right, root.val)
                    return root.val + max(left, right, 0)
                checkNodeSum(root)
                return max_sum
        