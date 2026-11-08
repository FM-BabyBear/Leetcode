from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # recursive
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        if root.left or root.right:
            maxLeftDepth = self.maxDepth(root.left)
            maxRightDepth = self.maxDepth(root.right)
            return max(maxLeftDepth, maxRightDepth) + 1
        else:
            return 1

    # iteration
    def maxDepth2(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        s = [(1, root)]
        depth = 0

        while s:
            currentLength, node = s.pop()
            depth = max(currentLength, depth)

            if node.left:
                s.append((depth + 1, node.left))
            if node.right:
                s.append((depth + 1, node.right))

        return depth

    # BFS
    def maxDepth3(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        n = 0
        q = deque([root])

        while q:
            n = n + 1
            length = len(q)

            while length:
                cur = q.popleft()
                length = length - 1
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return n
