class Solution:
    # Time Complexity: O(M+N), M is the length of pattern. N is the length of s
    # Space Complexity: O(N)
    def wordPattern(self, pattern: str, s: str) -> bool:
        sArr = s.split(" ")
        if len(pattern) != len(sArr):
            return False

        p_s_map = {}
        s_p_map = {}

        for char, word in zip(pattern, sArr):
            if char not in p_s_map:
                p_s_map[char] = word
            if word not in s_p_map:
                s_p_map[word] = char

            if char in p_s_map and p_s_map[char] != word:
                return False
            if word in s_p_map and s_p_map[word] != char:
                return False

        return True

    # Time Complexity: O(M+N), M is the length of pattern. N is the length of s
    # Space Complexity: O(N)
    def wordPattern2(self, pattern: str, s: str) -> bool:
        sArr = s.split(" ")
        if len(pattern) != len(sArr):
            return False

        map = {}
        for index in range(len(pattern)):
            char = pattern[index]
            word = sArr[index]

            charIndex = f"char_{char}"
            wordIndex = f"word_{word}"

            if charIndex not in map:
                map[charIndex] = index
            if wordIndex not in map:
                map[wordIndex] = index

            if map[charIndex] != map[wordIndex]:
                return False

        return True
