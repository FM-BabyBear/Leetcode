class Solution:
    # Time: O(m+n) m: length of jewels / n: length of stones
    # Space: O(1)
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = {}
        sum = 0

        for char in stones:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1

        for char in jewels:
            if char in dict:
                sum += dict[char]

        return sum

    # Time: O(m*n) m: length of jewels / n: length of stones
    # Space: O(1)
    def numJewelsInStones2(self, jewels: str, stones: str) -> int:
        sum = 0

        for char in stones:
            if char in jewels:
                sum += 1

        return sum

    # Time: O(m+n) m: length of jewels / n: length of stones
    # Space: O(m)
    def numJewelsInStones3(self, jewels: str, stones: str) -> int:
        sum = 0
        j = set(jewels)
        for char in stones:
            if char in j:
                sum += 1

        return sum
