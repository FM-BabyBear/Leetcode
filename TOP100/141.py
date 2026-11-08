# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        next = head

        while next:
            if next in visited:
                return True
            visited.add(next)
            next = next.next

        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:

        if head.next is None:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next

        return False
