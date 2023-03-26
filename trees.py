# 104. Maximum Depth of Binary Search Tree
def maxDepth(root):
    if root == None:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))


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


# 111. Minimum Depth of Binary Tree
def minDepth(root):
    if root == None:
        return 0

    if root.left and root.right:
        return 1 + min(minDepth(root.left), minDepth(root.right))
    elif root.left == None:
        return 1 + minDepth(root.right)
    elif root.right == None:
        return 1 + minDepth(root.left)


# 94. Binary Tree Inorder Traversal
def inorderTraversal(root):
    if root:
        return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

    return []
