from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSame(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        q1 = deque([root])
        q2 = deque([subRoot])
        while q1 and q2:
            node1 = q1.popleft()
            node2 = q2.popleft()

            if node1 and node2 and node1.val == node2.val:
                q1.append(node1.left)
                q1.append(node1.right)
                q2.append(node2.left)
                q2.append(node2.right)
            elif node1 is None and node2 is None:
                continue
            else:
                return False

        return len(q1) == 0 and len(q2) == 0

    # Time: O(mn) m: number of nodes in root / n: number of nodes in subRoot
    # Space: O(m+n)
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode) -> bool:

        queue = deque([root])
        result = False
        while queue:
            node = queue.popleft()
            if node is None:
                continue

            if node.val == subRoot.val:
                result = self.isSame(node, subRoot)
                if result:
                    return True

            if not result:
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return result

    def identical(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if root is None or subRoot is None:
            return root is None and subRoot is None

        return (
            root.val == subRoot.val
            and self.identical(root.left, subRoot.left)
            and self.identical(root.right, subRoot.right)
        )

    # Time: O(mn) m: number of nodes in root / n: number of nodes in subRoot
    # Space: O(m+n)
    def isSubtree2(self, root: TreeNode | None, subRoot: TreeNode) -> bool:

        if root is None:
            return False

        if self.identical(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(
                root.right, subRoot
            )
