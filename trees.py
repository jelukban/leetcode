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


# 230. Kth Smallest Element in BST
def kthSmallest(root, k):
    values = []
    to_visit = [root]

    while to_visit:
        current = to_visit.pop()
        values.append(current.val)

        if current.left:
            to_visit.append(current.left)
        if current.right:
            to_visit.append(current.right)

    values.sort()
    return values[k-1]


# 101. Symmetric Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root):
    symmetricTree = flipTree(root)

    return treesAreEqual(root, symmetricTree)


def flipTree(root, new_tree_root=None, new_tree=None):
    if new_tree is None:
        new_tree = TreeNode(root.val)
        new_tree_root = new_tree

    if root.left:
        new_tree.right = TreeNode(root.left.val)
        flipTree(root.left, new_tree_root, new_tree.right)
    if root.right:
        new_tree.left = TreeNode(root.right.val)
        flipTree(root.right, new_tree_root, new_tree.left)

    return new_tree_root


def treesAreEqual(self, tree1, tree2):
    if tree1 is None:
        return tree2 is None
    if tree2 is None:
        return False
    if tree1.val != tree2.val:
        return False

    return treesAreEqual(tree1.left, tree2.left) and treesAreEqual(tree1.right, tree2.right)
