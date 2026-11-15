from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time: O(n)
    # Space: O(logn)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def longestPath(node: Optional[TreeNode]) -> int:
            nonlocal diameter

            if not node:
                return -1

            leftPath = longestPath(node.left)
            rightPath = longestPath(node.right)

            diameter = max(diameter, leftPath + rightPath + 2)

            return max(leftPath, rightPath) + 1

        longestPath(root)
        return diameter
