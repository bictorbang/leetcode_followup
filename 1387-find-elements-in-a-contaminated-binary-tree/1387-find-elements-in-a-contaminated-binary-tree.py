# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        self.hashmap = [0]
        cur = self.root
        def decontaminate(node):
            if node.left:
                node.left.val = 2 * node.val + 1
                self.hashmap.append(node.left.val)
                decontaminate(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                self.hashmap.append(node.right.val)
                decontaminate(node.right)
        decontaminate(cur)

    def find(self, target: int) -> bool:
        return target in self.hashmap
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)