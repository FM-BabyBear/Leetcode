from collections import deque

# 1. from top to bottom
# 2. from bottom to top


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def calHeight(self, root: TreeNode | None) -> int:
        if root is None:
            return -1

        leftHeight = self.calHeight(root.left)
        rightHeight = self.calHeight(root.right)

        height = max(leftHeight, rightHeight) + 1

        return height

    def isBalanced(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        leftNodeHeight = self.calHeight(root.left)
        rightNodeHeight = self.calHeight(root.right)

        return (
            abs(leftNodeHeight - rightNodeHeight) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )

    def isBalancedHelper(self, root: TreeNode | None) -> tuple[bool, int]:
        if root is None:
            return (True, -1)

        isLeftBalenced, leftNodeHeight = self.isBalancedHelper(root.left)
        isRightBalenced, rightNodeHeight = self.isBalancedHelper(root.right)

        return (
            abs(leftNodeHeight - rightNodeHeight) <= 1
            and isLeftBalenced
            and isRightBalenced,
            max(leftNodeHeight, rightNodeHeight) + 1,
        )

    def isBalanced2(self, root: TreeNode | None) -> bool:
        return self.isBalancedHelper(root)[0]
