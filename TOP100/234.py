class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # Time: O(n) Space: O(n) n: number of list
    def isPalindrome(self, head: ListNode | None) -> bool:
        self.frontierNode = head

        def recursiveCheck(currentNode=head) -> bool:
            if currentNode is not None:
                if not recursiveCheck(currentNode.next):
                    return False
                if self.frontierNode.val != currentNode.val:
                    return False

                self.frontierNode = self.frontierNode.next
                return True

            return True

        recursiveCheck()

    def reverse(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head

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

    def firstHalfEnd(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return head

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # Time: O(n) Space: O(1)
    def isPalindrome2(self, head: ListNode | None) -> bool:
        if head is None:
            return False
        firstHalfEnd = self.firstHalfEnd(head)
        secondHalfHead = self.reverse(firstHalfEnd.next)
        print(secondHalfHead)
        result = True

        firstHalfStart = head
        secondHalfStart = secondHalfHead

        while firstHalfStart and secondHalfStart:
            if firstHalfStart.val != secondHalfStart.val:
                result = False
            firstHalfStart = firstHalfStart.next
            secondHalfStart = secondHalfStart.next
        firstHalfEnd.next = self.reverse(secondHalfHead)
        print(head)
        return result
