class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time: O(max(m,n)) m: length of l1 / n: length of l2
    # Space: O(1)

    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        num1 = 0
        num2 = 0
        digit = 0

        while l1 is not None or l2 is not None:
            if l1 and l1.val:
                num1 = l1.val * 10**digit + num1

            if l2 and l2.val:
                num2 = l2.val * 10**digit + num2
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            digit += 1

        sum = num1 + num2
        head = ListNode(0)
        cur = head

        if sum == 0:
            return head

        while sum > 0:
            sum, d = divmod(sum, 10)
            next = ListNode(d)
            cur.next = next
            cur = cur.next

        return head.next

    # Time: O(max(m,n)) m: length of l1 / n: length of l2
    # Space: O(1)
    def addTwoNumbers2(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        head = ListNode(0)
        cur = head
        num1 = 0
        num2 = 0
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            if l1:
                num1 = l1.val if l1.val else 0
                l1 = l1.next
            else:
                num1 = 0

            if l2:
                num2 = l2.val if l2.val else 0
                l2 = l2.next
            else:
                num2 = 0

            total = num1 + num2 + carry
            carry, d = divmod(total, 10)
            cur.next = ListNode(d)
            cur = cur.next

        return head.next
