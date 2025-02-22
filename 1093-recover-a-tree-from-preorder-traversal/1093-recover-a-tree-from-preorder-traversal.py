# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        nodes = [(len(node[1]), int(node[2])) for node in re.findall("((-*)(\d+))", traversal)][::-1]
        def dfs(cur_dash):
            if not nodes or cur_dash != nodes[-1][0]: return
            node = TreeNode(nodes.pop()[1], dfs(cur_dash + 1), dfs(cur_dash + 1))
            return node

        return dfs(0)


        