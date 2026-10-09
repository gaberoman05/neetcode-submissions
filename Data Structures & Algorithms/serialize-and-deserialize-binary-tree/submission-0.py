# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        serial = []
        def dfs(root):
            nonlocal serial
            if root is None:
                serial.append("N")
                return 
            serial.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(serial)
        # example of what the serial will look like:
        # ",1,2,null,null,3,4,5"

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # from the string, parse by ,
        vals = data.split(",")
        idx = 0 

        def dfs():
            nonlocal idx
            if vals[idx] == "N":
                idx += 1
                return None
            node = TreeNode(int(vals[idx]))
            idx += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


