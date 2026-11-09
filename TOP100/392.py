# Undown
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
