class Solution:
    def isBadVersion(self, version: int) -> bool:

        if version // 2 == 0:
            return True

        return False

    # Time: O(lgn) Space: O(1)
    def firstBadVersion(self, n: int) -> int:

        left = 1
        right = n
        mid = (left + right) // 2

        if self.isBadVersion(1):
            return left

        while True:
            if self.isBadVersion(mid):
                if (mid - left) == 1:
                    return mid
                else:
                    right = mid
            else:
                if (right - mid) == 1:
                    return right
                else:
                    left = mid

            mid = (left + right) // 2
