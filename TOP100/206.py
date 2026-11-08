# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:

        if head is None:
            return None

        prev = None
        cur = head
        next = head.next

        while cur:
            cur.next = prev

            prev = cur
            cur = next
            if next:
                next = next.next

        return prev

    def reverseList2(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head

        p = self.reverseList2(head.next)

        head.next.next = head
        head.next = None

        return p
