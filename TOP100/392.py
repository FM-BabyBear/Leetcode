# Undown
import bisect


class Solution:
    # Time: O(MN) M: length of s; N: length of t
    # Space: O(1)
    def isSubsequence(self, s: str, t: str) -> bool:

        sLength = len(s)
        tLength = len(t)

        if sLength > tLength:
            return False

        for char in s:
            if t:
                index = t.find(char)

                if index == -1:
                    return False

                t = t[index + 1 :]
            else:
                return False
        return True

    # DP
    # Time: O(MN) M: length of s; N: length of t
    # Space: O(MN)
    def isSubsequence2(self, s: str, t: str) -> bool:

        sLength = len(s)
        tLength = len(t)
        dp = [[0 for _ in range(tLength + 1)] for _ in range(sLength + 1)]

        for i in range(1, sLength + 1):
            for j in range(1, tLength + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                    continue

                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = (
                        dp[i - 1][j] if dp[i - 1][j] > dp[i][j - 1] else dp[i][j - 1]
                    )
        return dp[sLength][tLength] == sLength

    # Time: O(M + log(N)) M: length of s; N: length of t
    # Space: O(N)
    def isSubsequence3(self, s: str, t: str) -> bool:
        dict = {}
        for index, char in enumerate(t):
            if char in dict:
                dict[char].append(index)
            else:
                dict[char] = []

        curMatchIndex = -1
        for char in s:
            if char in dict:
                matchIndex = bisect.bisect_right(dict[char], curMatchIndex)
                if matchIndex == len(dict[char]):
                    return False
                curMatchIndex = dict[char][matchIndex]
            else:
                return False

        return True

    # Time: O(N) M: length of s; N: length of t
    # Space: O(1)
    def isSubsequence4(self, s: str, t: str) -> bool:

        sLength = len(s)
        tLength = len(t)

        sPointer = 0
        tPointer = 0

        while sPointer < sLength and tPointer < tLength:
            if s[sPointer] == t[tPointer]:
                sPointer += 1
            tPointer += 1

        return sPointer == sLength

    # Time: O(N) M: length of s; N: length of t
    # Space: O(N)
    def isSubsequence5(self, s: str, t: str) -> bool:
        sLength = len(s)
        tLength = len(t)

        def recursiveSub(sIndex: int, tIndex: int) -> bool:

            if sIndex == sLength:
                return True
            if tIndex == tLength:
                return False

            if s[sIndex] == t[tIndex]:
                sIndex += 1

            tIndex += 1

            return recursiveSub(sIndex, tIndex)

        return recursiveSub(0, 0)
