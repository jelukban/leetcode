# 104. Maximum Depth of Binary Search Tree
def maxDepth(root):
    if root == None:
        return 0

    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))