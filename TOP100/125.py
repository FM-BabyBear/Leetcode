class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join(c.lower() for c in s if c.isalnum())
        if s1 == "":
            return True
        mid = len(s1) // 2
        for i in range(mid):
            if s1[i] != s1[-i + 1]:
                return False

        return True
