from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isMirror(self, n1: TreeNode | None, n2: TreeNode | None) -> bool:
        if n1 is None and n2 is None:
            return True

        if n1 is None or n2 is None:
            return False

        if n1.val == n2.val:
            return self.isMirror(n1.left, n2.right) and self.isMirror(n1.right, n2.left)

    # recursive
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        return self.isMirror(root.left, root.right)

    # iteration
    def isSymmetric2(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        q = deque([root.left, root.right])

        while q:
            q1 = q.popleft()
            q2 = q.popleft()

            if q1 is None and q2 is None:
                continue

            if q1 is None or q2 is None:
                return False

            if q1.val != q2.val:
                return False

            if (q1.left is not None) != (q2.right is not None):
                return False

            if q1.left is not None:
                q.append(q1.left)
                q.append(q2.right)

            if (q1.right is not None) != (q2.left is not None):
                return False

            if q1.right is not None:
                q.append(q1.right)
                q.append(q2.left)

        return True
