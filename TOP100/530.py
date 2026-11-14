# A Binary Search Tree (BST) is a binary tree where each node follows these rules:
# 1. Left subtree: All values are smaller than the current node.
# 2. Right subtree: All values are greater than the current node.
# 3. Both left and right subtrees must also be BSTs.

from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time: O(n)
    # Space: O(n)
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        list = []
        minDiff = 10**6

        def traverse(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            traverse(node.left)
            list.append(node.val)
            traverse(node.right)

        traverse(root)
        for i in range(1, len(list)):
            minDiff = min(minDiff, list[i] - list[i - 1])

        return minDiff

    # Time: O(n)
    # Space: O(logn)
    def getMinimumDifference2(self, root: Optional[TreeNode]) -> int:
        self.minDiff = 10**6
        self.prevNodeVal = None

        def traverse(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            traverse(node.left)
            if self.prevNodeVal:
                self.minDiff = min(self.minDiff, node.val - self.prevNodeVal)

            self.prevNodeVal = node.val
            traverse(node.right)

        traverse(root)

        return self.minDiff

    def getMinimumDifference3(self, root: Optional[TreeNode]) -> int:
        list = []
        minDiff = 10**6

        def traverse(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            traverse(node.left)
            list.append(node.val)
            traverse(node.right)

        traverse(root)
        list.sort()
        for i in range(1, len(list)):
            minDiff = min(minDiff, list[i] - list[i - 1])

        return minDiff
