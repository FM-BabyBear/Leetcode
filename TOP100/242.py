class Solution:
    # Time: O(nlogn) space: O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = sorted(s)
        t1 = sorted(t)

        return s1 == t1

    # Time: O(n) space: O(1)
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        occurence = [0] * 26
        for i in range(len(s)):
            sIndex = ord(s[i]) - ord("a")
            tIndex = ord(t[i]) - ord("a")

            occurence[sIndex] = occurence[sIndex] + 1
            occurence[tIndex] = occurence[tIndex] - 1

        for num in range(26):
            if num != 0:
                return False

        return True
