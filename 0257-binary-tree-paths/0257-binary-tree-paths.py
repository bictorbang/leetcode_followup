# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(node, cur):
            if not node.left and not node.right:
                res.append(cur + str(node.val))
                return 
            if node.left:
                dfs(node.left, cur + str(node.val) + "->")
            if node.right:
                dfs(node.right, cur + str(node.val) + "->")
        dfs(root, cur = "")
        return res