# 104. Maximum Depth of Binary Search Tree
def maxDepth(root):
    if root == None:
        return 0

    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# 98. Validate Binary Search Trees
def isValidBST(root):
    return isValidBST_impl(root, None, None)


def isValidBST_impl(root, min_val, max_val):
    if not root:
        return True
    if ((min_val is not None and root.val <= min_val) or
            (max_val is not None and root.val >= max_val)):
        return False

    return (isValidBST_impl(root.left, min_val, root.val) and
            isValidBST_impl(root.right, root.val, max_val))
