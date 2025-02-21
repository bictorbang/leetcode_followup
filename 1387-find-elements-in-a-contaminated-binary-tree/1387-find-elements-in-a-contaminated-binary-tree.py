class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.node = set()
        def decontaminate(node, val):
            if not node:
                return
            self.node.add(val)
            decontaminate(node.right, 2 * val + 2)
            decontaminate(node.left, 2 * val + 1)
        decontaminate(root, 0)
    def find(self, target: int) -> bool:
        return target in self.node