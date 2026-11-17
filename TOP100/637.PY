from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time: O(n)
    # Space: O(n)
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        arr = []
        if root is None:
            return arr

        q = deque([root])

        while q:
            sum = 0
            length = len(q)

            for _ in range(length):
                node = q.popleft()
                sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            arr.append(sum / length)
        return arr

    def calculate(
        self, node: TreeNode | None, l: int, sum: list[float], count: list[int]
    ):
        if node is None:
            return

        if l < len(sum):
            sum[l] += node.val
            count[l] += 1
        else:
            sum.append(node.val)
            count.append(1)

        self.calculate(node.left, l + 1, sum, count)
        self.calculate(node.right, l + 1, sum, count)

    # Time: O(n)
    # Space: O(logn)
    def averageOfLevels2(self, root: TreeNode | None) -> list[float]:
        sum = []
        count = []

        self.calculate(root, 0, sum, count)

        for i in range(len(sum)):
            sum[i] = sum[i] / count[i]
        return sum
