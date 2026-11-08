class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        i = len(s)
        sum = map[s[i - 1]]

        for i in reversed(range(len(s) - 1)):
            if map[s[i]] < map[s[i + 1]]:
                sum -= map[s[i]]
            else:
                sum += map[s[i]]
        return sum

    def romanToInt1(self, s: str) -> int:
        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        sum = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1:
                char = (s[i], s[i + 1])
                if map[char[0]] < map[char[1]]:
                    sum += map[char[1]] - map[char[0]]
                    i += 2
                else:
                    sum += map[char[0]]
                    i += 1
            else:
                sum += map[s[i]]
                i += 1

        return sum
