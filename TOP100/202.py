# 1. 理解为什么第三种情况不会发生
# 2. 理解两种算法的时间复杂度
# 3. 自己手写一下这两种算法

from collections import deque


class Solution:
    def getNext(self, n: int) -> int:
        next = 0
        while n > 0:
            n, d = divmod(n, 10)
            next += d * d
        return next

    def isHappy(self, n: int) -> bool:
        def inner(n: int) -> bool:

            if n == 1:
                return True
            elif n in visited:
                return False
            else:
                visited.add(n)
                next = self.getNext(n)
                return inner(next)

        visited = set()
        return inner(n)

    def isHappy2(self, n: int) -> bool:
        visited = set()

        while n != 1 and n not in visited:
            visited.add(n)
            n = self.getNext(n)

        return n == 1

    def isHappy3(self, n: int) -> bool:
        slow = n
        fast = self.getNext(n)

        while fast != 1 and slow != fast:
            slow = self.getNext(slow)
            fast = self.getNext(self.getNext(fast))

        return fast == 1


def main() -> None:
    solution = Solution()
    res = solution.isHappy3(2)
    print("res ", res)


main()
