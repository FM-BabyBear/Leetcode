class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        left = 2
        right = num // 2

        while left <= right:
            guess = (left + right) // 2
            guessSquare = guess * guess

            if guessSquare == num:
                return True

            if guessSquare > num:
                right = guess - 1

            if guessSquare < num:
                left = guess + 1

        return False
