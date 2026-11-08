class Solution:
    def getFormat(self, s: str) -> str:
        map = {}
        ss = []

        for index, char in enumerate(s):
            if char not in map:
                map[char] = str(index)
            ss.append(map[char])
        return " ".join(ss)

    def isIsomorphic(self, s: str, t: str) -> bool:
        sLength = len(s)
        tLength = len(t)

        if sLength != tLength:
            return False

        sFormat = self.getFormat(s)
        tFormat = self.getFormat(t)

        return sFormat == tFormat

    def isIsomorphic2(self, s: str, t: str) -> bool:
        sLength = len(s)
        tLength = len(t)

        if sLength != tLength:
            return False

        s_t_map = {}
        t_s_map = {}

        for s_char, t_char in zip(s, t):
            if s_char not in s_t_map:
                s_t_map[s_char] = t_char
            if t_char not in t_s_map:
                t_s_map[t_char] = s_char

            if s_t_map[s_char] != t_char or t_s_map[t_char] != s_char:
                return False

        return True


def main() -> None:
    solution = Solution()
    res = solution.isIsomorphic("f11", "b23")
    print("res ", res)


main()
