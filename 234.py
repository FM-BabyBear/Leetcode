class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head

        p = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return p

    # Time: O(n) Space: O(n)
    def isPalindrome(self, head: ListNode | None) -> bool:
        reverseHead = self.reverseList(head)

        while head:
            if head.val == reverseHead.val:
                head = head.next
                reverseHead = reverseHead.next
            else:
                return False
        return True
