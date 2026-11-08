# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time: O(n) Space: O(logn)
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None

        root.left = self.invertTree(root.right)
        root.right = self.invertTree(root.left)

        return root
