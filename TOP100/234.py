class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # Time: O(n) Space: O(n)
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
