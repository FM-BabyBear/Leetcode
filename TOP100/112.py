# 1. recursive
# 2. iteration
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None:
            return root.val == targetSum

        rest = targetSum - root.val
        leftHasPathSum = False
        rightHasPathSum = False

        if root.left:
            leftHasPathSum = self.hasPathSum(root.left, rest)
        if root.right:
            rightHasPathSum = self.hasPathSum(root.right, rest)
        return leftHasPathSum or rightHasPathSum

    # iteration: dfs
    def hasPathSum2(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False

        q = [(root, targetSum)]

        while q:
            cur, sum = q.pop()
            length = len(q)

            while length:
                length = length - 1
                if cur.left is None and cur.right is None and cur.val == sum:
                    return True
                if cur.left:
                    q.append((cur.left, sum - cur.val))
                if cur.right:
                    q.append((cur.right, sum - cur.val))

        return False
