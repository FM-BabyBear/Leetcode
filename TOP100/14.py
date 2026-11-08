from typing import List
import math


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = ""
        first = strs[0]
        for i in range(len(first)):
            for j in range(1, len(strs)):
                if strs[j][i] != first[i]:
                    return prefix
            prefix += first[i]
        return prefix

    def longestCommonPrefix1(self, strs: List[str]) -> str:
        strLength = len(strs)
        if strLength == 0:
            return ""
        prefix = strs[0]

        for i in range(1, strLength):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0 : len(prefix) - 1]
                if prefix == 0:
                    return ""
        return prefix

    def mergeCommonPrefix(self, left: str, right: str) -> str:

        prefix = left

        while right.find(prefix) != 0:
            prefix = prefix[: len(prefix) - 1]

        return prefix

    # divide and conqure
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        strLength = len(strs)
        if strLength == 0:
            return ""

        if strLength == 1:
            return strs[0]

        left = self.longestCommonPrefix2(strs[: strLength // 2])
        right = self.longestCommonPrefix2(strs[strLength // 2 :])
        return self.mergeCommonPrefix(left, right)

    def isCommonPrefix(self, strs: List[str], s: str) -> bool:
        arrLength = len(strs)
        i = 0

        while i < arrLength:
            if strs[i].find(s) != 0:
                return False
            i += 1

        return True

    # Binary Search
    def longestCommonPrefix3(self, strs: List[str]) -> str:
        minLen = minLen = min(len(s) for s in strs)

        left = 0
        right = minLen
        firstStr = strs[0]
        lcp = ""

        while left <= right:
            mid = (left + right) // 2

            if self.isCommonPrefix(strs, firstStr[:mid]):
                lcp = firstStr[:mid]
                left = mid + 1
            else:
                right = mid - 1

        return lcp


def main() -> None:
    solution = Solution()
    longestCommonPrefix = solution.longestCommonPrefix3(["flower", "flow", "flight"])
    print("longestCommonPrefix ", longestCommonPrefix)


main()
