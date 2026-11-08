# Definition for a binary tree node.
from collections import deque


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

    def invertTree2(self, root: TreeNode | None) -> TreeNode | None:
        # Time: O(n) Space: O(n)
        if root is None:
            return None

        q = deque([root])

        while q:
            node = q.popleft()
            temp = node.left
            node.left = node.right
            node.right = temp

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return root
